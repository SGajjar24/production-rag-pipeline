import os

class Settings:
    PROJECT_NAME: str = "Grounded RAG Pipeline"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    CHROMA_DB_PATH: str = os.getenv("CHROMA_DB_PATH", "./chroma_db")

settings = Settings()
