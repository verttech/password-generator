import customtkinter as ctk
import secrets
import string
import pyperclip
from tkinter import messagebox 

def update_length(val):
    entry_length.delete(0, "end")
    entry_length.insert(0, str(int(val)))

def generate_password():
    try:
        length = int(entry_length.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid length")
        return

    if length < 9 or length > 128:
        messagebox.showerror("Error", "Length must be between 9 and 128")
        return

    groups = []
    password = []

    if var_uppercase.get():
        groups.append(string.ascii_uppercase)
    if var_lowercase.get():
        groups.append(string.ascii_lowercase)
    if var_numbers.get():
        groups.append(string.digits)
    if var_specials.get():
        groups.append('&^#@!%$*')

    if not groups:
        messagebox.showerror("Error", "Select at least one character group")
        return

    all_chars = ''.join(groups)

    if length <= len(groups):
        password = [secrets.choice(group) for group in groups[:length]]
    else:
        password = [secrets.choice(group) for group in groups]
        for _ in range(length - len(password)):
            password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)

    entry_password.delete("1.0", "end")
    entry_password.insert("1.0", ''.join(password))

def copy_password():
    password = entry_password.get("1.0", "end").strip()
    if password:
        pyperclip.copy(password)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.title("Password Generator")
window.geometry("467x335")
window.resizable(False, False)

window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
pos_x = (screen_width // 2) - (window_width // 2) 
pos_y = (screen_height // 2) - (window_height // 2)
window.geometry(f"+{pos_x}+{pos_y}")

frame = ctk.CTkFrame(master=window, corner_radius=15)
frame.pack(padx=20, pady=20, fill="both", expand=True)

frame.grid_columnconfigure(0, weight=0)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=2)

label_length = ctk.CTkLabel(master=frame, text="Length:", font=("Arial", 16))
label_length.grid(row=0, column=0, padx=5, pady=10, sticky="w")

entry_length = ctk.CTkEntry(master=frame, width=60, font=("Arial", 16))
entry_length.insert(0, "12")
entry_length.grid(row=0, column=1, padx=5, pady=10, sticky="w")

slider_length = ctk.CTkSlider(master=frame, from_=9, to=128, number_of_steps=119, command=update_length)
slider_length.set(12)
slider_length.grid(row=0, column=2, padx=5, pady=10, sticky="we")

var_uppercase = ctk.BooleanVar(value=True)
var_lowercase = ctk.BooleanVar(value=True)
var_numbers = ctk.BooleanVar(value=True)
var_specials = ctk.BooleanVar(value=True)

check_uppercase = ctk.CTkCheckBox(master=frame, text="A-Z", variable=var_uppercase, font=("Arial", 16))
check_uppercase.grid(row=1, column=0, padx=5, pady=5, sticky="w")

check_lowercase = ctk.CTkCheckBox(master=frame, text="a-z", variable=var_lowercase, font=("Arial", 16))
check_lowercase.grid(row=1, column=1, padx=5, pady=5, sticky="w")

check_numbers = ctk.CTkCheckBox(master=frame, text="0-9", variable=var_numbers, font=("Arial", 16))
check_numbers.grid(row=2, column=0, padx=5, pady=5, sticky="w")

check_specials = ctk.CTkCheckBox(master=frame, text="&^#@!%$*", variable=var_specials, font=("Arial", 16))
check_specials.grid(row=2, column=1, padx=5, pady=5, sticky="w")

label_password = ctk.CTkLabel(master=frame, text="Password:", font=("Arial", 16))
label_password.grid(row=3, column=0, padx=5, pady=(10, 0), sticky="w")

entry_password = ctk.CTkTextbox(master=frame, width=400, height=90, font=("Arial", 16))
entry_password.grid(row=4, column=0, padx=5, pady=(0, 10), columnspan=3, sticky="we")

btn_generate = ctk.CTkButton(master=frame, text="Generate", command=generate_password, corner_radius=20, font=("Arial", 16))
btn_generate.grid(row=5, column=0, padx=5, pady=10, sticky="w")

btn_copy = ctk.CTkButton(master=frame, text="Copy", command=copy_password, corner_radius=20, font=("Arial", 16))
btn_copy.grid(row=5, column=2, padx=5, pady=10, sticky="e")

window.mainloop()