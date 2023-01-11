import tkinter as tk
from tkinter import *
from tkinter import filedialog
from docx import Document

def upload_document():
    filepath = filedialog.askopenfilename()
    # you can use the filepath to open the file and read the text
    print(filepath)

def run_plagiarism_checker():
    # code to run the plagiarism checker
    print("Plagiarism checker running...")

root = tk.Tk()
root.title("Plagiarism Checker")
root.config(bg="gray")
# Adding widgets to the root window
Label(root, text = 'Plagiarism Checker',
      font =('Verdana', 15)).pack(side = TOP, pady = 10)
      # specify size of window.
root.geometry("350x300")
# setting the minimum size of the root window
root.minsize(250, 200)
# text 
T = Text(root,bg="white", height=3, width=100, font=('Verdana',12))
text= "This is simple plagiarism checker that checks plagiarism in a document."
T.pack()
# insert the text 
T.insert(tk.END, text)
upload_button = tk.Button(root, text="Upload Document", command=upload_document)
upload_button.pack()

run_button = tk.Button(root, text="Run Checker", command=run_plagiarism_checker)
run_button.pack()

root.mainloop()



def extract_text_from_docx(filepath):
    # Open the Word document
    doc = Document(filepath)
    # Extract the text from the document
    text = [para.text for para in doc.paragraphs]
    #Join the text and return as string
    return '\n'.join(text)

def run_plagiarism_checker():
    filepath = upload_document()
    if filepath:
        # Use the extract_text_from_docx to extract the text from uploaded docx file
        text = extract_text_from_docx(filepath)
        # Do the plagiarism checking here
        print(text)