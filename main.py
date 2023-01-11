import os
# from ui import run_plagiarism_checker
# import ui
import requests 
from bs4 import BeautifulSoup


#  some urls to websites 
urls = [
    "https://www.data.gov/",
    "https://data.gov.uk/",
    "https://data.gov.au/",
    "https://www.jstor.org/",
    "https://muse.jhu.edu/",
    "https://doaj.org/",
    "https://www.nih.gov/",
    "https://www.who.int/",
    "https://scholar.google.com/"
]

def get_document_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        text = soup.get_text()
        return title, text
    else:
        print(f"Failed to access {url}. Status code: {response.status_code}")

def search_documents(urls):
    documents = {}
    for url in urls:
        title, text = get_document_text(url)
        if title and text:
            documents[title] = [url, title, text]
    return documents

urls = [
    "https://www.data.gov/",
    "https://data.gov.uk/",
    "https://data.gov.au/",
    "https://www.jstor.org/",
    "https://muse.jhu.edu/",
    "https://doaj.org/",
    "https://www.nih.gov/",
    "https://www.who.int/",
     "https://scholar.google.com/"
]

documents = search_documents(urls)
print(documents)


