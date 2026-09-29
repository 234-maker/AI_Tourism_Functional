"""
Repeatable Raw-to-Prepared Tourism Data Cleaning and Standardization Pipeline.
Layer 1: Data Layer
"""
import os
import json
import csv
import sqlite3
from typing import Dict, Any, List

def time_to_minutes(time_str: str) -> int:
    """Convert HH:MM string to minutes past midnight."""
    if not time_str or ":" not in time_str:
        return 0
    parts = time_str.split(":")
    return int(parts[0]) * 60 + int(parts[1])

def clean_and_prepare():
    raw_path = os.path.join("data", "raw", "raw_attractions_up.json")
    with open(raw_path, "r", encoding="utf-8") as f:
        raw_items = json.load(f)

    prepared_items = []
    cities_summary = {}

    for item in raw_items:
        attraction_id = item["id"].strip()
        name = item["name"].strip()
        city = item["city"].strip()
        state = item["state"].strip()
        category = item["category"].strip()

        # Normalize timings
        timings = item.get("timings", {})
        open_time = timings.get("open_time", "08:00")
        close_time = timings.get("close_time", "18:00")
        open_mins = time_to_minutes(open_time)
        close_mins = time_to_minutes(close_time)
        closed_days = timings.get("closed_on", [])
        best_time = timings.get("best_time_to_visit", "Anytime")

        # Entry fee normalization
        fees = item.get("entry_fee_inr", {})
        adult_fee = float(fees.get("indian_adult", 0))
        child_fee = float(fees.get("indian_child", 0))
        foreigner_fee = float(fees.get("foreigner", adult_fee))

        # Accessibility normalization
        acc = item.get("accessibility", {})
        is_wheelchair = bool(acc.get("wheelchair_accessible", False))
        is_senior = bool(acc.get("senior_citizen_friendly", False))
        walking_intensity = acc.get("walking_intensity", "Medium")

        # Family friendly
        fam = item.get("family_friendly", {})
        is_family = bool(fam.get("suitable", True))

        # Location validation
        loc = item.get("location", {})
        lat = float(loc.get("latitude", 0.0))
        lon = float(loc.get("longitude", 0.0))

        # Validate UP bounding box: lat ~ 23.5-31.0, lon ~ 77.0-85.0
        assert 23.0 <= lat <= 31.0, f"Invalid latitude {lat} for {name}"
        assert 76.5 <= lon <= 85.5, f"Invalid longitude {lon} for {name}"

        # Source provenance
        source = item.get("source", {})
        source_name = source.get("organization", "UP Tourism")
        source_url = source.get("official_url", "https://uptourism.gov.in")
        is_mock = bool(source.get("is_mock", False))

        # Search tokens & semantic text representation for RAG Layer
        search_blob = f"{name} {city} {category} {' '.join(item.get('interests', []))} {item.get('description', '')} {' '.join(item.get('highlights', []))}"

        prepared_record = {
            "id": attraction_id,
            "name": name,
            "city": city,
            "state": state,
            "category": category,
            "interests": item.get("interests", []),
            "description": item.get("description", "").strip(),
            "highlights": item.get("highlights", []),
            "open_time": open_time,
            "close_time": close_time,
            "open_time_mins": open_mins,
            "close_time_mins": close_mins,
            "closed_days": closed_days,
            "best_time_to_visit": best_time,
            "fee_adult_inr": adult_fee,
            "fee_child_inr": child_fee,
            "fee_foreigner_inr": foreigner_fee,
            "indicative_duration_hours": float(item.get("indicative_duration_hours", 1.5)),
            "wheelchair_accessible": is_wheelchair,
            "senior_friendly": is_senior,
            "walking_intensity": walking_intensity,
            "accessibility_notes": acc.get("notes", ""),
            "family_friendly": is_family,
            "family_notes": fam.get("notes", ""),
            "area": loc.get("area", ""),
            "latitude": lat,
            "longitude": lon,
            "nearby_transit": loc.get("nearby_metro", ""),
            "nearby_facilities": item.get("nearby_facilities", []),
            "transport_hints": item.get("transport_hints", ""),
            "source_name": source_name,
            "source_url": source_url,
            "is_mock": is_mock,
            "faqs": item.get("faqs", []),
            "search_blob": search_blob
        }
        prepared_items.append(prepared_record)

        cities_summary[city] = cities_summary.get(city, 0) + 1

    # 1. Save prepared JSON
    os.makedirs(os.path.join("data", "prepared"), exist_ok=True)
    prep_json_path = os.path.join("data", "prepared", "prepared_attractions.json")
    with open(prep_json_path, "w", encoding="utf-8") as f:
        json.dump(prepared_items, f, indent=2, ensure_ascii=False)

    # 2. Save prepared CSV
    prep_csv_path = os.path.join("data", "prepared", "prepared_attractions.csv")
    csv_fields = [
        "id", "name", "city", "category", "open_time", "close_time",
        "fee_adult_inr", "fee_foreigner_inr", "indicative_duration_hours",
        "wheelchair_accessible", "senior_friendly", "walking_intensity",
        "latitude", "longitude", "source_name", "source_url"
    ]
    with open(prep_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for item in prepared_items:
            row = {k: item[k] for k in csv_fields}
            writer.writerow(row)

    # 3. Store in SQLite Database
    sqlite_path = os.path.join("data", "prepared", "tourism_db.sqlite")
    conn = sqlite3.connect(sqlite_path)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS attractions")
    cur.execute("DROP TABLE IF EXISTS attraction_faqs")
    cur.execute("DROP TABLE IF EXISTS user_feedback")
    cur.execute("DROP TABLE IF EXISTS hallucination_audit_log")

    cur.execute("""
    CREATE TABLE attractions (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        category TEXT NOT NULL,
        interests_json TEXT,
        description TEXT,
        highlights_json TEXT,
        open_time TEXT,
        close_time TEXT,
        open_time_mins INTEGER,
        close_time_mins INTEGER,
        closed_days_json TEXT,
        best_time_to_visit TEXT,
        fee_adult_inr REAL,
        fee_child_inr REAL,
        fee_foreigner_inr REAL,
        indicative_duration_hours REAL,
        wheelchair_accessible INTEGER,
        senior_friendly INTEGER,
        walking_intensity TEXT,
        accessibility_notes TEXT,
        family_friendly INTEGER,
        family_notes TEXT,
        area TEXT,
        latitude REAL,
        longitude REAL,
        nearby_transit TEXT,
        facilities_json TEXT,
        transport_hints TEXT,
        source_name TEXT,
        source_url TEXT,
        is_mock INTEGER,
        search_blob TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE attraction_faqs (
        faq_id INTEGER PRIMARY KEY AUTOINCREMENT,
        attraction_id TEXT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        FOREIGN KEY (attraction_id) REFERENCES attractions(id)
    )
    """)

    cur.execute("""
    CREATE TABLE user_feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        destination TEXT,
        rating INTEGER,
        feedback_category TEXT,
        comment TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE hallucination_audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT,
        generated_response TEXT,
        grounding_score REAL,
        cited_sources TEXT,
        flagged_unsupported_claims TEXT,
        status TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    placeholders = ", ".join(["?"] * 34)
    for p in prepared_items:
        cur.execute(f"INSERT INTO attractions VALUES ({placeholders})", (
            p["id"], p["name"], p["city"], p["state"], p["category"],
            json.dumps(p["interests"]), p["description"], json.dumps(p["highlights"]),
            p["open_time"], p["close_time"], p["open_time_mins"], p["close_time_mins"],
            json.dumps(p["closed_days"]), p["best_time_to_visit"],
            p["fee_adult_inr"], p["fee_child_inr"], p["fee_foreigner_inr"],
            p["indicative_duration_hours"],
            1 if p["wheelchair_accessible"] else 0,
            1 if p["senior_friendly"] else 0,
            p["walking_intensity"], p["accessibility_notes"],
            1 if p["family_friendly"] else 0, p["family_notes"],
            p["area"], p["latitude"], p["longitude"],
            p["nearby_transit"], json.dumps(p["nearby_facilities"]),
            p["transport_hints"], p["source_name"], p["source_url"],
            1 if p["is_mock"] else 0, p["search_blob"]
        ))

        for faq in p["faqs"]:
            cur.execute("""
            INSERT INTO attraction_faqs (attraction_id, question, answer)
            VALUES (?, ?, ?)
            """, (p["id"], faq["question"], faq["answer"]))

    conn.commit()
    conn.close()

    print(f"Data pipeline complete! Output files generated in data/prepared/:")
    print(f" - {prep_json_path}")
    print(f" - {prep_csv_path}")
    print(f" - {sqlite_path}")
    print(f"Total attractions processed: {len(prepared_items)}")
    for city, count in cities_summary.items():
        print(f"  * {city}: {count} places")

if __name__ == "__main__":
    clean_and_prepare()
