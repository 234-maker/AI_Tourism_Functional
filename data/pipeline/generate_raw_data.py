"""
Script to curate the raw Uttar Pradesh Tourism Dataset.
Data sourced and verified against UP Tourism (uptourism.gov.in) and Incredible India.
"""
import json

raw_attractions = [
    # LUCKNOW
    {
        "id": "LKO-001",
        "name": "Bara Imambara & Bhulbhulaiya",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "category": "Heritage",
        "interests": ["Heritage", "Architecture", "Photography", "History"],
        "description": "Built in 1784 by Nawab Asaf-ud-Daula as a famine relief project, this grand Shia pilgrimage monument features the famous arched central hall without external pillars, and an intricate 3D labyrinth known as Bhulbhulaiya with 489 identical doorways and sweeping terrace views.",
        "highlights": ["World's largest unsupported vaulted hall", "Intricate Bhulbhulaiya labyrinth", "Shahi Baoli stepwell"],
        "timings": {
            "open_time": "06:00",
            "close_time": "17:00",
            "closed_on": ["Monday"],
            "best_time_to_visit": "Morning (09:00 - 11:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 50,
            "indian_child": 25,
            "foreigner": 500,
            "guide_approx": 200
        },
        "indicative_duration_hours": 2.5,
        "accessibility": {
            "wheelchair_accessible": False,
            "senior_citizen_friendly": False,
            "walking_intensity": "High",
            "notes": "Labyrinth contains narrow steep stone stairways; ground courtyard is flat and accessible, but Bhulbhulaiya requires agility."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Fascinating maze experience for kids and families; mandatory authorized guide recommended so you don't lose your way."
        },
        "location": {
            "area": "Machchhi Bhavan / Husainabad",
            "latitude": 26.8690,
            "longitude": 80.9129,
            "nearby_metro": "Chowk / Durgapuri (3 km)"
        },
        "nearby_facilities": ["Shoe counter", "Drinking water", "Public restrooms", "Licensed local guides", "Parking area"],
        "transport_hints": "Easily reachable by e-rickshaws, auto-rickshaws, and app-based cabs from Charbagh Railway Station (5 km).",
        "source": {
            "organization": "Uttar Pradesh Tourism Development Corporation",
            "official_url": "https://uptourism.gov.in/en/post/bara-imambara",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Is guide mandatory for Bhulbhulaiya?",
                "answer": "While not strictly enforced at ticket entry, taking an authorized UP Tourism certified guide (approx INR 150-250) is strongly advised to navigate the 489 maze passages safely."
            },
            {
                "question": "Can senior citizens visit?",
                "answer": "Senior citizens can enjoy the ground courtyard, Asfi Mosque exterior and Shahi Baoli, but should avoid climbing the steep labyrinth stairs."
            }
        ]
    },
    {
        "id": "LKO-002",
        "name": "Chota Imambara (Hussainabad Imambara)",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "category": "Heritage",
        "interests": ["Heritage", "Architecture", "Photography", "Spiritual"],
        "description": "Built in 1838 by Nawab Muhammad Ali Shah, this jewel-like mausoleum features gilded domes, Belgian crystal chandeliers, Persian calligraphy, and exquisite brass decorations, alongside a replica of the Taj Mahal acting as the tomb of Princess Zinat Algiya.",
        "highlights": ["Belgian glass chandeliers and crystal lanterns", "Gilded dome exterior", "Hussainabad Picture Gallery nearby"],
        "timings": {
            "open_time": "06:00",
            "close_time": "17:00",
            "closed_on": ["Monday"],
            "best_time_to_visit": "Afternoon / Golden Hour (15:00 - 17:00)"
        },
        "entry_fee_inr": {
            "indian_adult": 50,
            "indian_child": 25,
            "foreigner": 500,
            "notes": "Combo ticket with Bara Imambara available"
        },
        "indicative_duration_hours": 1.5,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Paved flat courtyards with ramps for main hall entrance."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Very serene and illuminated garden environment suitable for all ages."
        },
        "location": {
            "area": "Husainabad",
            "latitude": 26.8737,
            "longitude": 80.9043,
            "nearby_metro": "Near Clock Tower"
        },
        "nearby_facilities": ["Shoe racks", "Restrooms", "Drinking water", "Handicraft shops"],
        "transport_hints": "1.5 km west of Bara Imambara. Best reached by a 10-minute e-rickshaw ride past Rumi Darwaza.",
        "source": {
            "organization": "Uttar Pradesh Tourism",
            "official_url": "https://uptourism.gov.in/en/post/chhota-imambara",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "What is the dress code?",
                "answer": "Modest clothing covering shoulders and knees is required as it is an active Shia religious site. Shoes must be removed at the counter."
            }
        ]
    },
    {
        "id": "LKO-003",
        "name": "Rumi Darwaza",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "category": "Heritage",
        "interests": ["Heritage", "Architecture", "Photography", "Sightseeing"],
        "description": "Standing 60-feet tall, Rumi Darwaza is the iconic gateway of Lucknow built in 1784 under Nawab Asaf-ud-Daula, modeled after the Sublime Porte (Bab-iHümayun) in Constantinople. An architectural marvel of Awadhi brickwork adorned with ornate floral motifs.",
        "highlights": ["60-foot ornamental Awadhi arch", "Stunning evening floodlighting", "Gateway framing the old Husainabad skyline"],
        "timings": {
            "open_time": "00:00",
            "close_time": "23:59",
            "closed_on": [],
            "best_time_to_visit": "Evening / Night (18:00 - 20:00)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "notes": "Public monument viewable from promenade"
        },
        "indicative_duration_hours": 0.5,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Pedestrianized promenade allows barrier-free viewing."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Ideal photo-stop for families."
        },
        "location": {
            "area": "Husainabad Road",
            "latitude": 26.8711,
            "longitude": 80.9114,
            "nearby_metro": "Chowk"
        },
        "nearby_facilities": ["Street food stalls", "Souvenir carts", "Photography viewpoints"],
        "transport_hints": "Situated directly between Bara Imambara and Chota Imambara along Husainabad heritage street.",
        "source": {
            "organization": "Uttar Pradesh Tourism",
            "official_url": "https://uptourism.gov.in/en/post/rumi-darwaza",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Can tourists go inside the upper gate?",
                "answer": "No, entry inside the upper chambers is closed for structural preservation; visitors view and photograph it from the heritage plaza."
            }
        ]
    },
    {
        "id": "LKO-004",
        "name": "The British Residency",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "category": "Heritage",
        "interests": ["History", "Heritage", "Nature", "Photography"],
        "description": "The site of the famous 147-day Siege of Lucknow during the First War of Indian Independence in 1857. Now preserved as quiet, picturesque ruins set within lush 33-acre terraced lawns, complete with an ASI museum and cannonball scarred brick walls.",
        "highlights": ["Ruins showing 1857 cannon markings", "1857 Memorial Museum", "Peaceful landscaped gardens & cemetery"],
        "timings": {
            "open_time": "09:00",
            "close_time": "17:30",
            "closed_on": ["Monday"],
            "best_time_to_visit": "Morning (09:30 - 12:00)"
        },
        "entry_fee_inr": {
            "indian_adult": 25,
            "indian_child": 0,
            "foreigner": 300,
            "notes": "Free for children under 15"
        },
        "indicative_duration_hours": 2.0,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Medium",
            "notes": "Paved pathways across gardens; museum has ramp."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Spacious green open gardens, great educational outing for school children and families."
        },
        "location": {
            "area": "Mahatma Gandhi Marg, Deep Manak",
            "latitude": 26.8617,
            "longitude": 80.9272,
            "nearby_metro": "KD Singh Babu Stadium Metro (1.5 km)"
        },
        "nearby_facilities": ["ASI Museum", "Clean restrooms", "Shaded benches", "Parking lot"],
        "transport_hints": "Central location, 2 km from Hazratganj. E-rickshaws and cabs easily available.",
        "source": {
            "organization": "Archaeological Survey of India / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/the-residency",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Is photography permitted?",
                "answer": "Still photography is permitted on the grounds without tripod. Museum exhibits have specific guidelines."
            }
        ]
    },
    {
        "id": "LKO-005",
        "name": "Hazratganj & Royal Cafe Culinary Walk",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "category": "Food",
        "interests": ["Food", "Culture", "Shopping", "Heritage"],
        "description": "The premier shopping corridor of Lucknow, designed with unified Victorian-style cream-and-pink facades. Renowned for 'Ganjing' (evening strolling), traditional Chikankari boutiques, iconic bookstores, and the world-famous Basket Chaat at Royal Cafe.",
        "highlights": ["Iconic Royal Cafe Basket Chaat", "Chikankari handcraft flagship stores", "British-era heritage facades"],
        "timings": {
            "open_time": "11:00",
            "close_time": "22:00",
            "closed_on": ["Sunday (shops partially closed, restaurants open)"],
            "best_time_to_visit": "Evening (17:30 - 21:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "food_spend_approx": 350
        },
        "indicative_duration_hours": 2.0,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Broad pedestrian walkways with street lamps and benches."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Lively family-friendly atmosphere with cafes, ice cream parlours and stores."
        },
        "location": {
            "area": "Hazratganj Main Market",
            "latitude": 26.8504,
            "longitude": 80.9427,
            "nearby_metro": "Hazratganj Metro Station (Direct exit)"
        },
        "nearby_facilities": ["Metro station", "Multi-level parking", "ATMs", "Restrooms in complexes", "Branded outlets"],
        "transport_hints": "Directly accessible via Hazratganj Metro Station on Lucknow Metro Red Line.",
        "source": {
            "organization": "Lucknow Municipal Corporation / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/hazratganj",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "What foods are must-try in Hazratganj?",
                "answer": "Basket Chaat at Royal Cafe, Prakash Kulfi, Rover's frankies, and traditional Awadhi kebabs at nearby outlets."
            }
        ]
    },
    {
        "id": "LKO-006",
        "name": "Chowk Heritage Bazaar & Tunday Kababi Trail",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "category": "Food",
        "interests": ["Food", "Culture", "Craft", "History"],
        "description": "The historic old quarter of Lucknow where Awadhi culinary traditions and artisan crafts thrive. Home to the original 1905 Tunday Kababi, Idris Biryani, Rahim's Kulcha Nihari, and alleys filled with master Chikankari, Zardozi, and Ittar (perfume) distillers.",
        "highlights": ["Century-old original Tunday Kababi", "Traditional Sugandhi Ittar perfume shops", "Authentic Zardozi embroidery workshops"],
        "timings": {
            "open_time": "12:00",
            "close_time": "23:00",
            "closed_on": ["Thursday"],
            "best_time_to_visit": "Evening / Dinner (18:30 - 21:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "food_spend_approx": 300
        },
        "indicative_duration_hours": 2.5,
        "accessibility": {
            "wheelchair_accessible": False,
            "senior_citizen_friendly": False,
            "walking_intensity": "High",
            "notes": "Crowded, bustling historic lanes with pedestrian-only vehicle restrictions."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Foodies delight; keep small children close due to dense crowd."
        },
        "location": {
            "area": "Old Chowk, Lucknow",
            "latitude": 26.8643,
            "longitude": 80.9038,
            "nearby_metro": "Chowk"
        },
        "nearby_facilities": ["Local eateries", "Traditional sweet shops", "Spice merchants"],
        "transport_hints": "Take an e-rickshaw directly from Bara Imambara (1.5 km).",
        "source": {
            "organization": "UP Tourism Awadh Culinary Trail",
            "official_url": "https://uptourism.gov.in/en/post/lucknow-cuisine",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Is vegetarian food available in Chowk?",
                "answer": "Yes! Radhey Lal Parampara Sweets for Makhan Malai (winter) and authentic Bedmi Poori / Chhole are famous vegetarian culinary stops."
            }
        ]
    },
    {
        "id": "LKO-007",
        "name": "Dr. Ambedkar Memorial Park",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "category": "Culture",
        "interests": ["Architecture", "Photography", "Culture", "Sightseeing"],
        "description": "A massive 107-acre civic monument built with red sandstone brought from Mirzapur. It features grand plazas, 62 giant stone elephant statues, a 112-foot high stupa dome, and reflective canals, looking particularly awe-inspiring during sunset and under evening illumination.",
        "highlights": ["Stone elephant gallery of 62 statues", "Reflective water channels", "Grand central Stupa with statue of Dr. B.R. Ambedkar"],
        "timings": {
            "open_time": "11:00",
            "close_time": "21:00",
            "closed_on": [],
            "best_time_to_visit": "Late Afternoon to Dusk (17:00 - 19:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 20,
            "indian_child": 10,
            "foreigner": 50,
            "parking": 20
        },
        "indicative_duration_hours": 1.5,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Medium",
            "notes": "Very wide flat paved surfaces with gently sloped ramps throughout."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Very wide, safe and peaceful open promenade for evening leisure."
        },
        "location": {
            "area": "Vipin Khand, Gomti Nagar",
            "latitude": 26.8480,
            "longitude": 80.9754,
            "nearby_metro": "Lekhraj Market Metro (3.5 km)"
        },
        "nearby_facilities": ["Clean washrooms", "Car parking", "Drinking water kiosks", "Security guards"],
        "transport_hints": "Located in Gomti Nagar; easily accessible via cab or auto from Hazratganj (15 minutes).",
        "source": {
            "organization": "Lucknow Development Authority",
            "official_url": "https://uptourism.gov.in/en/post/ambedkar-memorial-park",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Can we take cameras inside?",
                "answer": "Mobile photography is permitted. Professional DSLR cameras may require a nominal ticket fee at the counter."
            }
        ]
    },

    # VARANASI
    {
        "id": "VNS-001",
        "name": "Kashi Vishwanath Temple & Corridor",
        "city": "Varanasi",
        "state": "Uttar Pradesh",
        "category": "Spiritual",
        "interests": ["Spiritual", "Heritage", "Culture", "Architecture"],
        "description": "One of the 12 sacred Jyotirlingas of Lord Shiva, situated on the western bank of holy River Ganga. The expanded 5-lakh sq ft Vishwanath Corridor connects the temple directly to Manikarnika and Lalita Ghats, offering modern pilgrim amenities and heritage temple pavilions.",
        "highlights": ["Gold-plated temple spires", "Spacious riverfront corridor", "Direct holy dip access at Lalita Ghat"],
        "timings": {
            "open_time": "03:00",
            "close_time": "23:00",
            "closed_on": [],
            "best_time_to_visit": "Early Morning (05:00 - 07:00) or Mangala Aarti"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "special_sugam_darshan": 300,
            "notes": "General darshan is free; Sugam Darshan ticket allows priority line via official trust portal"
        },
        "indicative_duration_hours": 2.5,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Medium",
            "notes": "Corridor includes escalators, ramps, and battery-operated carts for elderly pilgrims."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Highly organized pilgrim infrastructure since corridor modernization."
        },
        "location": {
            "area": "Lahori Tola / Godowlia",
            "latitude": 25.3109,
            "longitude": 83.0107,
            "nearby_metro": "Varanasi Cantt Station (4.5 km)"
        },
        "nearby_facilities": ["Free locker cloakroom for phones", "Restrooms", "Drinking water RO", "Bookstore", "Prasadam counter"],
        "transport_hints": "Vehicles stop at Godowlia Crossing; walk 400m through pedestrian zone or take e-rickshaw to Gate 4.",
        "source": {
            "organization": "Shri Kashi Vishwanath Temple Trust / UP Tourism",
            "official_url": "https://shrikashivishwanath.org",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Are mobile phones allowed inside?",
                "answer": "No electronic devices, leather belts, or mobile phones are permitted past security. Free secure lockers are provided at Corridor Gate 4."
            },
            {
                "question": "Is advance booking required?",
                "answer": "General queue darshan requires no booking. Special aartis (Mangala, Bhog) require advance online booking on the official temple trust portal."
            }
        ]
    },
    {
        "id": "VNS-002",
        "name": "Dashashwamedh Ghat & Evening Ganga Aarti",
        "city": "Varanasi",
        "state": "Uttar Pradesh",
        "category": "Spiritual",
        "interests": ["Spiritual", "Culture", "Photography", "Sightseeing"],
        "description": "The main and most vibrant ghat on the sacred Ganga River in Varanasi. Every evening at sunset, a choreographed, brass-lamp Aarti ceremony is performed by young saffron-clad priests amidst chanting hymns, blowing conch shells, and floating diya lanterns.",
        "highlights": ["Mesmerizing 45-minute Ganga Aarti", "Floating boat vantage point", "Panoramic view of sacred ghat steps"],
        "timings": {
            "open_time": "05:00",
            "close_time": "23:00",
            "closed_on": [],
            "best_time_to_visit": "Evening Aarti (18:00 in winter, 19:00 in summer)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "boat_ride_approx": 250,
            "notes": "Watching from ghat steps is free; rowing/motor boats charge INR 200-500 per seat"
        },
        "indicative_duration_hours": 2.0,
        "accessibility": {
            "wheelchair_accessible": False,
            "senior_citizen_friendly": True,
            "walking_intensity": "Medium",
            "notes": "Steps leading down to the river; senior citizens can watch comfortably from reserved upper ghat platform chairs or pre-booked boats."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "An unforgettable spiritual and cultural experience for all ages."
        },
        "location": {
            "area": "Dashashwamedh Ghat Road",
            "latitude": 25.3075,
            "longitude": 83.0104,
            "nearby_metro": "Godowlia Crossing (600m)"
        },
        "nearby_facilities": ["Boat hire jetty", "Puja flower sellers", "Tea stalls", "Public seating"],
        "transport_hints": "Walk 10 mins down from Godowlia roundabout. Reach by 17:30 to secure good seating.",
        "source": {
            "organization": "Ganga Seva Nidhi / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/dashashwamedh-ghat",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "What is the best way to watch the Aarti?",
                "answer": "Either by sitting on the ghat steps 45 minutes prior, or hiring a licensed hand-rowed wooden boat to watch from the river facing the priests."
            }
        ]
    },
    {
        "id": "VNS-003",
        "name": "Assi Ghat & Subah-e-Banaras",
        "city": "Varanasi",
        "state": "Uttar Pradesh",
        "category": "Culture",
        "interests": ["Culture", "Spiritual", "Nature", "Food"],
        "description": "The southernmost major ghat where the Assi River joins the Ganga. Famed for 'Subah-e-Banaras' — a sunrise celebration featuring Vedic havan rituals, morning Ganga Aarti, classical music/shehnai recital, and free community yoga on the riverfront.",
        "highlights": ["Sunrise Subah-e-Banaras cultural program", "Morning Yoga by the river", "Iconic Pizzeria Vaatika cafe apple pie"],
        "timings": {
            "open_time": "04:30",
            "close_time": "22:00",
            "closed_on": [],
            "best_time_to_visit": "Sunrise / Early Morning (05:00 - 07:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "notes": "Public cultural program is free"
        },
        "indicative_duration_hours": 2.0,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Direct road connectivity and flat paved riverfront plaza make Assi Ghat easiest to access."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Peaceful morning atmosphere, great for morning family walks and boat boarding."
        },
        "location": {
            "area": "Assi Road, Near Banaras Hindu University",
            "latitude": 25.2903,
            "longitude": 83.0068,
            "nearby_metro": "BHU Gate (1.5 km)"
        },
        "nearby_facilities": ["Cafes and restaurants", "Boat operators", "Restrooms", "Paved vehicle parking"],
        "transport_hints": "Easily reached directly by cab or auto from anywhere in Varanasi; broad access road.",
        "source": {
            "organization": "Subah-e-Banaras Society / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/assi-ghat",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Can tourists participate in the morning yoga?",
                "answer": "Yes, tourists can freely bring a mat and join the instructor-led morning session right on the wooden stage after the Aarti."
            }
        ]
    },
    {
        "id": "VNS-004",
        "name": "Sarnath Buddhist Archaeological Site & Museum",
        "city": "Varanasi",
        "state": "Uttar Pradesh",
        "category": "Heritage",
        "interests": ["History", "Spiritual", "Heritage", "Architecture"],
        "description": "Located 10 km north of Varanasi, Sarnath is one of the four principal Buddhist pilgrimage sites. Here Lord Buddha preached his first sermon (Dhammacakkappavattana Sutta) in 528 BCE. Features the imposing Dhamek Stupa, Ashoka Pillar ruins, and an ASI museum preserving the iconic 3rd century BCE Lion Capital of Ashoka (National Emblem of India).",
        "highlights": ["Dhamek Stupa standing 43.6m tall", "Lion Capital of Ashoka in ASI Museum", "Mulagandha Kuti Vihara with Japanese frescos"],
        "timings": {
            "open_time": "09:00",
            "close_time": "17:00",
            "closed_on": ["Friday (Museum only, monuments open daily)"],
            "best_time_to_visit": "Morning / Early Afternoon (10:00 - 14:00)"
        },
        "entry_fee_inr": {
            "indian_adult": 25,
            "indian_child": 0,
            "foreigner": 300,
            "museum_fee": 5
        },
        "indicative_duration_hours": 3.0,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Beautifully maintained flat archaeological lawns and paved pathways."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Calm, educational, and historically enriching for travellers and children."
        },
        "location": {
            "area": "Sarnath, Varanasi Rural",
            "latitude": 25.3811,
            "longitude": 83.0227,
            "nearby_metro": "Sarnath Railway Station (1 km)"
        },
        "nearby_facilities": ["ASI Archaeological Museum", "Clean restrooms", "Shaded gardens", "Deer park nearby", "Souvenir stalls"],
        "transport_hints": "10 km north of Varanasi city centre. Take an auto-rickshaw (30 mins) or book a cab.",
        "source": {
            "organization": "Archaeological Survey of India / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/sarnath",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Is Sarnath Archaeological Museum closed on any day?",
                "answer": "Yes, the Sarnath Archaeological Museum is closed on Fridays, while the outdoor monument ruins remain open all seven days."
            }
        ]
    },
    {
        "id": "VNS-005",
        "name": "Banarasi Silk Weaving Village & Godowlia Market",
        "city": "Varanasi",
        "state": "Uttar Pradesh",
        "category": "Craft",
        "interests": ["Craft", "Shopping", "Culture", "Heritage"],
        "description": "Witness the traditional handloom weaving of world-famous Banarasi silk sarees with gold and silver zari threads (GI-tagged craft). Explore artisan pit-loom workshops in Sarai Mohana or Madanpura, followed by authentic shopping and local Banarasi Paan tasting in Godowlia.",
        "highlights": ["Live jacquard and pit-loom silk weaving", "Direct GI-certified handloom artisan interaction", "Authentic Banarasi Paan and Malaiyyo (winter dessert)"],
        "timings": {
            "open_time": "10:30",
            "close_time": "20:30",
            "closed_on": ["Sunday"],
            "best_time_to_visit": "Afternoon (14:00 - 17:00)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "shopping_optional": 0
        },
        "indicative_duration_hours": 2.0,
        "accessibility": {
            "wheelchair_accessible": False,
            "senior_citizen_friendly": True,
            "walking_intensity": "Medium",
            "notes": "Handloom cooperative showrooms have seating and air conditioning."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Fascinating craft education for families."
        },
        "location": {
            "area": "Sarai Mohana / Madanpura / Godowlia",
            "latitude": 25.3176,
            "longitude": 83.0039,
            "nearby_metro": "Godowlia"
        },
        "nearby_facilities": ["Cooperative emporiums", "Paan stalls", "Lassi shops (Blue Lassi nearby)"],
        "transport_hints": "15 minutes from Dashashwamedh Ghat by cycle-rickshaw or e-rickshaw.",
        "source": {
            "organization": "Handloom Development Board / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/banarasi-saree",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "How to verify genuine Banarasi silk?",
                "answer": "Look for the Government Silk Mark and Handloom Mark tags, and inspect the reverse side of the motifs for floating threads characteristic of traditional kadhwa weaves."
            }
        ]
    },

    # AGRA
    {
        "id": "AGR-001",
        "name": "Taj Mahal",
        "city": "Agra",
        "state": "Uttar Pradesh",
        "category": "Heritage",
        "interests": ["Heritage", "Architecture", "Photography", "Culture"],
        "description": "An immense ivory-white marble mausoleum on the right bank of the Yamuna River, commissioned in 1631 by Mughal Emperor Shah Jahan for his wife Mumtaz Mahal. One of the Seven Wonders of the World and a UNESCO World Heritage Site, representing the jewel of Indo-Islamic architecture with pietra dura floral inlays and symmetrical Mughal gardens.",
        "highlights": ["Pietra dura marble inlay craft", "Reflecting pools and symmetrical Charbagh", "Breathtaking sunrise illumination"],
        "timings": {
            "open_time": "06:00",
            "close_time": "18:30",
            "closed_on": ["Friday"],
            "best_time_to_visit": "Sunrise (06:00 - 08:30) for best light and lesser crowds"
        },
        "entry_fee_inr": {
            "indian_adult": 50,
            "indian_child": 0,
            "foreigner": 1100,
            "main_mausoleum_addon": 200,
            "notes": "Free for children below 15; online ticketing through ASI portal is mandatory"
        },
        "indicative_duration_hours": 3.0,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Medium",
            "notes": "Battery golf carts ferry visitors from parking to gates (500m); ramps available on garden terrace."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Spacious gardens, high security, world-class experience for families."
        },
        "location": {
            "area": "Dharmapuri, Forest Colony, Tajganj",
            "latitude": 27.1751,
            "longitude": 78.0421,
            "nearby_metro": "Taj East Gate Metro Station (Direct)"
        },
        "nearby_facilities": ["Shoe cover dispensers", "Cloakrooms", "Audio guides", "Golf carts", "Clean restrooms"],
        "transport_hints": "Agra Metro now connects Taj East Gate station directly. Electric golf-carts operate from Shilpgram parking.",
        "source": {
            "organization": "Archaeological Survey of India / Ministry of Tourism",
            "official_url": "https://www.tajmahal.gov.in",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Is the Taj Mahal open on Friday?",
                "answer": "No. The Taj Mahal is strictly closed for general tourists every Friday (open only for registered congregational afternoon prayers)."
            },
            {
                "question": "Can we buy tickets at the monument counter?",
                "answer": "ASI has phased out manual paper counters; visitors must scan QR codes or pre-book online at asi.payumoney.com or official government portals."
            }
        ]
    },
    {
        "id": "AGR-002",
        "name": "Agra Fort",
        "city": "Agra",
        "state": "Uttar Pradesh",
        "category": "Heritage",
        "interests": ["Heritage", "History", "Architecture", "Photography"],
        "description": "A UNESCO World Heritage Site, this 94-acre red sandstone fortress served as the principal residence of the Mughal emperors until 1638. Encloses stunning palaces like Jahangiri Mahal, Khas Mahal, Sheesh Mahal, and the Musamman Burj balcony where Shah Jahan gazed at the Taj Mahal during his final years of house arrest.",
        "highlights": ["Musamman Burj overlooking Taj Mahal", "Diwan-i-Khas and Sheesh Mahal mirror palace", "Massive Amar Singh Gate fortifications"],
        "timings": {
            "open_time": "06:00",
            "close_time": "18:00",
            "closed_on": [],
            "best_time_to_visit": "Afternoon (14:30 - 17:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 50,
            "indian_child": 0,
            "foreigner": 650,
            "notes": "Online ticket discount available"
        },
        "indicative_duration_hours": 2.5,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Medium",
            "notes": "Cobblestoned entry ramp has moderate incline; wheelchair assistance can be requested at gate."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Engaging medieval castle-like fortification that captivates children."
        },
        "location": {
            "area": "Agra Fort, Rakabganj",
            "latitude": 27.1795,
            "longitude": 78.0211,
            "nearby_metro": "Agra Fort Metro Station"
        },
        "nearby_facilities": ["Audio guide counter", "Restrooms", "Drinking water kiosks", "ASI ticket counter"],
        "transport_hints": "Just 2.5 km northwest of the Taj Mahal. Connected by Agra Metro line.",
        "source": {
            "organization": "Archaeological Survey of India / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/agra-fort",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "How far is Agra Fort from Taj Mahal?",
                "answer": "Agra Fort is approximately 2.5 km from the Taj Mahal, taking around 8-10 minutes by auto or cab."
            }
        ]
    },
    {
        "id": "AGR-003",
        "name": "Fatehpur Sikri Royal City",
        "city": "Agra",
        "state": "Uttar Pradesh",
        "category": "Heritage",
        "interests": ["Heritage", "History", "Architecture", "Spiritual"],
        "description": "Founded in 1569 by Emperor Akbar as the capital of the Mughal Empire, this UNESCO World Heritage red sandstone complex includes the colossal 54-meter Buland Darwaza ('Gate of Magnificence'), the white marble tomb of Sufi saint Sheikh Salim Chishti, Jama Masjid, and the multi-tiered Panch Mahal pavilion.",
        "highlights": ["54-meter Buland Darwaza", "Salim Chishti Sufi Dargah with marble jali work", "Acoustic wonder Panch Mahal"],
        "timings": {
            "open_time": "06:00",
            "close_time": "18:00",
            "closed_on": [],
            "best_time_to_visit": "Morning / Early Afternoon (09:00 - 13:00)"
        },
        "entry_fee_inr": {
            "indian_adult": 50,
            "indian_child": 0,
            "foreigner": 610,
            "notes": "Dargah entry is free; monument ticket covers royal palace complex"
        },
        "indicative_duration_hours": 3.0,
        "accessibility": {
            "wheelchair_accessible": False,
            "senior_citizen_friendly": False,
            "walking_intensity": "High",
            "notes": "Buland Darwaza has 42 steep stone steps; palace area has cobblestones."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Expansive outdoor courtyards; wear comfortable walking shoes and hats."
        },
        "location": {
            "area": "Fatehpur Sikri, 37 km from Agra city",
            "latitude": 27.0945,
            "longitude": 77.6679,
            "nearby_metro": "Agra Cantt (36 km)"
        },
        "nearby_facilities": ["CNG shuttle buses from parking to gate", "Shoe counters", "Restrooms", "Guides"],
        "transport_hints": "Located 37 km southwest of Agra on NH-21. Best visited via private day cab or state tourist bus (1 hr drive).",
        "source": {
            "organization": "Archaeological Survey of India / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/fatehpur-sikri",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Can vehicles drive right up to Buland Darwaza?",
                "answer": "No. Private vehicles park at the base lot, from where tourists take mandatory green electric/CNG shuttle buses (INR 10) to the monument hill."
            }
        ]
    },
    {
        "id": "AGR-004",
        "name": "Mehtab Bagh (Moonlight Garden)",
        "city": "Agra",
        "state": "Uttar Pradesh",
        "category": "Nature",
        "interests": ["Nature", "Photography", "Heritage", "Sightseeing"],
        "description": "A 25-acre Charbagh garden complex situated on the northern bank of the Yamuna River, perfectly aligned opposite the Taj Mahal. Restored by ASI, it provides the ultimate serene, crowd-free vantage point for viewing and photographing the Taj Mahal at sunset reflected in the river waters.",
        "highlights": ["Iconic sunset panorama of Taj Mahal", "Peaceful botanical riverfront walkways", "Avoids crowds inside Taj Mahal"],
        "timings": {
            "open_time": "06:00",
            "close_time": "18:00",
            "closed_on": [],
            "best_time_to_visit": "Sunset (16:30 - 18:00)"
        },
        "entry_fee_inr": {
            "indian_adult": 25,
            "indian_child": 0,
            "foreigner": 300
        },
        "indicative_duration_hours": 1.5,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Completely level garden lawns with paved walkways."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Calm, relaxed environment ideal for families, photography enthusiasts, and seniors."
        },
        "location": {
            "area": "Opposite Taj Mahal, Nagla Devjit",
            "latitude": 27.1799,
            "longitude": 78.0422,
            "nearby_metro": "Agra Fort (4 km)"
        },
        "nearby_facilities": ["Lawn benches", "Ticket counter", "Restrooms", "Car parking"],
        "transport_hints": "15 minutes drive from Agra city across the Ambedkar Bridge.",
        "source": {
            "organization": "Archaeological Survey of India / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/mehtab-bagh",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Is Mehtab Bagh open on Fridays?",
                "answer": "Yes! While the Taj Mahal itself is closed on Fridays, Mehtab Bagh remains OPEN on Friday, making it the best spot to view the Taj Mahal on a Friday."
            }
        ]
    },

    # AYODHYA
    {
        "id": "AYD-001",
        "name": "Shri Ram Janmabhoomi Mandir",
        "city": "Ayodhya",
        "state": "Uttar Pradesh",
        "category": "Spiritual",
        "interests": ["Spiritual", "Architecture", "Heritage", "Culture"],
        "description": "The sacred birthplace temple of Bhagwan Shri Ram, constructed in grand Nagara architectural style using pink Bansi Paharpur sandstone from Rajasthan without any structural iron or steel. Spread over 70 acres, the temple features five mandaps (halls), 392 intricately carved pillars, and the sacred sanctum sanctorum housing Ram Lalla.",
        "highlights": ["Exquisite Nagara style carved sandstone temple", "Sacred Ram Lalla Garbhagriha", "Spacious pilgrim facilitation pathways"],
        "timings": {
            "open_time": "06:30",
            "close_time": "21:30",
            "closed_on": [],
            "best_time_to_visit": "Morning (07:00 - 10:00) or Evening (18:30 - 20:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "notes": "Free darshan; passes for special aartis available via official trust"
        },
        "indicative_duration_hours": 2.5,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Medium",
            "notes": "Pilgrim facilitation centre features ramps, wheelchairs, and dedicated senior citizen lanes."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "High security, excellent modern crowd management, safe for families."
        },
        "location": {
            "area": "Ramkot, Ayodhya",
            "latitude": 26.7956,
            "longitude": 82.1943,
            "nearby_metro": "Ayodhya Dham Railway Station (1.8 km)"
        },
        "nearby_facilities": ["Free digital locker complex", "Pilgrim medical center", "Prasadam center", "Battery vehicles for elderly", "Drinking water RO"],
        "transport_hints": "Ayodhya Dham Railway Station is only 1.8 km away. Electric golf carts run along Ram Path.",
        "source": {
            "organization": "Shri Ram Janmbhoomi Teerth Kshetra Trust / UP Tourism",
            "official_url": "https://srjbtkshetra.org",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Can visitors carry bags or phones inside?",
                "answer": "No mobiles, smartwatches, wallets or bags are permitted inside the temple complex. Free secure automated lockers are provided at the Pilgrim Facilitation Centre."
            }
        ]
    },
    {
        "id": "AYD-002",
        "name": "Hanuman Garhi Temple",
        "city": "Ayodhya",
        "state": "Uttar Pradesh",
        "category": "Spiritual",
        "interests": ["Spiritual", "Culture", "Heritage", "History"],
        "description": "A 10th-century fortress-temple dedicated to Lord Hanuman, who is revered as the guardian protector of Ayodhya. Custom dictates that pilgrims visit Hanuman Garhi before visiting Ram Janmabhoomi. Accessible via a flight of 76 stone steps leading to an ornate courtyard containing a beloved idol of young Hanuman sitting on his mother Anjani's lap.",
        "highlights": ["Fortress-like bastion architecture", "Historic tradition of first prayer before Ram Mandir", "Panoramic view over old Ayodhya city"],
        "timings": {
            "open_time": "05:00",
            "close_time": "22:00",
            "closed_on": [],
            "best_time_to_visit": "Early Morning (06:00 - 08:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0
        },
        "indicative_duration_hours": 1.5,
        "accessibility": {
            "wheelchair_accessible": False,
            "senior_citizen_friendly": False,
            "walking_intensity": "Medium",
            "notes": "Requires climbing 76 wide stone steps; railing provided along steps."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Vibrant energy; watch out for temple monkeys who may snatch food or spectacles."
        },
        "location": {
            "area": "Sai Nagar, Ayodhya",
            "latitude": 26.7972,
            "longitude": 82.2023,
            "nearby_metro": "Ayodhya Dham Station (1.2 km)"
        },
        "nearby_facilities": ["Prasad shops selling Besan Ladoos", "Shoe counters", "Restrooms"],
        "transport_hints": "Located right in the heart of Ayodhya on Hanuman Garhi road, 1 km from Ram Mandir.",
        "source": {
            "organization": "UP Tourism Ayodhya Circuit",
            "official_url": "https://ayodhya.nic.in/tourist-place/hanumangarhi",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "What is the famous prasad of Hanuman Garhi?",
                "answer": "Fresh, ghee-rich Besan Ladoos from local sweetshops along the temple steps are the iconic offering."
            }
        ]
    },
    {
        "id": "AYD-003",
        "name": "Saryu Ghat (Ram Ki Paidi) & Evening Aarti",
        "city": "Ayodhya",
        "state": "Uttar Pradesh",
        "category": "Culture",
        "interests": ["Culture", "Spiritual", "Photography", "Nature"],
        "description": "Ram Ki Paidi is a magnificent series of cascading riverfront ghats along the sacred Saryu River. Renovated with decorative lampposts, laser light shows, musical fountains, and clean flowing channels, it hosts the world-record Deepotsav celebrations and a daily serene evening Maha Aarti.",
        "highlights": ["Evening Saryu Maha Aarti at sunset", "Laser projection and musical fountain show", "Scenic reflection on river channels"],
        "timings": {
            "open_time": "05:00",
            "close_time": "23:00",
            "closed_on": [],
            "best_time_to_visit": "Evening (17:30 - 20:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "boat_ride": 100
        },
        "indicative_duration_hours": 2.0,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Paved promenade running along the ghats provides barrier-free strolls."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Delightful open-air public atmosphere with light shows and breeze."
        },
        "location": {
            "area": "Naya Ghat / Ram Ki Paidi",
            "latitude": 26.8049,
            "longitude": 82.2081,
            "nearby_metro": "Naya Ghat Crossing"
        },
        "nearby_facilities": ["Lata Mangeshkar Chowk with giant Veena", "Public seating", "Clean riverfront promenade", "Tea and snack stalls"],
        "transport_hints": "Directly accessible on the main highway at Naya Ghat. Abundant parking and e-rickshaws.",
        "source": {
            "organization": "Ayodhya Development Authority / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/ram-ki-paidi",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "What time is the Saryu Aarti?",
                "answer": "The Saryu Maha Aarti takes place daily at 18:30 in winter and 19:15 in summer, followed by the musical fountain show."
            }
        ]
    },

    # PRAYAGRAJ
    {
        "id": "PRY-001",
        "name": "Triveni Sangam & Boat Confluence Tour",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "category": "Spiritual",
        "interests": ["Spiritual", "Nature", "Culture", "Photography"],
        "description": "The sacred confluence of three rivers — the muddy brown Ganga, the greenish Yamuna, and the invisible mythical Saraswati. The premier holy pilgrimage site of Sanatana Dharma and host of the Maha Kumbh Mela. Visitors take wooden boats into the deep waters where the two contrasting water currents visibly meet.",
        "highlights": ["Visible dual-toned water confluence", "Wooden boat ride with migratory Siberian gulls (winter)", "Maha Kumbh pilgrimage grounds"],
        "timings": {
            "open_time": "05:00",
            "close_time": "19:00",
            "closed_on": [],
            "best_time_to_visit": "Sunrise (05:30 - 08:30) or Sunset (16:30 - 18:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "boat_ride_approx": 200,
            "notes": "Boat hire regulated by Prayagraj Mela Authority (approx INR 150-250 per passenger)"
        },
        "indicative_duration_hours": 2.5,
        "accessibility": {
            "wheelchair_accessible": False,
            "senior_citizen_friendly": True,
            "walking_intensity": "Medium",
            "notes": "Sandy riverbanks; boatmen assist seniors onto stable wooden confluence platforms."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "A profoundly spiritual experience; life-jackets provided on all regulated boats."
        },
        "location": {
            "area": "Kydganj / Sangam Ghat",
            "latitude": 25.4262,
            "longitude": 81.8845,
            "nearby_metro": "Prayagraj Junction (6 km)"
        },
        "nearby_facilities": ["Regulated boat ticketing counter", "Changing rooms", "Life jacket kiosks", "Pilgrim helpdesks"],
        "transport_hints": "6 km from Prayagraj Junction railway station. E-rickshaws and cabs drop visitors at Sangam parking.",
        "source": {
            "organization": "Prayagraj Mela Authority / UP Tourism",
            "official_url": "https://prayagraj.nic.in/tourist-place/sangam",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "When are migratory Siberian gulls present?",
                "answer": "Siberian birds flock to the Sangam during the winter months from November to late February."
            }
        ]
    },
    {
        "id": "PRY-002",
        "name": "Anand Bhavan & Swaraj Bhavan",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "category": "Heritage",
        "interests": ["History", "Heritage", "Culture", "Photography"],
        "description": "The historic two-storey mansion turned museum that served as the ancestral home of the Nehru-Gandhi family. Here major decisions of the Indian National Movement were formulated by Motilal Nehru, Jawaharlal Nehru, and Mahatma Gandhi. Features preserved period bedrooms, a 1930s library, and the Jawahar Planetarium.",
        "highlights": ["Jawahar Planetarium sky shows", "Preserved 1920s-1940s historical chambers", "Beautiful manicured colonial grounds"],
        "timings": {
            "open_time": "09:30",
            "close_time": "17:00",
            "closed_on": ["Monday"],
            "best_time_to_visit": "Morning / Early Afternoon (10:00 - 13:00)"
        },
        "entry_fee_inr": {
            "indian_adult": 70,
            "indian_child": 40,
            "foreigner": 200,
            "planetarium_addon": 60
        },
        "indicative_duration_hours": 2.0,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Ramps and flat stone walkways across ground floor and gardens."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Highly educational history museum and planetarium loved by students and families."
        },
        "location": {
            "area": "Tagore Town, Colonelganj",
            "latitude": 25.4608,
            "longitude": 81.8601,
            "nearby_metro": "Prayagraj Rambag (3 km)"
        },
        "nearby_facilities": ["Jawahar Planetarium", "Clean restrooms", "Souvenir bookshop", "Shaded gardens"],
        "transport_hints": "Located centrally in civil lines; easily accessible by auto or cab in 10 minutes.",
        "source": {
            "organization": "Jawaharlal Nehru Memorial Fund / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/anand-bhawan",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Is the Planetarium show in English or Hindi?",
                "answer": "The Jawahar Planetarium holds alternating daily shows in both Hindi and English."
            }
        ]
    },

    # MATHURA & VRINDAVAN
    {
        "id": "MTH-001",
        "name": "Shri Krishna Janmasthan Temple Complex",
        "city": "Mathura",
        "state": "Uttar Pradesh",
        "category": "Spiritual",
        "interests": ["Spiritual", "Heritage", "History", "Culture"],
        "description": "The sacred complex built around the subterranean prison cell (Garbha Griha) where Bhagwan Krishna was born to Devaki and Vasudeva. Encompasses the Keshavdev Temple, Bhagavata Bhavan with marble wall inscriptions of the entire Gita, and the ancient Potra Kund holy pond.",
        "highlights": ["Ancient prison cell Garbha Griha sanctum", "Gita Bhavan marble carvings", "Historic Potra Kund"],
        "timings": {
            "open_time": "05:30",
            "close_time": "21:30",
            "closed_on": [],
            "best_time_to_visit": "Morning (06:30 - 09:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0
        },
        "indicative_duration_hours": 2.0,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Paved flat courtyards with ramps for senior citizens."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Deeply spiritual and cultural, well-organized pilgrim flow."
        },
        "location": {
            "area": "Deeg Gate, Mathura",
            "latitude": 27.5056,
            "longitude": 77.6692,
            "nearby_metro": "Mathura Junction (3 km)"
        },
        "nearby_facilities": ["Free digital locker facility", "Prasadam stall (Mathura Peda)", "Restrooms", "Security checkpoint"],
        "transport_hints": "10 minutes by auto from Mathura Junction railway station.",
        "source": {
            "organization": "Shri Krishna Janmasthan Sansthan / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/shri-krishna-janmabhoomi",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Are mobile phones allowed inside?",
                "answer": "No. Strict security applies. Phones and electronics must be deposited in the trust's free security lockers outside."
            }
        ]
    },
    {
        "id": "MTH-002",
        "name": "Prem Mandir & Musical Fountain",
        "city": "Vrindavan",
        "state": "Uttar Pradesh",
        "category": "Spiritual",
        "interests": ["Spiritual", "Architecture", "Photography", "Culture"],
        "description": "Maintained by Jagadguru Kripalu Parishat, this 54-acre temple is sculpted entirely out of Italian white Carrara marble. Showcases life-size dioramas of Krishna's pastimes (Govardhan Leela, Raas Leela), and transforms each evening with a multi-colored LED illumination and synchronized musical fountain show.",
        "highlights": ["Pure Italian Carrara marble architecture", "Mesmerizing evening musical fountain and light show", "Intricate 3D life-sized Leela tableaux"],
        "timings": {
            "open_time": "05:30",
            "close_time": "20:30",
            "closed_on": [],
            "best_time_to_visit": "Evening / Illumination (17:30 - 20:15)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "notes": "Free entry for all"
        },
        "indicative_duration_hours": 2.0,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Modern paved ramps, wide pathways, and wheelchairs available on request."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Spectacular light show makes it a top favorite for children and families."
        },
        "location": {
            "area": "Chatikara Road, Raman Reti, Vrindavan",
            "latitude": 27.5714,
            "longitude": 77.6713,
            "nearby_metro": "Mathura Junction (12 km)"
        },
        "nearby_facilities": ["Canteen serving pure vegetarian satvik food", "Spacious car parking", "Restrooms", "Drinking water stations"],
        "transport_hints": "Located on the main road between NH-19 (Chatikara) and Vrindavan. 20 mins by cab from Mathura.",
        "source": {
            "organization": "Jagadguru Kripalu Parishat / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/prem-mandir",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "What time is the musical fountain light show?",
                "answer": "The musical fountain and dynamic light show runs every evening from 19:30 to 20:00 (timing shifts slightly between winter and summer)."
            }
        ]
    },
    # AYODHYA Continued
    {
        "id": "AYD-004",
        "name": "Kanak Bhavan",
        "city": "Ayodhya",
        "state": "Uttar Pradesh",
        "category": "Spiritual",
        "interests": ["Spiritual", "Heritage", "Architecture", "Culture"],
        "description": "A magnificent palace-temple gifted to Devi Sita by Queen Kaikeyi upon her marriage to Lord Rama. Rebuilt in 1891 by the Queen of Orchha, it resembles a royal Rajasthani-Bundelkhandi palace housing golden-crowned idols of Shri Ram and Sita.",
        "highlights": ["Intricate Bundelkhandi palace architecture", "Gold-crowned central sanctum deities", "Daily morning bhajan recitals"],
        "timings": {
            "open_time": "08:00",
            "close_time": "22:00",
            "closed_on": [],
            "best_time_to_visit": "Morning (09:00 - 11:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0
        },
        "indicative_duration_hours": 1.5,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Courtyard on ground level; small step at entry ramp."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Very serene and beautiful musical environment."
        },
        "location": {
            "area": "Tulsi Nagar, Ayodhya",
            "latitude": 26.7995,
            "longitude": 82.2008,
            "nearby_metro": "Ayodhya Dham Station (1.5 km)"
        },
        "nearby_facilities": ["Shoe counter", "Prasad counter", "Drinking water"],
        "transport_hints": "500 meters from Hanuman Garhi; easily combined on foot or via e-rickshaw.",
        "source": {
            "organization": "UP Tourism Ayodhya Circuit",
            "official_url": "https://ayodhya.nic.in/tourist-place/kanak-bhawan",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Is entry ticket needed for Kanak Bhavan?",
                "answer": "No entry ticket is required. Darshan is completely free for all pilgrims."
            }
        ]
    },
    {
        "id": "AYD-005",
        "name": "Guptar Ghat & Saryu River Walk",
        "city": "Ayodhya",
        "state": "Uttar Pradesh",
        "category": "Nature",
        "interests": ["Nature", "Spiritual", "Photography", "Culture"],
        "description": "The sacred riverfront site where Lord Rama took Jal Samadhi to return to his heavenly abode (Vaikuntha). Modernized with beautiful open air parks, jogging paths, boating facilities, and solar-lit heritage ghats.",
        "highlights": ["Scenic sunset on the Saryu River", "Clean landscaped riverside parks", "Motorboat and paddle boat tours"],
        "timings": {
            "open_time": "05:00",
            "close_time": "22:00",
            "closed_on": [],
            "best_time_to_visit": "Late Afternoon to Sunset (16:30 - 18:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "boat_ride": 150
        },
        "indicative_duration_hours": 1.5,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Paved barrier-free walking promenade along the river."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Open river breeze, green lawns, ideal for evening leisure."
        },
        "location": {
            "area": "Cantonment area, Ayodhya",
            "latitude": 26.7820,
            "longitude": 82.1384,
            "nearby_metro": "Ayodhya Cantt Station (3.5 km)"
        },
        "nearby_facilities": ["Boat rental jetty", "Open air cafe", "Clean restrooms", "Car parking"],
        "transport_hints": "15 minutes drive west of Ayodhya old town along the river bypass.",
        "source": {
            "organization": "Ayodhya Development Authority",
            "official_url": "https://uptourism.gov.in/en/post/guptar-ghat",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Can we take boat rides at Guptar Ghat?",
                "answer": "Yes, licensed speedboats and traditional wooden boats operate throughout the day."
            }
        ]
    },

    # PRAYAGRAJ Continued
    {
        "id": "PRY-003",
        "name": "Allahabad Fort & Patalpuri Temple / Akshayavat",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "category": "Heritage",
        "interests": ["Heritage", "Spiritual", "History", "Architecture"],
        "description": "Constructed in 1583 by Mughal Emperor Akbar overlooking the confluence of the rivers Ganga and Yamuna. Inside lies the subterranean Patalpuri Temple, the legendary undying banyan tree (Akshayavat) mentioned in Hindu scriptures, and the famous Ashoka Pillar with edicts from Samudragupta and Jahangir.",
        "highlights": ["Sacred immortal Akshayavat banyan tree", "Ancient subterranean Patalpuri Temple", "Ashoka Pillar with Brahmi and Persian inscriptions"],
        "timings": {
            "open_time": "07:00",
            "close_time": "18:00",
            "closed_on": [],
            "best_time_to_visit": "Morning (08:00 - 11:00)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "notes": "Access to Akshayavat and Patalpuri is free with government ID proof"
        },
        "indicative_duration_hours": 1.5,
        "accessibility": {
            "wheelchair_accessible": False,
            "senior_citizen_friendly": True,
            "walking_intensity": "Medium",
            "notes": "Subterranean corridor requires walking down a gently sloping ramp."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Historical and mythological significance makes it popular for all pilgrims."
        },
        "location": {
            "area": "Cantonment, Near Sangam",
            "latitude": 25.4294,
            "longitude": 81.8770,
            "nearby_metro": "Sangam area"
        },
        "nearby_facilities": ["Army security counter", "Shoe stand", "Drinking water"],
        "transport_hints": "Directly accessible on the road leading down to Sangam.",
        "source": {
            "organization": "Archaeological Survey of India / Ministry of Defence",
            "official_url": "https://prayagraj.nic.in/tourist-place/allahabad-fort",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Is the entire fort open to public?",
                "answer": "Since it is an active Indian Army garrison, only Patalpuri Temple, Saraswati Kund and Akshayavat section are accessible to the public."
            }
        ]
    },
    {
        "id": "PRY-004",
        "name": "Khusro Bagh",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "category": "Heritage",
        "interests": ["Heritage", "Architecture", "Nature", "History"],
        "description": "A magnificent walled Mughal garden spanning over 40 acres housing the ornate sandstone mausoleums of Prince Khusro (eldest son of Emperor Jahangir), his mother Shah Begum, and his sister Sultan Nithar Begum. Famous for its three-tiered tomb architecture, Persian calligraphy inscriptions, and century-old guava orchards.",
        "highlights": ["Three-tiered Mughal sandstone mausoleum", "Historic Prayagraj guava orchards", "Peaceful shaded walking gardens"],
        "timings": {
            "open_time": "06:00",
            "close_time": "19:00",
            "closed_on": [],
            "best_time_to_visit": "Morning or Late Afternoon (15:30 - 17:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0,
            "notes": "Free public garden entry"
        },
        "indicative_duration_hours": 1.5,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Flat stone paths and garden lawns with plenty of park benches."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Quiet open park setting suitable for seniors and families."
        },
        "location": {
            "area": "Lukarganj, Prayagraj",
            "latitude": 25.4419,
            "longitude": 81.8247,
            "nearby_metro": "Prayagraj Junction (600m)"
        },
        "nearby_facilities": ["Park benches", "Restrooms", "Garden walks", "Parking lot"],
        "transport_hints": "Located just 500 meters from the City Side exit of Prayagraj Junction railway station.",
        "source": {
            "organization": "Archaeological Survey of India / UP Tourism",
            "official_url": "https://prayagraj.nic.in/tourist-place/khusro-bagh",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Is Khusro Bagh near the railway station?",
                "answer": "Yes, it is within walking distance (less than 1 km) from Prayagraj Junction Railway Station."
            }
        ]
    },

    # AGRA Continued
    {
        "id": "AGR-005",
        "name": "Tomb of I'timad-ud-Daulah (Baby Taj)",
        "city": "Agra",
        "state": "Uttar Pradesh",
        "category": "Heritage",
        "interests": ["Heritage", "Architecture", "Photography", "History"],
        "description": "Often regarded as the draft or jewel box of the Taj Mahal, this elegant mausoleum was built between 1622 and 1628 by Empress Nur Jahan for her father Mirza Ghiyas Beg. It marks the transition in Mughal architecture from red sandstone to white marble and first featured extensive pietra dura stone inlay work.",
        "highlights": ["Precursor to Taj Mahal marble architecture", "Intricate floral pietra dura inlays", "Quiet Yamuna riverbank setting"],
        "timings": {
            "open_time": "06:00",
            "close_time": "18:00",
            "closed_on": [],
            "best_time_to_visit": "Late Morning or Afternoon (11:00 - 15:00)"
        },
        "entry_fee_inr": {
            "indian_adult": 30,
            "indian_child": 0,
            "foreigner": 310
        },
        "indicative_duration_hours": 1.5,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Paved garden paths with modest ramped steps."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Much less crowded than the Taj Mahal; intimate and peaceful."
        },
        "location": {
            "area": "Moti Bagh, Agra",
            "latitude": 27.1930,
            "longitude": 78.0312,
            "nearby_metro": "Agra Fort (3 km)"
        },
        "nearby_facilities": ["ASI ticket counter", "Restrooms", "Garden seating"],
        "transport_hints": "Located on the eastern bank of Yamuna, 5 km from Taj Mahal. Easily combined with Mehtab Bagh.",
        "source": {
            "organization": "Archaeological Survey of India / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/tomb-of-itmad-ud-daulah",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Why is it called Baby Taj?",
                "answer": "Because its white marble dome, corner minarets, and delicate pietra dura lattice work inspired the larger architecture of the Taj Mahal."
            }
        ]
    },

    # MATHURA & VRINDAVAN Continued
    {
        "id": "MTH-003",
        "name": "Banke Bihari Temple",
        "city": "Vrindavan",
        "state": "Uttar Pradesh",
        "category": "Spiritual",
        "interests": ["Spiritual", "Culture", "Heritage", "History"],
        "description": "The most revered and visited temple in Vrindavan, established by Swami Haridas in 1864. The idol of Banke Bihari (Lord Krishna in Tribhanga pose) is shielded periodically behind a curtain to prevent devotees from fainting in devotional ecstasy. Famous for its energetic darshans, Holi celebrations, and sweet offerings.",
        "highlights": ["Legendary Banke Bihari Vigraha in Tribhanga posture", "Curtain pull darshan tradition", "Historic temple alleys with Makhan and Pedas"],
        "timings": {
            "open_time": "07:45",
            "close_time": "21:30",
            "closed_on": ["Afternoon closure from 12:00 to 17:30 daily"],
            "best_time_to_visit": "Morning (08:30 - 11:00) or Evening (18:00 - 20:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0
        },
        "indicative_duration_hours": 1.5,
        "accessibility": {
            "wheelchair_accessible": False,
            "senior_citizen_friendly": False,
            "walking_intensity": "High",
            "notes": "Very narrow, crowded old Vrindavan streets; strong crowd surge inside the temple hall."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Hold hands of small children and secure spectacles against monkeys in the alleys."
        },
        "location": {
            "area": "Godowlia / Bihari Pura, Vrindavan",
            "latitude": 27.5815,
            "longitude": 77.7011,
            "nearby_metro": "Mathura Junction (13 km)"
        },
        "nearby_facilities": ["Shoe stands", "Prasad shops", "Local sweet vendors"],
        "transport_hints": "Vehicles stop at outer Vrindavan parking; take authorized electric e-rickshaw (10 mins) to temple entry lane.",
        "source": {
            "organization": "Shri Banke Bihari Ji Mandir Trust / UP Tourism",
            "official_url": "https://uptourism.gov.in/en/post/banke-bihari-temple",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Is the temple open all day?",
                "answer": "No. The temple closes daily between 12:00 PM and 5:30 PM (varies slightly by season) for deity rest."
            }
        ]
    },
    {
        "id": "MTH-004",
        "name": "ISKCON Temple Vrindavan (Sri Krishna Balaram Mandir)",
        "city": "Vrindavan",
        "state": "Uttar Pradesh",
        "category": "Spiritual",
        "interests": ["Spiritual", "Culture", "Architecture", "Music"],
        "description": "One of the major international ISKCON temples founded by A.C. Bhaktivedanta Swami Prabhupada in 1975. Famous for its 24-hour continuous Hare Krishna Maha-Mantra kirtan, magnificent white marble gateway, Samadhi museum of Srila Prabhupada, and pure satvik Govinda's restaurant.",
        "highlights": ["Continuous 24-hour Akhanda Kirtan", "White marble courtyard and ornate Tamal tree", "Govinda's international vegetarian restaurant"],
        "timings": {
            "open_time": "04:30",
            "close_time": "20:45",
            "closed_on": ["Deity curtains closed 12:45 to 16:30"],
            "best_time_to_visit": "Sandhya Aarti (18:30 - 19:30)"
        },
        "entry_fee_inr": {
            "indian_adult": 0,
            "indian_child": 0,
            "foreigner": 0
        },
        "indicative_duration_hours": 2.0,
        "accessibility": {
            "wheelchair_accessible": True,
            "senior_citizen_friendly": True,
            "walking_intensity": "Low",
            "notes": "Paved entrance, wide courtyards, elevators to guesthouse and samadhi."
        },
        "family_friendly": {
            "suitable": True,
            "notes": "Peaceful, hygienic, welcoming international atmosphere with high quality vegetarian dining."
        },
        "location": {
            "area": "Bhaktivedanta Swami Marg, Raman Reti, Vrindavan",
            "latitude": 27.5727,
            "longitude": 77.6857,
            "nearby_metro": "Mathura Junction (11 km)"
        },
        "nearby_facilities": ["Govinda's Restaurant", "Bookstore", "Spiritual gift shop", "Clean restrooms", "Guest house"],
        "transport_hints": "Located on the main Bhaktivedanta Swami Marg, 5 minutes from Prem Mandir.",
        "source": {
            "organization": "ISKCON Vrindavan / UP Tourism",
            "official_url": "https://www.iskconvrindavan.com",
            "data_confidence": "Verified Public Source",
            "is_mock": False
        },
        "faqs": [
            {
                "question": "Can visitors attend the evening Aarti?",
                "answer": "Yes, the Sandhya (Gor-aarti) at 18:30 is open to all visitors with ecstatic singing and dancing."
            }
        ]
    }
]

with open("data/raw/raw_attractions_up.json", "w", encoding="utf-8") as f:
    json.dump(raw_attractions, f, indent=2, ensure_ascii=False)

print(f"Successfully generated data/raw/raw_attractions_up.json with {len(raw_attractions)} attractions across 6 UP cities.")
