import streamlit as st
from rag_pipeline import load_docs, create_vector_db, query_rag

st.set_page_config(page_title="Free RAG Assistant", layout="centered")

st.title("Free Enterprise RAG Knowledge Assistant")
st.markdown("A 100% Free Retrieval-Augmented Generation (RAG) system using open-source embeddings and Google Gemini API.")

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
            st.info(answer)

st.divider()
st.caption("Powered by Streamlit, FAISS, HuggingFace, and Google Gemini.")
