import os
from dotenv import load_dotenv
from rag_pipeline import load_docs, create_vector_db, query_rag

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key or api_key == "your_api_key_here":
    print("API Key not set correctly in .env.")
else:
    print("API Key detected!")
    docs = load_docs()
    db = create_vector_db(docs)
    print("Asking Gemini: What is cotton?")
    # Silence the huggingface token warning by setting env var if not set
    os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
    try:
        answer = query_rag(db, "What is cotton?")
        print("\n=== Gemini Response ===")
        print(answer)
        print("=======================\n")
        print("Verification Successful!")
    except Exception as e:
        print(f"Error communicating with Gemini: {e}")
