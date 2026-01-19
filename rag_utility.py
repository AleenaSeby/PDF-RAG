import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA

load_dotenv()

working_dir = Path(__file__).parent.resolve()

embedding = HuggingFaceEmbeddings()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def process_document_to_chroma_db(file_name):
    pdf_path = working_dir / file_name

    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )

    texts = text_splitter.split_documents(documents)

    Chroma.from_documents(
        documents=texts,
        embedding=embedding,
        persist_directory=str(working_dir / "doc_vectorstore")
    )

    return True


def answer_question(user_question):
    vectordb = Chroma(
        persist_directory=str(working_dir / "doc_vectorstore"),
        embedding_function=embedding
    )

    retriever = vectordb.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
    )

    response = qa_chain.invoke({"query": user_question})
    return response["result"]
