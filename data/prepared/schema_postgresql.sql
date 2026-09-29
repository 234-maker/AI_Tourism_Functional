-- ==============================================================================
-- PostgreSQL & PGVector DDL Schema for AI-Based Tourism Recommendation & Itinerary Planner
-- Layer 1: Data Layer & Layer 2: RAG Layer Vector Schema
-- ==============================================================================

-- Enable PGVector extension for similarity search if available
CREATE EXTENSION IF NOT EXISTS vector;

-- 1. Destinations / Cities Table
CREATE TABLE IF NOT EXISTS destinations (
    city_id VARCHAR(10) PRIMARY KEY,
    city_name VARCHAR(100) NOT NULL UNIQUE,
    state VARCHAR(100) NOT NULL DEFAULT 'Uttar Pradesh',
    region_type VARCHAR(50) DEFAULT 'Heritage & Spiritual Circuit',
    ideal_duration_days INT DEFAULT 2,
    best_season VARCHAR(100) DEFAULT 'October to March',
    airport_code VARCHAR(10),
    railway_hub VARCHAR(100),
    overview TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Curated Attractions Table
CREATE TABLE IF NOT EXISTS attractions (
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL DEFAULT 'Uttar Pradesh',
    category VARCHAR(50) NOT NULL,
    interests_json JSONB,
    description TEXT NOT NULL,
    highlights_json JSONB,
    open_time VARCHAR(10) NOT NULL,
    close_time VARCHAR(10) NOT NULL,
    open_time_mins INT NOT NULL,
    close_time_mins INT NOT NULL,
    closed_days_json JSONB,
    best_time_to_visit VARCHAR(100),
    fee_adult_inr NUMERIC(8, 2) DEFAULT 0.00,
    fee_child_inr NUMERIC(8, 2) DEFAULT 0.00,
    fee_foreigner_inr NUMERIC(8, 2) DEFAULT 0.00,
    indicative_duration_hours NUMERIC(4, 2) DEFAULT 1.5,
    wheelchair_accessible BOOLEAN DEFAULT FALSE,
    senior_friendly BOOLEAN DEFAULT FALSE,
    walking_intensity VARCHAR(20) DEFAULT 'Medium',
    accessibility_notes TEXT,
    family_friendly BOOLEAN DEFAULT TRUE,
    family_notes TEXT,
    area VARCHAR(150),
    latitude NUMERIC(9, 6) NOT NULL,
    longitude NUMERIC(9, 6) NOT NULL,
    nearby_transit VARCHAR(255),
    facilities_json JSONB,
    transport_hints TEXT,
    source_name VARCHAR(255) NOT NULL,
    source_url TEXT NOT NULL,
    is_mock BOOLEAN DEFAULT FALSE,
    search_blob TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexing for high-performance lookup
CREATE INDEX IF NOT EXISTS idx_attractions_city ON attractions(city);
CREATE INDEX IF NOT EXISTS idx_attractions_category ON attractions(category);
CREATE INDEX IF NOT EXISTS idx_attractions_wheelchair ON attractions(wheelchair_accessible);
CREATE INDEX IF NOT EXISTS idx_attractions_senior ON attractions(senior_friendly);

-- 3. Attraction FAQs Table (Knowledge Base Grounding)
CREATE TABLE IF NOT EXISTS attraction_faqs (
    faq_id SERIAL PRIMARY KEY,
    attraction_id VARCHAR(20) REFERENCES attractions(id) ON DELETE CASCADE,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    source_url TEXT
);

CREATE INDEX IF NOT EXISTS idx_faqs_attraction ON attraction_faqs(attraction_id);

-- 4. RAG Knowledge Chunks & PGVector Table
CREATE TABLE IF NOT EXISTS tourism_knowledge_chunks (
    chunk_id VARCHAR(50) PRIMARY KEY,
    attraction_id VARCHAR(20) REFERENCES attractions(id) ON DELETE SET NULL,
    city VARCHAR(100) NOT NULL,
    chunk_type VARCHAR(50) NOT NULL, -- 'OVERVIEW', 'CULTURE_HISTORY', 'ACCESSIBILITY_LOGISTICS', 'FAQ'
    content TEXT NOT NULL,
    metadata JSONB,
    source_citation TEXT NOT NULL,
    embedding vector(384) -- compatible with all-MiniLM-L6-v2 or TF-IDF dense embeddings
);

-- Create HNSW Vector Index for PGVector Cosine Distance
CREATE INDEX IF NOT EXISTS idx_chunks_embedding ON tourism_knowledge_chunks 
USING hnsw (embedding vector_cosine_ops);

-- 5. Itineraries Table (Persisted Travel Plans)
CREATE TABLE IF NOT EXISTS itineraries (
    itinerary_id VARCHAR(50) PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    duration_days INT NOT NULL,
    traveller_type VARCHAR(50),
    budget_level VARCHAR(50),
    language VARCHAR(20) DEFAULT 'English',
    plan_json JSONB NOT NULL,
    indicative_total_cost_inr NUMERIC(10, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 6. Responsible AI Hallucination & Audit Log
CREATE TABLE IF NOT EXISTS hallucination_audit_log (
    log_id SERIAL PRIMARY KEY,
    query TEXT NOT NULL,
    response TEXT NOT NULL,
    grounding_score NUMERIC(5, 3) NOT NULL, -- 0.000 to 1.000
    cited_sources JSONB,
    unsupported_claims JSONB,
    status VARCHAR(30) DEFAULT 'VERIFIED_GROUNDED',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 7. User Feedback & Insights Table
CREATE TABLE IF NOT EXISTS user_feedback (
    feedback_id SERIAL PRIMARY KEY,
    session_id VARCHAR(100),
    destination VARCHAR(100),
    rating INT CHECK (rating >= 1 AND rating <= 5),
    feedback_category VARCHAR(50), -- 'ACCURACY', 'PACING', 'TIMING_ERROR', 'RECOMMENDATION_QUALITY', 'OTHER'
    comment TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
