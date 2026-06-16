# Production-Grade Grounded RAG Pipeline

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-green.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg)](https://fastapi.tiangolo.com)
[![VectorDB](https://img.shields.io/badge/VectorDB-Chroma-orange.svg)](https://github.com/chroma-core/chroma)
[![LLM](https://img.shields.io/badge/LLM-Gemini_2.5_Flash-00D9FF.svg)](https://ai.google.dev/)

An enterprise-grade, asynchronous Retrieval-Augmented Generation (RAG) pipeline designed for zero-hallucination document Q&A. Every generated assertion is traceably grounded in source passages with exact page and paragraph citations.

## 🚀 Key Features
*   **Semantic & Recursive Splitting**: Layout-aware chunking preserving paragraph boundaries and adding unique source hashes.
*   **Dense & Sparse Retrieval**: Reciprocal Rank Fusion (RRF) combining vector search with lexical BM25 matching.
*   **LLM-in-the-Loop Grounding**: Prompt engineering templates forcing strict context verification.
*   **Asynchronous FastAPI**: Production endpoints for document ingestion, querying, and verification metrics.
*   **Dockerized**: Containerized deployment layout ready for orchestration.

## 📁 Project Structure
```
production-rag-pipeline/
├── api/
│   ├── main.py             # FastAPI App Bootstrapper
│   ├── routes.py           # Ingestion and Query Endpoints
│   └── schemas.py          # Request/Response validation
├── core/
│   ├── config.py           # Configuration manager
│   ├── db.py               # ChromaDB client connector
│   └── models.py           # Gemini 2.5 Flash SDK interface
├── pipeline/
│   └── splitter.py         # Advanced chunking logic
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🛠️ Quick Start
1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the FastAPI server:
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000
   ```
