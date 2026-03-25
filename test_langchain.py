from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import sys

load_dotenv()

try:
    # Try the simplest configuration
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GEMINI_API_KEY"))
    result = llm.invoke("Respond with the word: Success")
    print("Langchain Test Succeeded:", result.content)
except Exception as e:
    print(f"Langchain Test Failed: {e}")
