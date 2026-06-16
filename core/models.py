from google import genai
from core.config import settings

class LLMClient:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        # self.client = genai.Client(api_key=self.api_key)
        
    def generate_grounded_answer(self, context_str: str, query: str) -> str:
        prompt = f"""You are a high-reliability technical assistant. Answer the user query using ONLY the provided verified context.
Every factual assertion must include a bracketed citation pointing to the Source name and Hash.
If the context does not contain the answer, say "I cannot answer this based on the provided documents."

CONTEXT:
{context_str}

QUERY:
{query}

ANSWER:"""
        
        if not self.api_key or self.api_key == "mock":
            return "MIL-STD-130N requires all military parts marking to have a machine-readable 2D Data Matrix [Source: mil-std-130n.pdf | Hash: a4d3f1e9c2b8], which must remain legible under chemical exposure [Source: mil-std-130n.pdf | Hash: f2e8d4c9b1a7]."
        
        # client = genai.Client(api_key=self.api_key)
        # response = client.models.generate_content(
        #     model="gemini-2.5-flash",
        #     contents=prompt
        # )
        # return response.text
        return "Grounded response mock placeholder."
