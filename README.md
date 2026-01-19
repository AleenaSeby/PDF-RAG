# PDF_RAG

Simple local RAG (Retrieval-Augmented Generation) demo using:
- LLM: ChatGroq (llama-3.3-70b-versatile)
- Embeddings: HuggingFaceEmbeddings
- Vector store: Chroma (persisted in ./doc_vectorstore)
- UI: Streamlit

## How it works
1. Upload a PDF via the Streamlit app (app.py).
2. rag_utility.process_document_to_chroma_db:
   - Loads PDF, splits into chunks, computes embeddings, and persists a Chroma DB at ./doc_vectorstore.
3. rag_utility.answer_question:
   - Loads persisted Chroma, creates a retriever, runs RetrievalQA with ChatGroq, returns answer.

## Why
- Enables question-answering over document contents by combining vector search with a capable LLM (RAG).
- Persists vectors so documents are searchable across sessions.

## Quick setup (Windows recommended)
1. Create short-path virtualenv to avoid long-path errors:
   powershell
   python -m venv C:\venv\pdf_rag
   C:\venv\pdf_rag\Scripts\Activate.ps1

2. Upgrade pip and install requirements:
   powershell
   python -m pip install --upgrade pip setuptools wheel
   python -m pip install --no-cache-dir -r "path\requirements.txt"

3. Ensure .env contains GROQ_API_KEY (do not commit .env).

## Run
powershell
python -m streamlit run "path\app.py"

## Usage
- Upload a PDF in the web UI.
- Wait for "Document Processed Successfully".
- Enter a question and click "Answer".
- Responses come from the LLM informed by retrieved document chunks.

## Files
- app.py — Streamlit UI and file upload handling.
- rag_utility.py — PDF loading, splitting, embedding, Chroma persistence, and QA.
- requirements.txt — Python deps.
- .env — API key(s) (GROQ_API_KEY).
- doc_vectorstore/ — persisted Chroma DB (chroma.sqlite3 + data folders).


## Notes & troubleshooting
- Vector store is global by default (./doc_vectorstore). Repeated uploads append/merge; to avoid duplicates, use per-file subfolders or delete the folder before processing.
- If you hit WinError 206 (path 

https://github.com/user-attachments/assets/7c28ff9a-e35d-4ff0-9445-32bc361ec4e0

too long), use a venv at a short path (C:\venv\...) or enable long paths in Windows registry (requires admin + reboot).
- If streamlit CLI not found, run via `python -m streamlit run app.py`.
- Keep your GROQ API key secret.

## Demo Video
