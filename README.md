# Enterprise RAG Knowledge Assistant

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-url.streamlit.app)

## Overview
This project implements a fully **FREE** Retrieval-Augmented Generation (RAG) system using open-source embeddings and Google Gemini API. 

It enables users to query domain-specific knowledge with accurate, context-aware responses without incurring any API or hosting costs.

## Architecture
`User Query` → `FAISS Retrieval` → `Context Injection` → `Gemini LLM` → `Response`

## Tech Stack
- **Python** (Core language)
- **Streamlit** (Frontend UI)
- **FAISS** (Vector Database locally via CPU)
- **HuggingFace Embeddings** (FREE sentence-transformers)
- **Google Gemini** (FREE LLM API tier)

## Key Features
- **100% free AI stack**
- **Semantic document retrieval**
- Context-aware LLM responses
- Lightweight and deployable

## Use Case
- Enterprise knowledge assistant
- Research document Q&A
- Domain-specific chatbot

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd project-1-rag-system
```

### 2. Set up a Virtual Environment (Highly Recommended)
Creating a virtual environment isolates project dependencies from your system.
```bash
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Packages
```bash
pip install -r requirements.txt
```

### 4. Create an API Key & Configure Environment
1. Go to Google AI Studio: [https://aistudio.google.com](https://aistudio.google.com)
2. Click **Get API Key** and copy your key.
3. Rename `.env.example` to `.env`.
4. Add your API key to `.env`:
```
GEMINI_API_KEY="your_key"
```

### 5. Run the Application
```bash
streamlit run app.py
```

## Future Improvements
- PDF ingestion capabilities
- Multi-document folder support
- Persistent database implementation
- API deployment via FastAPI

## Author
**Irene Cheung, PhD, SMIEEE**  
AI Leader | Machine Learning • LLM • AI Agents • Computer Vision
