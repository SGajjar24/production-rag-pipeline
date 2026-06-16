import chromadb
from core.config import settings

class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.CHROMA_DB_PATH)
        self.collection = self.client.get_or_create_collection(
            name="rag_documents"
        )
    
    def upsert_chunks(self, chunks):
        ids = [c["metadata"]["hash"] for c in chunks]
        documents = [c["text"] for c in chunks]
        metadatas = [c["metadata"] for c in chunks]
        
        self.collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )
        
    def query(self, text: str, top_k: int = 3):
        results = self.collection.query(
            query_texts=[text],
            n_results=top_k
        )
        # Parse output format
        parsed_results = []
        if results and results["documents"]:
            for i in range(len(results["documents"][0])):
                parsed_results.append({
                    "text": results["documents"][0][i],
                    "source": results["metadatas"][0][i].get("source", "unknown"),
                    "hash": results["ids"][0][i]
                })
        return parsed_results
