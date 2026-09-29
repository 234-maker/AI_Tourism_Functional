"""
Day-Wise Itinerary Composer and Plan Synthesizer.
Layer 3: Intelligence Layer
"""
import os
import sys
from typing import List, Dict, Any, Optional

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from intelligence.ranking import PlaceRanker
from intelligence.time_estimator import estimate_transit_time_mins, haversine_distance_km

class ItineraryComposer:
    def __init__(self):
        self.ranker = PlaceRanker()

    def compose_itinerary(
        self,
        city: str,
        duration_days: int = 2,
        interests: List[str] = None,
        budget_level: str = "Moderate",
        traveller_type: str = "Family",
        mobility_needs: str = "Standard",
        language: str = "English"
    ) -> Dict[str, Any]:
        """
        Synthesizes a realistic, day-wise itinerary with time slots, transit links,
        budget calculations, and grounded explanations.
        """
        duration_days = max(1, min(5, duration_days))
        ranked_results = self.ranker.rank_places(
            city=city,
            interests=interests,
            budget_level=budget_level,
            traveller_type=traveller_type,
            mobility_needs=mobility_needs
        )

        if not ranked_results:
            return {
                "success": False,
                "message": f"No attractions found for {city}.",
                "city": city,
                "days": []
            }

        # Select candidate places (up to 3 places per day to ensure comfortable pacing)
        total_slots_needed = duration_days * 3
        candidate_pool = [r["place"] for r in ranked_results]
        
        # Spatial Clustering into Days:
        # Group places by proximity or logical sequence (Morning, Afternoon, Evening)
        days_plan = []
        assigned_place_ids = set()

        # Slot times definition
        slot_definitions = [
            {"slot": "Morning", "default_start": "09:00", "end": "12:30", "ideal_types": ["Heritage", "Spiritual", "Nature"]},
            {"slot": "Afternoon", "default_start": "13:30", "end": "16:30", "ideal_types": ["Heritage", "Culture", "Craft"]},
            {"slot": "Evening", "default_start": "17:30", "end": "20:30", "ideal_types": ["Spiritual", "Food", "Culture", "Nature"]}
        ]

        total_itinerary_ticket_cost = 0.0

        for day_num in range(1, duration_days + 1):
            day_items = []
            current_lat, current_lon = None, None

            for slot_info in slot_definitions:
                best_place = None
                best_match_score = -999.0

                for candidate in candidate_pool:
                    if candidate["id"] in assigned_place_ids:
                        continue

                    score = 0.0
                    # Slot affinity
                    cat = candidate.get("category", "")
                    if cat in slot_info["ideal_types"]:
                        score += 3.0

                    # Evening lighting or aarti check
                    best_time_str = candidate.get("best_time_to_visit", "").lower()
                    if slot_info["slot"] == "Evening" and ("evening" in best_time_str or "sunset" in best_time_str or "aarti" in best_time_str):
                        score += 8.0
                    if slot_info["slot"] == "Morning" and ("morning" in best_time_str or "sunrise" in best_time_str):
                        score += 5.0

                    # Spatial proximity to previous place on same day
                    if current_lat is not None and current_lon is not None:
                        dist = haversine_distance_km(current_lat, current_lon, candidate["latitude"], candidate["longitude"])
                        # Penalize places farther than 10 km
                        score -= dist * 0.4

                    if score > best_match_score:
                        best_match_score = score
                        best_place = candidate

                if best_place:
                    assigned_place_ids.add(best_place["id"])
                    
                    # Transit from previous stop
                    transit_info = None
                    if current_lat is not None and current_lon is not None:
                        transit_info = estimate_transit_time_mins(
                            current_lat, current_lon,
                            best_place["latitude"], best_place["longitude"]
                        )

                    current_lat = best_place["latitude"]
                    current_lon = best_place["longitude"]

                    fee = best_place.get("fee_adult_inr", 0.0)
                    total_itinerary_ticket_cost += fee

                    # Find ranking rationale for this place
                    place_rank_meta = next((r for r in ranked_results if r["place"]["id"] == best_place["id"]), None)
                    reasons = place_rank_meta["match_reasons"] if place_rank_meta else []
                    warnings = place_rank_meta["constraint_warnings"] if place_rank_meta else []

                    is_hi = language.lower() == "hindi"
                    is_hing = language.lower() == "hinglish"

                    slot_label = slot_info["slot"]
                    if is_hi:
                        slot_label = "प्रातः काल" if slot_info["slot"] == "Morning" else ("दोपहर" if slot_info["slot"] == "Afternoon" else "संध्या / आरती")
                    elif is_hing:
                        slot_label = "Morning Slot" if slot_info["slot"] == "Morning" else ("Afternoon Slot" if slot_info["slot"] == "Afternoon" else "Evening Aarti / Sunset")

                    # Format why recommended
                    why_text = "; ".join(reasons) if reasons else f"Top-rated {best_place['category']} destination in {city}"
                    if is_hi and reasons:
                        why_text = f"आपकी चुनी गई रुचियों ({', '.join(interests or ['धरोहर'])}) के पूर्णतः अनुकूल"
                    elif is_hing and reasons:
                        why_text = f"Aapke selected interests ({', '.join(interests or ['Heritage'])}) ke hisaab se top match"

                    acc_badge = "Wheelchair Accessible" if best_place["wheelchair_accessible"] else "Step Access"
                    if is_hi:
                        acc_badge = "व्हीलचेयर सुगम (रैंप उपलब्ध)" if best_place["wheelchair_accessible"] else "सीढ़ियां (सावधानी रखें)"
                    elif is_hing:
                        acc_badge = "Wheelchair Accessible" if best_place["wheelchair_accessible"] else "Stairs Present"

                    day_items.append({
                        "slot": slot_label,
                        "slot_type": slot_info["slot"],
                        "time_window": f"{slot_info['default_start']} - {slot_info['end']}",
                        "attraction_id": best_place["id"],
                        "name": best_place["name"],
                        "category": best_place["category"],
                        "area": best_place.get("area", ""),
                        "duration_hours": best_place.get("indicative_duration_hours", 1.5),
                        "fee_inr": fee,
                        "highlights": best_place.get("highlights", []),
                        "why_recommended": why_text,
                        "accessibility_badge": acc_badge,
                        "walking_intensity": best_place.get("walking_intensity", "Medium"),
                        "transit_from_previous": transit_info,
                        "source": best_place.get("source_name", "UP Tourism"),
                        "source_url": best_place.get("source_url", ""),
                        "warnings": warnings,
                        "latitude": best_place["latitude"],
                        "longitude": best_place["longitude"]
                    })

        is_hi = language.lower() == "hindi"
        is_hing = language.lower() == "hinglish"
        day_title = f"Day {day_num}: {city} " + ("Cultural & Heritage Discovery" if day_num == 1 else "Spiritual & Local Vibe")
        if is_hi:
            day_title = f"दिवस {day_num}: {city} " + ("धरोहर एवं सांस्कृतिक दर्शन" if day_num == 1 else "आध्यात्मिक एवं स्थानीय अनुभव")
        elif is_hing:
            day_title = f"Day {day_num}: {city} " + ("Heritage & Food Walk" if day_num == 1 else "Spiritual & Ghat Experience")

        days_plan.append({
            "day_number": day_num,
            "theme": day_title,
            "schedule": day_items
        })

        # Estimate food & local travel cost benchmarks
        estimated_food_spend = duration_days * (350 if budget_level == "Budget" else (700 if budget_level == "Moderate" else 1500))
        estimated_local_transit = duration_days * (200 if budget_level == "Budget" else (500 if budget_level == "Moderate" else 1200))
        estimated_total_cost = total_itinerary_ticket_cost + estimated_food_spend + estimated_local_transit

        # Alternate suggestions pool (unused high-ranked places)
        alternates = []
        for r in ranked_results:
            p = r["place"]
            if p["id"] not in assigned_place_ids:
                alternates.append({
                    "id": p["id"],
                    "name": p["name"],
                    "category": p["category"],
                    "fee_inr": p.get("fee_adult_inr", 0.0),
                    "wheelchair_accessible": p.get("wheelchair_accessible", False),
                    "reason_to_swap": f"Great alternative if seeking more {p['category']} experiences or facing time constraints."
                })
                if len(alternates) >= 3:
                    break

        return {
            "success": True,
            "city": city,
            "duration_days": duration_days,
            "budget_tier": budget_level,
            "traveller_type": traveller_type,
            "mobility_needs": mobility_needs,
            "language": language,
            "budget_breakdown": {
                "monument_tickets_inr": total_itinerary_ticket_cost,
                "indicative_food_inr": estimated_food_spend,
                "indicative_transit_inr": estimated_local_transit,
                "estimated_total_inr": estimated_total_cost,
                "note": "Ticket prices are official; meals and commute are indicative estimates."
            },
            "days": days_plan,
            "alternate_recommendations": alternates,
            "responsible_ai_notice": {
                "status": "Source-Grounded",
                "disclaimer": "This itinerary was algorithmically composed using verified UP Tourism data. Timings and transit intervals are indicative benchmarks to assist traveler planning."
            }
        }

if __name__ == "__main__":
    composer = ItineraryComposer()
    itinerary = composer.compose_itinerary(
        city="Varanasi",
        duration_days=2,
        interests=["Spiritual", "Culture", "Food"],
        budget_level="Moderate",
        traveller_type="Family"
    )
    print("--- 2-DAY VARANASI ITINERARY ---")
    print(f"Total Estimated Budget: INR {itinerary['budget_breakdown']['estimated_total_inr']}")
    for day in itinerary["days"]:
        print(f"\n{day['theme']}:")
        for item in day["schedule"]:
            transit = f" (Transit: {item['transit_from_previous']['duration_mins']} mins)" if item["transit_from_previous"] else ""
            print(f"  [{item['slot']} {item['time_window']}] {item['name']} - Fee: INR {item['fee_inr']}{transit}")
            print(f"     Why: {item['why_recommended']}")
