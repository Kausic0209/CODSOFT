#for gui
import tkinter as tk

#for random selecting feature
import random

def password_generator():
    ##characters that we want in our password
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+><?|0123456789abcdefghijklmnopqrstuvwxyz"
    #length of password
    length = int(length_entry.get())
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    password_var.set(password)

# for Create the main window
root = tk.Tk()
#title of password generator
root.title(" My Random Password Generator")
#for geometrical size 
root.geometry("400x250")
root.configure(bg="#f0f0f0")

# for Creating pack widgets
title_label = tk.Label(root, text="My Random Password Generator", font=("Arial", 20), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

length_frame = tk.Frame(root, bg="#f0f0f0")
length_frame.pack()

length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 14), bg="#f0f0f0", fg="#333")
length_label.pack(side=tk.LEFT, padx=5)

length_entry = tk.Entry(length_frame, bd=2, font=("Arial", 14))
length_entry.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(root, text="Generate Password", command=password_generator, bg="#4CAF50", fg="#fff", bd=2, font=("Arial", 12))
generate_button.pack(pady=10)

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Arial", 12), bg="#f0f0f0", fg="#333")
password_label.pack()

# for Runing the main event loop
root.mainloop()
#THANK YOU.