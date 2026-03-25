import streamlit as st
from rag_pipeline import load_docs, create_vector_db, query_rag

st.set_page_config(page_title="Enterprise RAG Assistant", page_icon="🏢", layout="wide")

with st.sidebar:
    st.header("⚙️ Core Architecture")
    st.markdown("""
    This application demonstrates a production-grade **Retrieval-Augmented Generation (RAG)** pipeline optimized for contextual querying.
    """)
    st.markdown("---")
    st.caption("**Key Components**:\n * **Frontend:** Streamlit\n * **Vector DB:** FAISS CPU\n * **Embeddings:** HuggingFace `sentence-transformers`\n * **LLM Engine:** Google Gemini AI")

st.title("🏢 Enterprise Knowledge Assistant")
st.markdown("A robust AI assistant integrating semantic document retrieval to provide highly accurate, domain-specific answers.")

@st.cache_resource
def setup():
    docs = load_docs()
    db = create_vector_db(docs)
    return db

db = setup()

query = st.text_input("Ask a question about textiles and fibers:")

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
