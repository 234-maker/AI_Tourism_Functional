"""
Geographic Distance and Transit Time Estimator.
Layer 3: Intelligence Layer
"""
import math
from typing import Tuple, Dict, Any

def haversine_distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the great circle distance in kilometers between two points."""
    r = 6371.0 # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2.0) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2.0) ** 2)
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return round(r * c, 2)

def estimate_transit_time_mins(lat1: float, lon1: float, lat2: float, lon2: float) -> Dict[str, Any]:
    """
    Estimates road travel transit duration with traffic buffer for Indian urban tourist circuits.
    Assumes average 18 km/h city auto/cab speed + 10 minutes parking/drop-off buffer.
    """
    dist_km = haversine_distance_km(lat1, lon1, lat2, lon2)
    
    if dist_km < 0.3:
        # Walking distance
        walk_mins = int((dist_km / 4.0) * 60) + 2
        return {
            "distance_km": dist_km,
            "mode": "Short Walk / E-rickshaw",
            "duration_mins": max(5, walk_mins)
        }
    
    # Road vehicle speed
    speed_kmh = 18.0
    travel_mins = int((dist_km / speed_kmh) * 60) + 10 # buffer
    
    return {
        "distance_km": dist_km,
        "mode": "Cab / Auto-rickshaw",
        "duration_mins": travel_mins
    }

if __name__ == "__main__":
    # Test distance between Bara Imambara and Chota Imambara in Lucknow
    res = estimate_transit_time_mins(26.8690, 80.9129, 26.8737, 80.9043)
    print("Bara Imambara -> Chota Imambara Transit:", res)
    # Test distance between Taj Mahal and Agra Fort
    res2 = estimate_transit_time_mins(27.1751, 78.0421, 27.1795, 78.0211)
    print("Taj Mahal -> Agra Fort Transit:", res2)
