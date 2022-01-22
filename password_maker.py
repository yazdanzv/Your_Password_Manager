from tkinter import *
from  tkinter import messagebox
from random import shuffle,choice,randint
from json import dump,load
import json
import pyperclip



COMMON_EMAIL = "yazdanzv.1378@gmail.com"
BLUE = "#676FA3"
LIGHT_BLUE = "#CDDEFF"
FILE_NAME = "PASSWORDS.json"


#----------------------------- Functions -------------------------------------

def generate_button_clicked():


    password = generate_pass()
    global pass_entry
    if len(pass_entry.get()) == 0:
        pass_entry.insert(END, password)
    else:
        pass_entry.delete(0,END)
        pass_entry.insert(END, password)

    # To copy the password automatically
    pyperclip.copy(password)

def add_button_clicked():


    global web_entry,pass_entry,email_entry

    data = {web_entry.get() : {"Email":email_entry.get(),"Password":pass_entry.get(),}}

    if len(web_entry.get()) != 0 and len(email_entry.get()) != 0 and len(pass_entry.get()) != 0:
        is_ok = messagebox.askokcancel(title=web_entry.get(), message=f"Website/username : {web_entry.get()}\n"
                                                                      f"Email : {email_entry.get()}\n"
                                                                      f"Password : {pass_entry.get()}\n"
                                                                      f"Is it ok to save ?")
        if is_ok:
            try:

                with open(FILE_NAME,'r') as f:
                    info = f.readlines()
                    if len(info) != 0:
                        with open(FILE_NAME, "r") as f:
                            old_data = load(f)
                            print(old_data)
                            old_data.update(data)
                        with open(FILE_NAME, "w") as f:
                            dump(old_data, f, indent=4)
                    else:
                        with open(FILE_NAME,'w') as f:
                            dump(data,f,indent=4)

            except FileNotFoundError:

                with open(FILE_NAME, "w") as f:
                    dump(data, f, indent=4)

            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)
    else:
        messagebox.showerror(title="ERROR",message="YOU DIDN'T FILL ALL THE BOXES !!!")

def search_button_clicked():

    global web_entry

    with open(FILE_NAME,'r') as f:
        n = len(f.readlines())

    if n != 0:
        if len(web_entry.get()) > 0:
            try:
                with open(FILE_NAME, "r") as f:
                    data = load(f)
                    password = data[web_entry.get()]["Password"]
                    email = data[web_entry.get()]["Email"]
                    messagebox.showinfo(title="Your Info", message=f"Email : {email}\n"
                                                                   f"Password : {password}\n")
            except FileNotFoundError:
                messagebox.showerror(title="ERROR", message="File not found !")
        else:
            messagebox.showerror(title="ERROR", message="No web/username entered !")
    else:
        messagebox.showerror(title="ERROR",message="File is empty !")



def generate_pass():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    return password

#---------------------------- Design the UI ----------------------------------

window = Tk()
window.title("Password Maker")
window.config(padx=50,pady=50,bg=BLUE)
window.minsize(width=300,height=300)

# Canvas for our logo
canvas = Canvas(width=200,height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.config(bg=BLUE,highlightthicknes=0)

# Labels
web_label = Label(text="Website/Username : ",width=20,height=2,font=("Arial",10,"bold"))
web_label.config(bg=BLUE,highlightthickness=0)
email_label = Label(text="Email : ",width=20,height=1,font=("Arial",10,"bold"))
email_label.config(bg=BLUE,highlightthickness=0)
pass_label = Label(text="Password : ",width=20,height=2,font=("Arial",10,"bold"))
pass_label.config(bg=BLUE,highlightthickness=0)

# Buttons
generate_btn = Button(text="Generate",width=19,command=generate_button_clicked)
generate_btn.config(bg=LIGHT_BLUE,highlightthickness=0)
add_btn = Button(text="Add",width=50,command=add_button_clicked)
add_btn.config(bg=LIGHT_BLUE,highlightthickness=0)
search_btn = Button(text="Search",command=search_button_clicked)
search_btn.config(bg=LIGHT_BLUE,width=19,highlightthickness=0)

# Edit text
pass_entry = Entry(width=35)
email_entry = Entry(width=59)
web_entry = Entry(width=35)
email_entry.insert(END,COMMON_EMAIL)

# Giving position
canvas.grid(column=1,row=0)
web_label.grid(column=0,row=1)
web_entry.grid(column=1,row=1)
email_label.grid(column=0,row=2)
email_entry.grid(column=1,row=2,columnspan=2)
pass_label.grid(column=0,row=3)
pass_entry.grid(column=1,row=3,padx=5)
generate_btn.grid(column=2,row=3)
add_btn.grid(column=1,row=4,columnspan=2)
search_btn.grid(column=2,row=1)



window.mainloop()