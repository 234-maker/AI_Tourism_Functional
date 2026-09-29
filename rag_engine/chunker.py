"""
Semantic Document Chunking Engine for Tourism Knowledge Base.
Layer 2: RAG Layer
"""
import os
import json
from typing import List, Dict, Any

def generate_chunks_from_prepared_data() -> List[Dict[str, Any]]:
    prepared_path = os.path.join("data", "prepared", "prepared_attractions.json")
    with open(prepared_path, "r", encoding="utf-8") as f:
        attractions = json.load(f)

    chunks = []
    chunk_counter = 1

    for a in attractions:
        aid = a["id"]
        aname = a["name"]
        city = a["city"]
        cat = a["category"]
        src_org = a["source_name"]
        src_url = a["source_url"]

        # Chunk 1: Overview & Historical/Cultural Significance
        overview_text = (
            f"Destination: {aname}, {city}, Uttar Pradesh. "
            f"Category: {cat}. Interests: {', '.join(a.get('interests', []))}. "
            f"Overview: {a['description']} "
            f"Key Highlights: {', '.join(a.get('highlights', []))}."
        )
        chunks.append({
            "chunk_id": f"CHUNK-{chunk_counter:04d}",
            "attraction_id": aid,
            "attraction_name": aname,
            "city": city,
            "chunk_type": "OVERVIEW",
            "content": overview_text,
            "source_citation": f"{src_org} ({src_url})",
            "metadata": {
                "city": city,
                "category": cat,
                "interests": a.get("interests", [])
            }
        })
        chunk_counter += 1

        # Chunk 2: Practical Timings, Ticketing & Logistics
        closed_str = ", ".join(a.get("closed_days", [])) if a.get("closed_days") else "Open all days"
        fee_str = (
            f"Entry Fee: Indian Adults INR {a['fee_adult_inr']}, Children INR {a['fee_child_inr']}, "
            f"Foreigners INR {a['fee_foreigner_inr']}."
        )
        logistics_text = (
            f"Visiting Logistics for {aname} ({city}): "
            f"Opening Hours: {a['open_time']} to {a['close_time']}. Closed Days: {closed_str}. "
            f"Best time to visit: {a['best_time_to_visit']}. {fee_str} "
            f"Indicative visit duration: {a['indicative_duration_hours']} hours. "
            f"Location / Area: {a.get('area', '')}. Nearby Transit: {a.get('nearby_transit', '')}. "
            f"Transport Tips: {a.get('transport_hints', '')}."
        )
        chunks.append({
            "chunk_id": f"CHUNK-{chunk_counter:04d}",
            "attraction_id": aid,
            "attraction_name": aname,
            "city": city,
            "chunk_type": "PRACTICAL_LOGISTICS",
            "content": logistics_text,
            "source_citation": f"{src_org} ({src_url})",
            "metadata": {
                "city": city,
                "open_time": a["open_time"],
                "close_time": a["close_time"],
                "closed_days": a.get("closed_days", []),
                "fee_adult_inr": a["fee_adult_inr"]
            }
        })
        chunk_counter += 1

        # Chunk 3: Accessibility, Family & Amenities
        facilities_str = ", ".join(a.get("nearby_facilities", []))
        acc_text = (
            f"Accessibility and Visitor Comfort for {aname} ({city}): "
            f"Wheelchair Accessible: {'Yes' if a['wheelchair_accessible'] else 'No'}. "
            f"Senior Citizen Friendly: {'Yes' if a['senior_friendly'] else 'No'}. "
            f"Walking Intensity: {a['walking_intensity']}. "
            f"Accessibility Guidance: {a.get('accessibility_notes', 'Standard paved terrain')}. "
            f"Family Friendly: {'Yes' if a['family_friendly'] else 'No'}. "
            f"Family Notes: {a.get('family_notes', '')}. "
            f"On-site Facilities: {facilities_str}."
        )
        chunks.append({
            "chunk_id": f"CHUNK-{chunk_counter:04d}",
            "attraction_id": aid,
            "attraction_name": aname,
            "city": city,
            "chunk_type": "ACCESSIBILITY_FAMILY",
            "content": acc_text,
            "source_citation": f"{src_org} ({src_url})",
            "metadata": {
                "city": city,
                "wheelchair": a["wheelchair_accessible"],
                "senior_friendly": a["senior_friendly"],
                "walking_intensity": a["walking_intensity"]
            }
        })
        chunk_counter += 1

        # Chunk 4+: Dedicated FAQs
        for idx, faq in enumerate(a.get("faqs", []), start=1):
            faq_text = (
                f"Frequently Asked Question for {aname} ({city}): "
                f"Q: {faq['question']} "
                f"A: {faq['answer']}"
            )
            chunks.append({
                "chunk_id": f"CHUNK-{chunk_counter:04d}",
                "attraction_id": aid,
                "attraction_name": aname,
                "city": city,
                "chunk_type": "FAQ",
                "content": faq_text,
                "source_citation": f"{src_org} FAQ Register ({src_url})",
                "metadata": {
                    "city": city,
                    "question": faq["question"]
                }
            })
            chunk_counter += 1

    # Save chunks to data/prepared/tourism_chunks.json
    out_path = os.path.join("data", "prepared", "tourism_chunks.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"Generated {len(chunks)} semantic knowledge chunks stored in {out_path}.")
    return chunks

if __name__ == "__main__":
    generate_chunks_from_prepared_data()
