import tkinter as tk
from tkinter import filedialog
from tkinter import *
from docx import Document

filepath = ''

def upload_document():
    global filepath
    filepath = filedialog.askopenfilename()
    if filepath:
        label_text.set("Selected Document: " + filepath.split("/")[-1])
    else:
        label_text.set("No File Selected")
    return filepath

def run_plagiarism_checker():
    global filepath
    if filepath:
        doc = Document(filepath)
        text = [para.text for para in doc.paragraphs]
        # here you can also extract details like author, title, date created, last modification etc
        author = doc.core_properties.author
        title = doc.core_properties.title
        created = doc.core_properties.created
        modified = doc.core_properties.modified
        print("author: ",author)
        print("title: ",title)
        print("created: ",created)
        print("modified: ",modified)
        print("text: ", '\n'.join(text))
        print(text)
    else:
        print("No file selected")

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

label_text = tk.StringVar()
label_text.set("No File Selected")
label = tk.Label(root, textvariable=label_text)
label.pack()

upload_button = tk.Button(text="Upload Document", command=upload_document)
upload_button.pack()

run_button = tk.Button(text="Run", command=run_plagiarism_checker)
run_button.pack()

root.mainloop()