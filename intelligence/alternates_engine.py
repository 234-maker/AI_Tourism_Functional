"""
Constraint-Driven Dynamic Alternate Recommendation Engine.
Layer 3: Intelligence Layer
"""
import os
import sys
from typing import List, Dict, Any, Optional

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from intelligence.ranking import PlaceRanker

class AlternatesEngine:
    def __init__(self):
        self.ranker = PlaceRanker()

    def get_alternatives(
        self,
        current_place_id: str,
        constraint_type: str,     # 'MOBILITY_RESTRICTION', 'DAY_CLOSURE', 'BUDGET_CUT', 'TIME_SHORTAGE'
        closed_day: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Finds context-aware replacements when travel constraints change.
        """
        # Find current place
        current_place = next((a for a in self.ranker.attractions if a["id"] == current_place_id), None)
        if not current_place:
            return {"success": False, "error": f"Place ID {current_place_id} not found."}

        city = current_place["city"]
        category = current_place["category"]
        candidates = [a for a in self.ranker.attractions if a["city"] == city and a["id"] != current_place_id]

        matched_alternates = []

        for p in candidates:
            score = 10.0
            reasons = []

            # Same category bonus
            if p["category"] == category:
                score += 5.0
                reasons.append(f"Shares the same '{category}' theme as {current_place['name']}")

            # Constraint checks
            if constraint_type == "MOBILITY_RESTRICTION":
                if p["wheelchair_accessible"] and p["walking_intensity"] == "Low":
                    score += 8.0
                    reasons.append("100% barrier-free with flat paved pathways and minimal stairs")
                elif p["walking_intensity"] == "High":
                    continue  # exclude high exertion places

            elif constraint_type == "DAY_CLOSURE":
                if closed_day and closed_day in p.get("closed_days", []):
                    continue  # also closed on this day!
                score += 6.0
                reasons.append(f"Confirmed OPEN on {closed_day or 'selected day'}")

            elif constraint_type == "BUDGET_CUT":
                if p.get("fee_adult_inr", 0) == 0:
                    score += 9.0
                    reasons.append("Free public entry — zero ticket cost")
                elif p.get("fee_adult_inr", 0) < current_place.get("fee_adult_inr", 0):
                    score += 5.0
                    reasons.append(f"Cheaper entry fee (INR {p['fee_adult_inr']} vs INR {current_place['fee_adult_inr']})")

            elif constraint_type == "TIME_SHORTAGE":
                if p.get("indicative_duration_hours", 2.0) <= 1.5:
                    score += 7.0
                    reasons.append(f"Quick visit ({p['indicative_duration_hours']}h vs {current_place['indicative_duration_hours']}h)")

            matched_alternates.append({
                "id": p["id"],
                "name": p["name"],
                "category": p["category"],
                "fee_inr": p.get("fee_adult_inr", 0.0),
                "duration_hours": p.get("indicative_duration_hours", 1.5),
                "wheelchair_accessible": p.get("wheelchair_accessible", False),
                "walking_intensity": p.get("walking_intensity", "Medium"),
                "score": score,
                "reasons": reasons,
                "source": p.get("source_name", "UP Tourism")
            })

        matched_alternates.sort(key=lambda x: x["score"], reverse=True)

        return {
            "success": True,
            "original_place": {
                "id": current_place["id"],
                "name": current_place["name"],
                "category": current_place["category"],
                "fee_inr": current_place["fee_adult_inr"]
            },
            "constraint_triggered": constraint_type,
            "recommended_alternatives": matched_alternates[:3]
        }

if __name__ == "__main__":
    engine = AlternatesEngine()
    # Test Taj Mahal Friday closure
    res = engine.get_alternatives("AGR-001", "DAY_CLOSURE", closed_day="Friday")
    print("\n--- ALTERNATIVES FOR TAJ MAHAL ON FRIDAY ---")
    for alt in res["recommended_alternatives"]:
        print(f"-> {alt['name']} (Fee: INR {alt['fee_inr']}) | {'; '.join(alt['reasons'])}")

    # Test Bara Imambara Mobility limitation
    res2 = engine.get_alternatives("LKO-001", "MOBILITY_RESTRICTION")
    print("\n--- ALTERNATIVES FOR BARA IMAMBARA (MOBILITY RESTRICTION) ---")
    for alt in res2["recommended_alternatives"]:
        print(f"-> {alt['name']} ({alt['walking_intensity']} walking) | {'; '.join(alt['reasons'])}")
