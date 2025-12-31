from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

def gemini():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7
    )