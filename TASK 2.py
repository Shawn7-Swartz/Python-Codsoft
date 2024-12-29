#GENRATE PASSWORD 

import tkinter as tk
from tkinter import messagebox
import random
import string

def gen():
    length = int(password_length.get())  
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    pass_entry.delete(0, tk.END)  
    pass_entry.insert(tk.END, password)
def copy(): 
    root.clipboard_clear()
    root.clipboard_append(pass_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)
password_length = tk.Entry(root, width=10)
password_length.pack()
gen_button = tk.Button(root, text="Generate Password", command=gen)
gen_button.pack(pady=10)
pass_entry = tk.Entry(root, width=50)
pass_entry.pack(pady=10)
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy)
copy_button.pack(pady=10)
root.mainloop()
