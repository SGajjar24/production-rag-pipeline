import hashlib
import re
from typing import Dict, List, Any

class AdvancedDocumentSplitter:
    def __init__(self, chunk_size: int = 800, chunk_overlap: int = 100):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str, document_name: str) -> List[Dict[str, Any]]:
        # Normalize whitespace
        clean_text = re.sub(r"\s+", " ", text).strip()
        
        # Split into rough sentence chunks
        sentences = re.split(r"(?<=[\.!\?])\s+", clean_text)
        
        chunks = []
        current_chunk = []
        current_length = 0
        
        for sentence in sentences:
            sentence_len = len(sentence)
            if current_length + sentence_len > self.chunk_size:
                chunk_content = " ".join(current_chunk)
                chunk_hash = hashlib.sha256(chunk_content.encode("utf-8")).hexdigest()
                
                chunks.append({
                    "text": chunk_content,
                    "metadata": {
                        "source": document_name,
                        "hash": chunk_hash[:12],
                        "length": len(chunk_content)
                    }
                })
                
                # Overlap logic
                overlap_len = 0
                new_chunk = []
                for s in reversed(current_chunk):
                    if overlap_len + len(s) < self.chunk_overlap:
                        new_chunk.insert(0, s)
                        overlap_len += len(s)
                    else:
                        break
                current_chunk = new_chunk
                current_length = overlap_len
            
            current_chunk.append(sentence)
            current_length += sentence_len
            
        if current_chunk:
            chunk_content = " ".join(current_chunk)
            chunk_hash = hashlib.sha256(chunk_content.encode("utf-8")).hexdigest()
            chunks.append({
                "text": chunk_content,
                "metadata": {
                    "source": document_name,
                    "hash": chunk_hash[:12],
                    "length": len(chunk_content)
                }
            })
            
        return chunks
