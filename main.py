from tkinter import *
from tkinter import messagebox as mb, messagebox
import pandas as pd
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    website_entry.delete(0, END)
    email = email_entry.get()
    password = password_entry.get()
    password_entry.delete(0, END)
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        mb.showerror("Error", "You left some fields empty.")
    mb.askokcancel(title="Save",
                   message=f"These are the details you have entered,\nEmail: {email}\nPassword: {password}\nWebsite: {website}\nWould you like to save?")

    new_data = pd.DataFrame({
        'Website': [website],
        'Email': [email],
        'Password': [password]
    })
    try:
        df = pd.read_csv('accounts.csv')
        df = pd.concat([df, new_data])
    except FileNotFoundError:
        df = new_data  # If the file doesn't exist, create a new DataFrame

    df.to_csv('accounts.csv', index=False)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(140, 100, image=logo_img)
canvas.grid(column=1, row=0)

website= Label(text="Website:  ", font=("Arial"))
website.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email=Label(text="Email:  ", font=("Arial"))
email.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"example@gmail.com")

password= Label(text="Password:  ", font=("Arial"))
password.grid(column=0, row=3)
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

passbutton = Button(text="Generate Password", width=14)
passbutton.grid(column=2,row=3)

addbutton = Button(text="Add", width=32, command=save)
addbutton.grid(column=1,row=4,columnspan=2)

window.mainloop()
