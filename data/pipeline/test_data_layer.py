"""
Unit test suite for Layer 1: Data Layer Validation.
Ensures data consistency, required fields, geographical boundaries, and integrity.
"""
import os
import json
import sqlite3

def test_data_layer():
    print("==========================================")
    print("RUNNING LAYER 1 DATA LAYER VALIDATION TEST")
    print("==========================================")

    # 1. Test prepared JSON file existence and parsing
    prep_path = os.path.join("data", "prepared", "prepared_attractions.json")
    assert os.path.exists(prep_path), f"Missing {prep_path}"

    with open(prep_path, "r", encoding="utf-8") as f:
        attractions = json.load(f)

    assert len(attractions) >= 25, f"Expected >= 25 attractions, found {len(attractions)}"
    print(f"PASS: Verified {len(attractions)} prepared attractions in JSON.")

    # 2. Test field completeness & schema constraints
    cities = set()
    categories = set()
    for a in attractions:
        assert a["id"], "Attraction missing ID"
        assert a["name"], "Attraction missing name"
        assert a["city"], "Attraction missing city"
        assert a["description"], f"Attraction {a['name']} missing description"
        assert a["source_name"], f"Attraction {a['name']} missing source_name"
        assert a["source_url"].startswith("http"), f"Invalid source_url for {a['name']}"
        assert 23.0 <= a["latitude"] <= 31.5, f"Latitude out of UP bounds for {a['name']}"
        assert 76.0 <= a["longitude"] <= 85.5, f"Longitude out of UP bounds for {a['name']}"
        assert a["walking_intensity"] in ["Low", "Medium", "High"], f"Invalid walking intensity in {a['name']}"
        assert isinstance(a["wheelchair_accessible"], bool), f"Invalid wheelchair flag in {a['name']}"
        assert isinstance(a["senior_friendly"], bool), f"Invalid senior flag in {a['name']}"
        assert a["indicative_duration_hours"] > 0, f"Invalid duration in {a['name']}"
        cities.add(a["city"])
        categories.add(a["category"])

    print(f"PASS: Verified all attributes & bounds across cities: {', '.join(sorted(cities))}")
    print(f"PASS: Verified categories: {', '.join(sorted(categories))}")

    # 3. Test SQLite database integrity
    sqlite_path = os.path.join("data", "prepared", "tourism_db.sqlite")
    assert os.path.exists(sqlite_path), f"Missing {sqlite_path}"
    conn = sqlite3.connect(sqlite_path)
    cur = conn.cursor()

    cur.execute("SELECT count(*) FROM attractions")
    db_count = cur.fetchone()[0]
    assert db_count == len(attractions), f"DB count {db_count} mismatch with JSON count {len(attractions)}"

    cur.execute("SELECT count(*) FROM attraction_faqs")
    faq_count = cur.fetchone()[0]
    assert faq_count > 0, "No FAQs found in SQLite attraction_faqs table"

    conn.close()
    print(f"PASS: SQLite database verified with {db_count} attractions and {faq_count} grounded FAQs.")
    print("ALL LAYER 1 DATA TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_data_layer()
