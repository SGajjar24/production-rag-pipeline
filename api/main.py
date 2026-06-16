from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Grounded RAG Engine API", 
    description="FastAPI gateway for document intelligence and grounding audit", 
    version="1.0.0"
)

app.include_router(router)
