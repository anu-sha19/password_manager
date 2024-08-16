import string
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


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
    pyperclip.copy(
        password)  # you don't have to copy your password manually. Password copied once you click "Generate Password"
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
website_entry = Entry(width=34, bd=5)
username_entry = Entry(width=53, bd=5)
password_entry = Entry(width=34, bd=5)

website_entry.grid(column=1, row=1)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

#Focus cursor on the first entry i.e website_entry
website_entry.focus()
username_entry.insert(0, "email123@gmail.com")


# ---------------------------- SAVE PASSWORD -------------------------------
def save_credentials():
    website = website_entry.get()  #.get() fetches the entry
    email = username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="ERROR!", message="Don't leave any of the fields empty!")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)  #Reading old data

        except FileNotFoundError:  #if there is no such file
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)  # updating old data with new data
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)  #saving updated data

        finally:
            website_entry.delete(0, END)  #to keep the entries clean after saving
            password_entry.delete(0, END)


def search_credentials():
    website = website_entry.get().title()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Website Credentials",
                            message="No data file found")
    else:
        if website in data:
            email = (data[website]["email"])
            password = (data[website]["password"])

            messagebox.showinfo(title="Website Credentials",
                                message=f"Your Credentials for {website}:\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Website Credentials",
                                message=f"{website} not found in database!")


#Buttons
generate = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=46, command=save_credentials)
search_button = Button(text="Search", width=15, command=search_credentials)

generate.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=2, row=1)

window.mainloop()
