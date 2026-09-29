# AI-Based Tourism Recommendation and Itinerary Planner

A GenAI-powered intelligent tourism recommendation and itinerary planning system focusing on Uttar Pradesh (Lucknow, Varanasi, Agra, Ayodhya, Prayagraj, Mathura–Vrindavan).

## 🌟 Key Features
- **Multi-Day Personalized Itineraries**: Constraint-aware planning based on trip duration (1–5 days), interests (Spiritual, Heritage, Food, Nature, Culture, Craft), budget tiers, and mobility requirements.
- **RAG-Powered Grounded Q&A**: Domain-specific retrieval with citations (`[1]`, `[2]`), verified facts, and hallucination safeguards.
- **Sarvam Indic AI Voice Capabilities**: Saaras Speech-to-Text & Translation and Bulbul Text-to-Speech audio syntheses for Hindi/Hinglish travelers.
- **Accessibility & Senior-Friendly Routing**: Highlights wheelchair ramps, flat terrains, and low-walking intensities.
- **Dynamic Alternates Solver**: Instant swap suggestions when monuments are closed (e.g., Friday Taj Mahal closure) or when mobility constraints change.
- **Dual Backend Architecture**: FastAPI (Python) intelligence & RAG pipeline alongside a Spring Boot Java enterprise service layer.

---

## 🏛️ Project Architecture
1. **Data Layer (`/data`)**: Curated attractions, spatial coordinates, metadata schemas, and SQLite/PostgreSQL models.
2. **RAG Engine (`/rag_engine`)**: Semantic chunking, TF-IDF vector retrieval, cosine similarity search, and grounded prompts.
3. **Intelligence Layer (`/intelligence`)**: Place ranking, transit estimation (Haversine formula), constraint resolver, and day-wise composer.
4. **Application Layer (`/backend`, `/backend_spring_boot`)**: FastAPI REST APIs with glassmorphic responsive web interface and Spring Boot backend.
5. **Responsible AI Layer**: Full citation tracking, caveat disclaimers, and tourist feedback loop.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Java 17+ & Maven (for Spring Boot backend)

### 1. Run the Python FastAPI Backend & UI
```bash
# Install dependencies
pip install fastapi uvicorn pydantic scikit-learn requests

# Start the application server
python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser.

### 2. Run the Spring Boot Backend (Optional)
```bash
cd backend_spring_boot
mvn clean spring-boot:run
```

---

## 🧪 Testing the Components
```bash
# Validate Data Layer
python data/pipeline/test_data_layer.py

# Test RAG Vector Retriever
python rag_engine/vector_retriever.py

# Test Grounded Prompts
python rag_engine/grounded_prompts.py

# Test Itinerary Composer
python intelligence/itinerary_composer.py

# Test Alternates Engine
python intelligence/alternates_engine.py
```

---

## 📚 Documentation
For complete academic details, system design diagrams, and mentor vetting criteria, see:
[`docs/PROJECT_REPORT_AND_MENTOR_GUIDE.md`](docs/PROJECT_REPORT_AND_MENTOR_GUIDE.md).
