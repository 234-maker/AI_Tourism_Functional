# Metadata Dictionary: Uttar Pradesh Tourism Dataset
**Project:** AI-Based Tourism Recommendation and Itinerary Planner  
**Layer:** Layer 1 — Data Layer  
**Coverage:** 6 Curated Destination Hubs in Uttar Pradesh (Lucknow, Varanasi, Agra, Ayodhya, Prayagraj, Mathura–Vrindavan)  
**Total Records:** 30 Curated Attractions with full provenance & verified public citations.

---

## 1. Schema & Field Definitions

| Field Name | Data Type | Constraint | Description | Allowed / Expected Values | Provenance / Source | Indicative or Factual |
|---|---|---|---|---|---|---|
| `id` | String | PK, Unique | Unique alphanumeric identifier for attraction | Format: `[LKO\|VNS\|AGR\|AYD\|PRY\|MTH]-[0-9]{3}` (e.g., `LKO-001`) | Internal Index Scheme | Factual |
| `name` | String | Not Null | Official name of the attraction / monument | String (e.g., "Bara Imambara & Bhulbhulaiya") | UP Tourism / ASI | Factual |
| `city` | String | Not Null | Indian city within Uttar Pradesh | `Lucknow`, `Varanasi`, `Agra`, `Ayodhya`, `Prayagraj`, `Mathura`, `Vrindavan` | State Administrative Registry | Factual |
| `state` | String | Default 'Uttar Pradesh' | State name | `Uttar Pradesh` | Official Registry | Factual |
| `category` | String | Not Null | Controlled tourism primary category | `Heritage`, `Spiritual`, `Culture`, `Nature`, `Food`, `Craft` | Standard Taxonomy | Factual |
| `interests` | List[String] | Min 1 item | Tags representing tourist interest affinities | `Heritage`, `Architecture`, `Photography`, `Spiritual`, `History`, `Culture`, `Food`, `Nature`, `Craft`, `Shopping` | Curated Taxonomy | Factual |
| `description` | Text | Not Null | Grounded factual description of history, architecture, and significance | 50–120 words summary without promotional fluff | UP Tourism Portal / ASI Plaque Archives | Factual |
| `highlights` | List[String] | Min 2 items | Key features or must-see spots within the attraction | 3-4 bullet strings | UP Tourism Guides | Factual |
| `open_time` | String | Format HH:MM | Official gate opening time (24-hr) | E.g. `06:00`, `09:00` | Official Tourism Notices | Factual |
| `close_time` | String | Format HH:MM | Official gate closing time (24-hr) | E.g. `18:00`, `22:00` | Official Tourism Notices | Factual |
| `open_time_mins` | Integer | 0–1439 | Minutes from midnight for opening (for algorithm optimization) | E.g., `360` for 06:00 | Computed by pipeline | Factual |
| `close_time_mins` | Integer | 0–1439 | Minutes from midnight for closing (for algorithm optimization) | E.g., `1080` for 18:00 | Computed by pipeline | Factual |
| `closed_days` | List[String] | Enum | Days monument is closed to general public | `Monday`, `Friday`, `Sunday`, or empty list | Official Gazetted Notice | Factual |
| `best_time_to_visit` | String | String | Ideal time of day for lighting, Aarti, or lower crowds | E.g. `Sunrise (06:00 - 08:30)`, `Evening Aarti (18:00)` | Curated Tourist Guidance | Indicative |
| `fee_adult_inr` | Float | >= 0 | General adult entry ticket fee for Indian citizens | In INR (e.g. `50.0`, `0.0` for free shrines) | ASI / UP Tourism Official Rates | Factual |
| `fee_child_inr` | Float | >= 0 | Child ticket fee in INR | In INR (e.g. `0.0`, `25.0`) | Official Rates | Factual |
| `fee_foreigner_inr` | Float | >= 0 | Standard foreign tourist ticket fee in INR | In INR (e.g. `1100.0`, `500.0`, `0.0`) | Official Rates | Factual |
| `indicative_duration_hours` | Float | 0.5 – 5.0 | Recommended duration to explore comfortably without rushing | Float in hours (e.g., `2.5`, `1.5`, `3.0`) | Empirical Travel Guide Benchmarks | Indicative |
| `wheelchair_accessible` | Boolean | True / False | Physical barrier-free access availability (ramps, elevators, flat plazas) | `true`, `false` | On-site accessibility audit | Factual |
| `senior_friendly` | Boolean | True / False | Low-step access, seating facilities, battery carts | `true`, `false` | Curated Accessibility Metric | Factual |
| `walking_intensity` | String | Controlled Enum | Walking and stair physical exertion level | `Low`, `Medium`, `High` | Standardized Mobility Scale | Indicative |
| `accessibility_notes` | Text | Optional | Specific accessibility guidance (e.g., steep stairs in labyrinth) | Explanatory text | On-site audit notes | Factual |
| `family_friendly` | Boolean | Default True | Suitability for multi-generation family travel | `true`, `false` | Curated Metric | Factual |
| `family_notes` | Text | Optional | Guidance for traveling with toddlers or elders | Explanatory text | Curated Metric | Indicative |
| `area` | String | Not Null | Local locality or neighborhood within the city | E.g. `Husainabad`, `Tajganj`, `Godowlia` | City Municipal Wards | Factual |
| `latitude` | Float | 23.0 – 31.0 | Geographic WGS84 Latitude coordinate | Decimal degrees (e.g. `26.8690`) | OpenStreetMap / Survey of India | Factual |
| `longitude` | Float | 76.5 – 85.5 | Geographic WGS84 Longitude coordinate | Decimal degrees (e.g. `80.9129`) | OpenStreetMap / Survey of India | Factual |
| `nearby_transit` | String | Optional | Nearest Metro station, Railway station, or Ghat jetty | E.g. `Taj East Gate Metro Station` | Public Transit Maps | Factual |
| `nearby_facilities` | List[String] | Min 1 item | On-site tourist conveniences | `Shoe counter`, `Restrooms`, `Drinking water`, `Lockers`, `Guides`, `Parking` | Verified Field Audit | Factual |
| `transport_hints` | Text | Not Null | First-mile / last-mile commute tips (e-rickshaw, shuttle, walking routes) | Clear commuter guidance | Curated Local Travel Hints | Indicative |
| `source_name` | String | Not Null | Primary governing body or verified public authority | `Archaeological Survey of India`, `UP Tourism`, `Temple Trusts` | Official Source | Factual |
| `source_url` | String | Valid URL | Public URL for official verification | HTTPS link | Official Websites | Factual |
| `is_mock` | Boolean | Default False | Flags synthetic or simulated data | `false` for actual places; `true` for future placeholder feeds | Responsible AI Policy | Factual |
| `faqs` | List[Dict] | Min 1 FAQ | Common tourist questions and grounded answers | Pairs of `{question, answer}` | Real tourist queries | Factual |
| `search_blob` | Text | Precomputed | Concatenated semantic tokens for vector search & BM25 indexing | Text | Computed by pipeline | Factual |

---

## 2. Indicative vs. Factual Data Boundary (Responsible AI Note)
As mandated by the Project Synopsis and Problem Statement:
- **Factual Attributes:** Monument names, locations, GPS coordinates, verified opening/closing hours, official ticket pricing, closed days, and public source URLs.
- **Indicative Attributes:** Recommended visit duration (`indicative_duration_hours`), optimal time slot (`best_time_to_visit`), and walking intensity classification. These are heuristics provided to optimize itinerary planning and are clearly marked as recommendations rather than statutory rules.
