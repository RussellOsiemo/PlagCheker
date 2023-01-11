import tkinter as tk
from tkinter import filedialog

def upload_document():
    filepath = filedialog.askopenfilename()
    # you can use the filepath to open the file and read the text
    print(filepath)

def run_plagiarism_checker():
    # code to run the plagiarism checker
    print("Plagiarism checker running...")

root = tk.Tk()
root.title("Plagiarism Checker")

upload_button = tk.Button(root, text="Upload Document", command=upload_document)
upload_button.pack()

run_button = tk.Button(root, text="Run Checker", command=run_plagiarism_checker)
run_button.pack()

root.mainloop()