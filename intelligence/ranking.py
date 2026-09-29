"""
Interest-Based Place Ranking and Constraint Filtering Engine.
Layer 3: Intelligence Layer
"""
import os
import json
from typing import List, Dict, Any

class PlaceRanker:
    def __init__(self, attractions_path: str = None):
        if attractions_path is None:
            attractions_path = os.path.join("data", "prepared", "prepared_attractions.json")
        with open(attractions_path, "r", encoding="utf-8") as f:
            self.attractions: List[Dict[str, Any]] = json.load(f)

    def rank_places(
        self,
        city: str,
        interests: List[str],
        budget_level: str = "Moderate",       # 'Budget', 'Moderate', 'Luxury'
        traveller_type: str = "Family",       # 'Solo', 'Family', 'Senior Citizens', 'Friends'
        mobility_needs: str = "Standard"      # 'Standard', 'Wheelchair', 'Low Walking'
    ) -> List[Dict[str, Any]]:
        """
        Rank attractions in a city based on interest alignment and constraint suitability.
        """
        # 1. Filter by city
        city_candidates = [
            a for a in self.attractions 
            if a["city"].strip().lower() == city.strip().lower()
        ]

        if not city_candidates:
            # Fallback for combined regional names like Mathura-Vrindavan
            if "mathura" in city.lower() or "vrindavan" in city.lower():
                city_candidates = [
                    a for a in self.attractions 
                    if a["city"].strip().lower() in ["mathura", "vrindavan"]
                ]

        scored_places = []
        interests_lower = [i.strip().lower() for i in interests] if interests else ["heritage", "culture"]

        for place in city_candidates:
            score = 10.0  # Base score
            match_reasons = []
            constraint_warnings = []

            # A. Interest Alignment
            place_interests = [pi.lower() for pi in place.get("interests", [])]
            place_cat = place.get("category", "").lower()
            
            overlap_count = 0
            for user_interest in interests_lower:
                if user_interest in place_interests or user_interest == place_cat:
                    overlap_count += 1
                    match_reasons.append(f"Matches your interest in '{user_interest.title()}'")
            
            score += overlap_count * 5.0

            # B. Mobility & Senior Citizen Constraints
            if mobility_needs == "Wheelchair" or traveller_type == "Senior Citizens":
                if place["wheelchair_accessible"]:
                    score += 4.0
                    match_reasons.append("Wheelchair & barrier-free accessibility confirmed")
                else:
                    score -= 8.0
                    constraint_warnings.append("Not fully wheelchair accessible (contains steps or uneven stone paths)")

                if place["senior_friendly"]:
                    score += 3.0
                elif place["walking_intensity"] == "High":
                    score -= 5.0
                    constraint_warnings.append("High walking/stair climbing intensity")

            # C. Family Friendly Constraint
            if traveller_type == "Family":
                if place["family_friendly"]:
                    score += 3.0
                else:
                    score -= 4.0
                    constraint_warnings.append("May be challenging with toddlers or large family groups")

            # D. Budget Constraint
            adult_fee = place.get("fee_adult_inr", 0.0)
            if budget_level == "Budget":
                if adult_fee == 0:
                    score += 4.0
                    match_reasons.append("Free entry — budget-friendly")
                elif adult_fee > 100:
                    score -= 3.0
                    constraint_warnings.append(f"Entry fee INR {adult_fee} may affect strict budgets")

            scored_places.append({
                "place": place,
                "score": round(score, 2),
                "match_reasons": match_reasons,
                "constraint_warnings": constraint_warnings
            })

        # Sort descending by score
        scored_places.sort(key=lambda x: x["score"], reverse=True)
        return scored_places

if __name__ == "__main__":
    ranker = PlaceRanker()
    ranked = ranker.rank_places(
        city="Lucknow",
        interests=["Food", "Heritage"],
        traveller_type="Senior Citizens",
        mobility_needs="Low Walking"
    )
    print("--- RANKED PLACES (Lucknow, Senior Citizens, Food & Heritage) ---")
    for r in ranked:
        p = r["place"]
        print(f"[{r['score']}] {p['name']} ({p['category']}) - Duration: {p['indicative_duration_hours']}h")
        if r["match_reasons"]:
            print(f"    Pros: {', '.join(r['match_reasons'])}")
        if r["constraint_warnings"]:
            print(f"    Caveat: {', '.join(r['constraint_warnings'])}")
