from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def gemini(
        model: str = "gemini-2.5-flash", 
        temperature: float = 0.7,
        max_tokens: float = None
    ) -> ChatGoogleGenerativeAI:

    return ChatGoogleGenerativeAI(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens
    )