import requests
import random
import tkinter as tk
from tkinter import messagebox
a = random.randint(10000, 99999)

# try1 = requests.get(f'https://trigger.macrodroid.com/fdb98500-31dc-483c-bf28-bf75661c63ba/sui?number=53840941&verifycode={a}')

win = tk.Tk()
win.geometry('500x500')
win.resizable(False, False)
win.title('window')


def logged_in():
    Username.destroy()
    Username_label.destroy()
    Password.destroy()
    Password_label.destroy()
    Submit_button.destroy()
    ask_phone_label.destroy()
    ask_phone.destroy()
    Verify_code.destroy()
    Verify_code_label.destroy()
    Verify_code_button.destroy()
    title = str(random.randint(100000000000000, 10000000000000000))
    win.title(title)
    win.geometry('800x800')



def send_verification(is_username_correct, is_password_correct, go_into_middle, phone_number, verify_code_USER):
    global given_code
    if go_into_middle:
        try:
            given_code = int(verify_code_USER.get())
        except BaseException:
            messagebox.showerror('Error', "Issue occurred on the int conversion with the given user verify code, "
                                          "most likely you didn't use numbers")
            exit()
        if given_code == int(a):
            logged_in()
        else:
            messagebox.showerror('Error', 'Wrong code')
            exit()
    else:
        pass

    if is_username_correct and is_password_correct:
        # insert the macrodroid webhook below !!!!!!!!!!!!!!!!!!!!!!!!
        requests.get(f'https://trigger.macrodroid.com/special_code/special_identifier?number={phone_number}&verifycode={a}')
        # remove the messagebox command below if you've already inserted a macrodroid identifier
        messagebox.showerror('Error', 'Please insert a macrodroid webhook, it will not work without it.')
        exit()
        # remove the messagebox command above if you've already inserted a macrodroid identifier
        Sumbit2_button.destroy()
        ask_phone.destroy()
        ask_phone_label.destroy()
        Verify_code.place(x=0, y=140)
        Verify_code_button.place(x=0, y=165)
        Verify_code_label.place(x=0, y=120)
    else:
        messagebox.showerror('Error', 'Wrong password or/and username')


def verify():
    password_entry_get = Password.get()
    username_entry_get = Username.get()
    is_username_correct = False
    is_password_correct = False

    if len(username_entry_get) < 3:
        messagebox.showerror('Error', f'Issue with the size of username and/or password, phone number')
        exit()
    elif len(password_entry_get) < 3:
        messagebox.showerror('Error', f'Issue with the size of username and/or password, phone number')
        exit()
    elif len(ask_phone.get()) < 3:
        messagebox.showerror('Error', f'Issue with the size of username and/or password, phone number')
        exit()
    try:
        phone_number = int(ask_phone.get())
    except BaseException:
        messagebox.showerror('Error', 'Issue while converting to int, most likely your not inserting an actual number.')
        exit()
    if username_entry_get in 'test':
        is_username_correct = True
    if password_entry_get in 'test':
        is_password_correct = True
    send_verification(is_username_correct=is_username_correct, is_password_correct=is_password_correct, go_into_middle=False, phone_number=phone_number, verify_code_USER=None)


def func():
    Submit_button.after(1, Submit_button.destroy())
    Sumbit2_button.place(x=0, y=165)
    ask_phone.place(x=0, y=140)
    ask_phone_label.place(x=0, y=120)


Username_label = tk.Label(win, text='Username', font=('arial', 10))
Username_label.place(x=0, y=30)

Username = tk.Entry(win, width=25)
Username.place(x=0, y=50)

Password = tk.Entry(win, width=25, show='*')
Password.place(x=0, y=100)

Password_label = tk.Label(win, text='Password', font=('arial', 10))
Password_label.place(x=0, y=76)

Submit_button = tk.Button(win, text='Login', font=('arial', 10), width=15, command=func)
Submit_button.place(x=0, y=125)

Sumbit2_button = tk.Button(win, text='Continue', font=('arial', 10), width=15, command=verify)
ask_phone = tk.Entry(win, width=25)
ask_phone_label = tk.Label(win, text='Verify with your phone number', font=('arial', 10))

Verify_code_label = tk.Label(win, text='Enter the code sent to your phone', font=('arial', 10))
Verify_code = tk.Entry(win, width=25)
Verify_code_button = tk.Button(win, text='Submit', font=('arial', 10), width=15, command=lambda: send_verification(is_password_correct=None, is_username_correct=None, go_into_middle=True, phone_number=None, verify_code_USER=Verify_code))

win.mainloop()