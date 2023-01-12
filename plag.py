import requests
import difflib
from bs4 import BeautifulSoup
from docx import Document

def extract_text_from_docx(filepath):
    doc = Document(filepath)
    text = [para.text for para in doc.paragraphs]
    return '\n'.join(text)

def search_documents(text):
    """Searches for documents online and returns a list of matching documents"""
    search_url = f"https://www.google.com/search?q={text}&btnI"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    documents = []
    for document in soup.find_all("cite"):
        documents.append(document.text)
    return documents

def check_plagiarism(filepath):
    """Compares a given document to online documents and returns a dictionary of plagiarism ratios"""
    text = extract_text_from_docx(filepath)
    online_documents = search_documents(text)
    plagiarism_ratios = {}
    for online_document in online_documents:
        response = requests.get(online_document)
        soup = BeautifulSoup(response.text, 'html.parser')
        online_text = soup.get_text()
        plagiarism_ratio = difflib.SequenceMatcher(None, text, online_text).ratio()
        plagiarism_ratios[online_document] = plagiarism_ratio
    return plagiarism_ratios
