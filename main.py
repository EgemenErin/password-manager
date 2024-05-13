from tkinter import *
from tkinter import messagebox as mb
import pandas as pd
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    website_entry.delete(0, END)
    email = email_entry.get()
    email_entry.delete(0, END)
    password = password_entry.get()
    password_entry.delete(0, END)

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
email_entry.insert(0,"egemenders@hotmail.com")

password= Label(text="Password:  ", font=("Arial"))
password.grid(column=0, row=3)
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

passbutton = Button(text="Generate Password", width=14)
passbutton.grid(column=2,row=3)

addbutton = Button(text="Add", width=32, command=save)
addbutton.grid(column=1,row=4,columnspan=2)

window.mainloop()