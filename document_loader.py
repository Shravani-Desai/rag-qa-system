import os
import requests
from bs4 import BeautifulSoup
import fitz  # PyMuPDF
from docx import Document


def load_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


def load_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])


def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_url(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup.get_text(separator="\n")


def load_document(source, source_type="file"):
    if source_type == "url":
        return load_url(source)
    
    ext = os.path.splitext(source)[1].lower()
    if ext == ".pdf":
        return load_pdf(source)
    elif ext == ".docx":
        return load_docx(source)
    elif ext == ".txt":
        return load_txt(source)
    else:
        raise ValueError(f"Unsupported file type: {ext}")