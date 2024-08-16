import string
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters_lowercase = list(string.ascii_lowercase)
    letters_uppercase = list(string.ascii_uppercase)
    letters = letters_uppercase + letters_lowercase
    numbers = str(list(range(0, 10)))
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
               "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|', '`', '~']

    rand_letters = random.randint(8, 10)
    rand_num = random.randint(2, 4)
    rand_symbols = random.randint(2, 5)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(rand_letters)]
    password_numbers = [random.choice(numbers) for _ in range(rand_num)]
    password_symbols = [random.choice(symbols) for _ in range(rand_symbols)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    #convert the password list to string
    password = "".join(password_list)

    #insert it into the entry
    pyperclip.copy(password)# you don't have to copy your password manually. Password copied once you click "Generate Password"
    password_entry.insert(0, password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

#Label
website_label = Label(text="Website:")
username = Label(text="Username/Email:")
password = Label(text="Password:")

#Makes the label visible in the grids we specify
website_label.grid(column=0, row=1)
username.grid(column=0, row=2)
password.grid(column=0, row=3)

#Entry
website_entry = Entry(width=53, bd=5)
username_entry = Entry(width=53, bd=5)
password_entry = Entry(width=34, bd=5)

website_entry.grid(column=1, row=1, columnspan=2)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

#Focus cursor on the first entry i.e website_entry
website_entry.focus()
username_entry.insert(0, "email123@gmail.com")


# ---------------------------- SAVE PASSWORD -------------------------------
def save_credentials():
    if website_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "":
        messagebox.showwarning(title="ERROR!", message="Don't leave any of the fields empty!")

    else:
        is_okay = messagebox.askyesnocancel(title=website_entry.get(), message=f"These are the details that you have"
                                                                               f" \nEmail: {username_entry.get()} \nPassword: {password_entry.get()} \nSave Credentials?")
        if is_okay:
            with open("data.txt", mode="a") as file:  #.get() fetches the entry
                file.write(f"{website_entry.get()}  | {username_entry.get()}  | {password_entry.get()} \n")
                website_entry.delete(0, END)  #to keep the entries clean after saving
                password_entry.delete(0, END)


#Buttons
generate = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=46, command=save_credentials)

generate.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
