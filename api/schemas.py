from pydantic import BaseModel, Field
from typing import List

class QueryRequest(BaseModel):
    query: str = Field(..., example="What are the compliance rules for MIL-STD-130N?")
    top_k: int = Field(default=3, ge=1, le=10)

class IngestRequest(BaseModel):
    document_name: str
    text_content: str

class Citation(BaseModel):
    source: str
    chunk_hash: str
    snippet: str

class QueryResponse(BaseModel):
    query: str
    response: str
    grounded: bool
    citations: List[Citation]
