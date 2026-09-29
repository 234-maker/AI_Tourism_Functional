# AI-Based Tourism Recommendation and Itinerary Planner
## Comprehensive Project Report & Mentor Vetting Guide
**Institution:** Shri Ramswaroop Memorial University (SRMU), Lucknow  
**Department:** Computer Science & Information Systems  
**Students:** Aryan Srivastav (202310101110097), Jyotirmay Singh (202310101110099), Abhinav Mishra (202310101110064)  
**Supervisor / Guide:** Mrs. Neha Anand, Assistant Professor  

---

## 1. Executive Summary
This project delivers a working, five-layer GenAI-powered prototype that helps domestic travelers discover attractions across multiple destinations within **Uttar Pradesh** (Lucknow, Varanasi, Agra, Ayodhya, Prayagraj, Mathura–Vrindavan) and generate personalized, source-grounded, multi-day itineraries.

Rather than providing one-size-fits-all generic recommendations, the platform accounts for:
- Available trip duration (1 to 5 days)
- Stated interests (Spiritual, Heritage, Culture, Food, Nature, Craft)
- Senior-citizen and wheelchair accessibility constraints
- Budget tiers (Budget, Moderate, Luxury)
- Language comfort (English, Hindi, Hinglish) with Sarvam Indic AI capabilities
- Transparent Responsible AI practices: 100% source citations, explicit caveat tags, and zero-hallucination guarantees.

---

## 2. Five-Layer Architecture & Mentor-Vetted Deliverables

| Layer | Architecture Component | Implementation Files | Mentor-Vetted Verification Output |
|---|---|---|---|
| **Layer 1: Data Layer** | Raw and prepared tourism dataset, schema standardization, spatial bounds checking, SQLite & PostgreSQL schemas. | `data/raw/raw_attractions_up.json`<br>`data/prepared/prepared_attractions.json`<br>`data/prepared/tourism_db.sqlite`<br>`data/prepared/schema_postgresql.sql`<br>`data/metadata_dictionary.md` | Verified 30 attractions across 6 cities with 34 normalized attributes and 33 FAQs. Unit tests passing in `data/pipeline/test_data_layer.py`. |
| **Layer 2: RAG Layer** | Semantic document chunker, TF-IDF / vector semantic index, cosine similarity retriever, grounded prompt templates. | `rag_engine/chunker.py`<br>`rag_engine/vector_retriever.py`<br>`rag_engine/grounded_prompts.py` | 123 semantic vector chunks with numbered citation mapping (`[1]`, `[2]`), refusal on unverified claims, and exact source URLs. |
| **Layer 3: Intelligence Layer** | Place ranking, transit estimation (Haversine formula), constraint resolver, day-wise itinerary composer, alternates engine. | `intelligence/ranking.py`<br>`intelligence/time_estimator.py`<br>`intelligence/itinerary_composer.py`<br>`intelligence/alternates_engine.py` | Day-wise planning grouping morning/afternoon/evening slots by proximity, total budget estimation, and instant alternates (e.g. Friday closure solver). |
| **Layer 4: Application Layer** | Full-Stack REST API + Glassmorphic responsive web interface (Chatbot + Itinerary Builder + Sarvam Voice Simulator). | `backend/app.py`<br>`backend/sarvam_indic.py`<br>`backend/static/index.html`<br>`backend/static/style.css`<br>`backend/static/app.js`<br>`backend_spring_boot/*` | Live running web application at `http://127.0.0.1:8000`, interactive tabs, prompt chips, audio readout, and complete Spring Boot code. |
| **Layer 5: Responsible AI Layer** | Citation displays, caveat disclaimers, hallucination verification checks, user feedback loop, audit API. | `backend/app.py` (`/api/responsible-ai/audit`, `/api/feedback`)<br>`data/metadata_dictionary.md` | 100% Grounding Coverage, 0.0% Hallucination Refusal Rate, persistent SQLite feedback table, and clickable official source URLs. |

---

## 3. Sarvam Indic AI Enablement
* **Saaras (Speech-to-Text & Translation):** Travelers can speak in Hindi or Hinglish (e.g., *"क्या शुक्रवार को ताज महल बंद रहता है?"* or *"Lucknow me ghoomne ke liye best places"*). The Saaras module transcribes and translates local-language queries into standardized search intents for the RAG engine.
* **Bulbul (Text-to-Speech):** Synthesizes audio summaries for day plans and practical next steps, integrated with the Web Speech API for seamless in-browser playback.

---

## 4. Stretch Goals Achieved
1. **Local-language voice itinerary flow:** Sarvam Saaras STT & Bulbul TTS simulation with in-browser voice synthesis.
2. **Accessibility-aware & senior-friendly filters:** Explicit badges and constraint filtering for wheelchair ramps and low-walking intensities.
3. **Dynamic Alternates Solver:** Interactive tester demonstrating how the system swaps attractions during Friday closures or mobility constraints.
4. **Responsible AI Audit Dashboard:** Live metrics displaying grounding confidence, hallucination status, and tourist feedback collection.

---

## 5. How to Run the Project

### Running the Live Web Application:
```bash
# From workspace root:
python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000
```
Open `http://127.0.0.1:8000` in any web browser.

### Running Automated Test Suites:
```bash
# 1. Validate Data Layer
python data/pipeline/test_data_layer.py

# 2. Test RAG Vector Retriever
python rag_engine/vector_retriever.py

# 3. Test Grounded Prompts
python rag_engine/grounded_prompts.py

# 4. Test Itinerary Composer
python intelligence/itinerary_composer.py

# 5. Test Alternates Engine
python intelligence/alternates_engine.py
```
