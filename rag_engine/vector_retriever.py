"""
Vector & Semantic Knowledge Base Retriever for Tourism RAG.
Layer 2: RAG Layer
"""
import os
import json
import numpy as np
from typing import List, Dict, Any, Optional
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TourismKnowledgeRetriever:
    def __init__(self, chunks_path: Optional[str] = None):
        if chunks_path is None:
            # 1. Base directory relative to this file
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            candidate = os.path.join(base_dir, "data", "prepared", "tourism_chunks.json")
            if os.path.exists(candidate):
                chunks_path = candidate
            elif os.path.exists(os.path.join("data", "prepared", "tourism_chunks.json")):
                chunks_path = os.path.join("data", "prepared", "tourism_chunks.json")
            else:
                chunks_path = os.path.join("/var/task", "data", "prepared", "tourism_chunks.json")
        self.chunks_path = chunks_path
        self.chunks: List[Dict[str, Any]] = []
        self.vectorizer: Optional[TfidfVectorizer] = None
        self.tfidf_matrix = None
        self._load_and_index()

    def _load_and_index(self):
        if not os.path.exists(self.chunks_path):
            raise FileNotFoundError(f"Knowledge chunks not found at {self.chunks_path}. Run chunker first.")

        with open(self.chunks_path, "r", encoding="utf-8") as f:
            self.chunks = json.load(f)

        corpus = [c["content"] for c in self.chunks]
        # Use sublinear tf and character/word n-grams for robust Hindi/English tourism term matching
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True,
            stop_words="english",
            max_features=5000
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(corpus)
        print(f"Vector Knowledge Base initialized with {len(self.chunks)} chunks across vocabulary size {self.tfidf_matrix.shape[1]}.")

    def retrieve(
        self,
        query: str,
        city_filter: Optional[str] = None,
        category_filter: Optional[str] = None,
        top_k: int = 4,
        min_score: float = 0.05
    ) -> List[Dict[str, Any]]:
        """
        Retrieve the top-K grounded chunks relevant to the user query.
        Applies optional city or category metadata pre-filtering.
        """
        if not query.strip() or self.tfidf_matrix is None:
            return []

        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()

        ranked_indices = np.argsort(scores)[::-1]
        results = []

        for idx in ranked_indices:
            score = float(scores[idx])
            if score < min_score and len(results) >= 1:
                break
            
            chunk = self.chunks[idx]

            # City filter check
            if city_filter and city_filter.strip().lower() != "all":
                if chunk["city"].strip().lower() != city_filter.strip().lower():
                    continue

            # Category filter check
            if category_filter and category_filter.strip().lower() != "all":
                chunk_cat = chunk["metadata"].get("category", "")
                if chunk_cat.strip().lower() != category_filter.strip().lower():
                    continue

            results.append({
                "chunk_id": chunk["chunk_id"],
                "attraction_id": chunk["attraction_id"],
                "attraction_name": chunk["attraction_name"],
                "city": chunk["city"],
                "chunk_type": chunk["chunk_type"],
                "content": chunk["content"],
                "source_citation": chunk["source_citation"],
                "score": round(score, 4)
            })

            if len(results) >= top_k:
                break

        return results

    def get_grounded_context_str(self, query: str, city_filter: Optional[str] = None, top_k: int = 4) -> str:
        """Format retrieved chunks into a numbered context block for LLM prompt grounding."""
        retrieved = self.retrieve(query=query, city_filter=city_filter, top_k=top_k)
        if not retrieved:
            return "No matching verified records found in knowledge base."

        context_lines = []
        for i, item in enumerate(retrieved, start=1):
            context_lines.append(
                f"[{i}] SOURCE: {item['source_citation']} (Chunk ID: {item['chunk_id']})\n"
                f"Content: {item['content']}"
            )
        return "\n\n".join(context_lines)

# Singleton instance helper
_retriever_instance = None

def get_retriever() -> TourismKnowledgeRetriever:
    global _retriever_instance
    if _retriever_instance is None:
        _retriever_instance = TourismKnowledgeRetriever()
    return _retriever_instance

if __name__ == "__main__":
    retriever = TourismKnowledgeRetriever()
    test_queries = [
        ("Taj Mahal timings and Friday closure", "Agra"),
        ("Bara Imambara labyrinth guide senior citizens", "Lucknow"),
        ("Subah-e-Banaras morning aarti yoga", "Varanasi"),
        ("Ram Janmabhoomi darshan phones lockers", "Ayodhya"),
        ("Sangam boat ride confluence", "Prayagraj")
    ]
    print("\n--- RUNNING VECTOR RETRIEVAL SMOKE TESTS ---")
    for q, city in test_queries:
        print(f"\nQuery: '{q}' (City: {city})")
        hits = retriever.retrieve(q, city_filter=city, top_k=2)
        for h in hits:
            print(f"  * [{h['score']}] {h['attraction_name']} ({h['chunk_type']}): {h['content'][:95]}... Source: {h['source_citation']}")
