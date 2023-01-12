import tkinter as tk
from tkinter import filedialog
from tkinter import *
from plag import check_plagiarism, extract_text_from_docx


def run_plagiarism_checker():
    global filepath
    plagiarism_ratios = check_plagiarism(filepath)
    result_text = "No plagiarism found"
    urls = ""
    if plagiarism_ratios:
        for online_code, ratio in plagiarism_ratios.items():
            if ratio > 0.8:
                result_text = f"Possible plagiarism found in code: \n{online_code}"
                urls += online_code + "\n"
                break
    result_label.config(text=result_text)
    url_label.config(text=urls)


def upload_document():
    global filepath
    filepath = filedialog.askopenfilename()
    if filepath:
        label_text.set("Selected Document: " + filepath.split("/")[-1])
    else:
        label_text.set("No File Selected")
    return filepath


root = tk.Tk()
root.title("Plagiarism Checker")
root.config(bg="gray")

# Adding widgets to the root window
Label(root, text = 'Plagiarism Checker',
      font =('Verdana', 15)).pack(side = TOP, pady = 10)

root.geometry("350x300")
root.minsize(250, 200)

T = Text(root,bg="white", height=3, width=100, font=('Verdana',12))
text= "This is simple plagiarism checker that checks plagiarism in a document."
T.pack()
T.insert(tk.END, text)

label_text = tk.StringVar()
label_text.set("No File Selected")
label = tk.Label(root, textvariable=label_text)
label.pack()

upload_button = tk.Button(text="Upload Document", command=upload_document)
upload_button.pack()

run_button = tk.Button(text="Run", command=run_plagiarism_checker)
run_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()
url_label = tk.Label(root, text="")
url_label.pack()

root.mainloop()
