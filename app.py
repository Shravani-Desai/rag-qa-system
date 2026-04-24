import streamlit as st
import tempfile
import os
from document_loader import load_document
from rag_engine import build_vector_store, get_qa_chain

st.set_page_config(page_title="RAG Q&A System", page_icon="🧠", layout="wide")
st.title("🧠 RAG-Powered Document Q&A")
st.markdown("Upload a PDF, DOCX, TXT file or enter a URL — then ask anything about it!")

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.header("📂 Load Your Document")
    input_type = st.radio("Input type:", ["Upload File", "Enter URL"])

    if input_type == "Upload File":
        uploaded_file = st.file_uploader(
            "Upload PDF, DOCX, or TXT",
            type=["pdf", "docx", "txt"]
        )
        if uploaded_file and st.button("Process Document"):
            with st.spinner("Reading and indexing document..."):
                suffix = os.path.splitext(uploaded_file.name)[1]
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name
                text = load_document(tmp_path)
                vector_store = build_vector_store(text)
                st.session_state.qa_chain = get_qa_chain(vector_store)
                st.session_state.chat_history = []
                st.success("✅ Document ready! Ask your questions.")

    else:
        url = st.text_input("Enter a URL:")
        if url and st.button("Process URL"):
            with st.spinner("Fetching and indexing webpage..."):
                text = load_document(url, source_type="url")
                vector_store = build_vector_store(text)
                st.session_state.qa_chain = get_qa_chain(vector_store)
                st.session_state.chat_history = []
                st.success("✅ Webpage ready! Ask your questions.")

if st.session_state.qa_chain:
    st.markdown("---")
    st.subheader("💬 Ask a Question")

    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(chat["question"])
        with st.chat_message("assistant"):
            st.write(chat["answer"])

    question = st.chat_input("Ask something about your document...")
    if question:
        with st.spinner("Thinking..."):
            answer = st.session_state.qa_chain.invoke(question)
            st.session_state.chat_history.append({
                "question": question,
                "answer": answer
            })
            st.rerun()
else:
    st.info("👈 Upload a document or enter a URL in the sidebar to get started!")