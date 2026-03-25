import os
import google.generativeai as genai
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    print("Warning: GEMINI_API_KEY not set in environment variables.")

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def load_docs(file_path="data/sample.txt"):
    """Loads text documents from the specified file path."""
    try:
        loader = TextLoader(file_path, encoding="utf-8")
        return loader.load()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []

def create_vector_db(docs):
    """Creates a FAISS vector database using HuggingFace embeddings."""
    if not docs:
        return None
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.from_documents(docs, embeddings)
    return db

def query_rag(db, question):
    """Queries the vector database and uses Gemini to generate a response."""
    if not db:
        return "Error: Vector database could not be initialized."
    if not api_key:
        return "Error: GEMINI_API_KEY is missing. Please set it in your .env file."

    docs = db.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are an AI assistant. Answer based only on the context provided.
    
    Context:
    {context}

    Question:
    {question}
    """

    try:
        models_to_try = [
            "gemini-2.5-flash",
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-1.5-pro",
            "gemini-1.0-pro"
        ]
        
        errors = []
        for model_name in models_to_try:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(prompt)
                return response.text
            except Exception as e:
                errors.append(f"- {model_name}: {e}")
                continue
                
        error_msg = "\n".join(errors)
        return f"Error connecting to models. Details:\n{error_msg}"
    except Exception as e:
        return f"Unexpected Error: {e}"
