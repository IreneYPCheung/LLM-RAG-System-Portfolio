from rag_pipeline import load_docs, create_vector_db

print("Testing RAG Pipeline...")
docs = load_docs()
print(f"Loaded {len(docs)} documents.")

print("Creating vector database with HuggingFace embeddings...")
db = create_vector_db(docs)

if db:
    print("Vector DB created successfully.")
else:
    print("Failed to create vector DB.")
