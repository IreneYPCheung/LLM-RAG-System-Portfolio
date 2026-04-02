import os
import tempfile
import streamlit as st
from rag_pipeline import load_docs, create_vector_db, query_rag

st.set_page_config(page_title="Enterprise RAG Assistant", page_icon="🏢", layout="wide")

# Hide all Streamlit branding and default headers/footers
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Core Architecture")
    st.markdown("""
    This application demonstrates a production-grade **Retrieval-Augmented Generation (RAG)** pipeline optimized for contextual querying.
    """)
    st.markdown("---")
    st.caption("**Key Components**:\n * **Frontend:** Streamlit\n * **Vector DB:** FAISS CPU\n * **Embeddings:** HuggingFace `sentence-transformers`\n * **LLM Engine:** Google Gemini AI")
    
    st.markdown("---")
    st.header("📄 Custom Knowledge Base")
    uploaded_file = st.file_uploader("Upload your own PDF or TXT to query against:", type=["txt", "pdf"])

st.title("🏢 Enterprise Knowledge Assistant")
st.markdown("A robust AI assistant integrating semantic document retrieval to provide highly accurate, domain-specific answers.")

@st.cache_resource
def setup_default():
    docs = load_docs()
    db = create_vector_db(docs)
    return db

db = None
if uploaded_file is not None:
    # Save uploaded file to a temporary file so Langchain can process it
    with st.spinner("Processing document..."):
        # Extract extension
        ext = uploaded_file.name.split('.')[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{ext}") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name
        
        docs = load_docs(tmp_file_path)
        db = create_vector_db(docs)
        
        # Cleanup
        try:
            os.remove(tmp_file_path)
        except Exception:
            pass
        st.sidebar.success("Document mapped to Vector DB!")
else:
    db = setup_default()

query = st.text_input("Ask a question about the knowledge base:")

if query:
    if not db:
        st.error("Failed to load knowledge base. Please check if `data/sample.txt` exists.")
    else:
        with st.spinner("Analyzing..."):
            answer = query_rag(db, query)
            st.markdown("### Answer")
            
            # Professional Error Handling
            if "Error connecting to models" in answer:
                st.error("⚠️ The AI failed to connect. This is typically due to Google's API geo-blocking your region (EU/Austria VPNs often face restrictions on the Free Tier).")
                with st.expander("View Technical Details"):
                    st.code(answer)
            else:
                st.info(answer)

st.divider()
st.caption("Powered by Streamlit, FAISS, HuggingFace, and Google Gemini.")
