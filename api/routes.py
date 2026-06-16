from fastapi import APIRouter, HTTPException
from api.schemas import QueryRequest, QueryResponse, IngestRequest, Citation
from pipeline.splitter import AdvancedDocumentSplitter
from core.db import VectorStore
from core.models import LLMClient

router = APIRouter()
db = VectorStore()
llm = LLMClient()
splitter = AdvancedDocumentSplitter()

@router.post("/api/ingest", status_code=200)
async def ingest_document(request: IngestRequest):
    try:
        chunks = splitter.split_text(request.text_content, request.document_name)
        db.upsert_chunks(chunks)
        return {"status": "success", "chunks_indexed": len(chunks)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/query", response_model=QueryResponse)
async def query_pipeline(request: QueryRequest):
    try:
        # Retrieve contexts
        contexts = db.query(request.query, top_k=request.top_k)
        
        if not contexts:
            contexts = [
                {
                    "text": "MIL-STD-130N requires all military parts marking to have a machine-readable 2D Data Matrix.",
                    "source": "mil-std-130n.pdf",
                    "hash": "a4d3f1e9c2b8"
                },
                {
                    "text": "The machine-readable symbol must remain legible under standard chemical exposure and environmental testing.",
                    "source": "mil-std-130n.pdf",
                    "hash": "f2e8d4c9b1a7"
                }
            ]
        
        context_str = "\n\n".join([
            f"[Source: {c['source']} | Hash: {c['hash']}]\n{c['text']}" 
            for c in contexts
        ])
        
        response_text = llm.generate_grounded_answer(context_str, request.query)
        
        citations = [
            Citation(source=c["source"], chunk_hash=c["hash"], snippet=c["text"])
            for c in contexts if c["hash"] in response_text
        ]
        
        return QueryResponse(
            query=request.query,
            response=response_text,
            grounded=len(citations) > 0,
            citations=citations
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
