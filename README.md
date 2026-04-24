\# 🧠 RAG-Powered Document Q\&A System



An AI-powered application that lets you upload any document (PDF, DOCX, TXT) or enter a URL and ask questions about it using natural language.



\## 🚀 Live Demo

\[Click here to try the app](https://shravani-rag-system.streamlit.app/)



\## 🛠️ Tech Stack

\- \*\*LangChain\*\* — RAG pipeline and prompt orchestration

\- \*\*Gemini Embeddings\*\* — Document vectorization

\- \*\*FAISS\*\* — Local vector database for semantic search

\- \*\*Groq + LLaMA 3\*\* — Fast LLM inference for answer generation

\- \*\*Streamlit\*\* — Interactive web UI



\## ⚙️ How It Works

1\. Upload a PDF, DOCX, TXT file or enter a URL

2\. Document is split into chunks and converted into vector embeddings

3\. User question is matched against relevant chunks using semantic search

4\. Retrieved context is passed to LLaMA 3 to generate a precise answer



\## 📦 Installation



```bash

git clone https://github.com/Shravani-Desai/rag-qa-system.git

cd rag-qa-system

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

```



\## 🔑 Environment Variables

Create a `.env` file in the root directory:

GOOGLE_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key

## ▶️ Run Locally
```bash
streamlit run app.py
```

## 📁 Project Structure
rag-qa-system/
├── app.py                # Streamlit UI
├── rag_engine.py         # RAG pipeline logic
├── document_loader.py    # File and URL parsing
├── requirements.txt      # Dependencies
└── .env                  # API keys (not committed)

## 🙋‍♀️ Author
**Shravani Desai** — [LinkedIn](https://www.linkedin.com/in/shravani-desai-153702337/) | [GitHub](https://github.com/Shravani-Desai)



