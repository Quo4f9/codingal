# In this assignment, you will build an ATM PIN Setup Interface using Python and Tkinter. You will group account details and keypad cells inside frames, add raised and sunken borders, build a keypad with grid(), position form widgets precisely with place(), hide the PIN using show="*", and use a button to read the entered details and update a Text widget.


import tkinter as tk


root = tk.Tk()
root.title("ATM PIN Setup")
root.geometry("500x550")
root.resizable(False, False)

account_frame = tk.LabelFrame(
    root,
    text="Account Details",
    padx=10,
    pady=10,
    bd=3,
    relief="raised"
)
account_frame.place(x=30, y=30, width=440, height=180)
r
tk.Label(account_frame, text="Account Number:").place(x=20, y=20)
account_entry = tk.Entry(account_frame, width=30)
account_entry.place(x=150, y=20)


tk.Label(account_frame, text="Account Name:").place(x=20, y=60)
name_entry = tk.Entry(account_frame, width=30)
name_entry.place(x=150, y=60)


tk.Label(account_frame, text="Enter PIN:").place(x=20, y=100)
pin_entry = tk.Entry(account_frame, width=30, show="*")
pin_entry.place(x=150, y=100)


keypad_frame = tk.LabelFrame(
    root,
    text="Keypad",
    padx=10,
    pady=10,
    bd=3,
    relief="sunken"
)
keypad_frame.place(x=30, y=225, width=440, height=200)


buttons = [
    ("1", 0, 0), ("2", 0, 1), ("3", 0, 2),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
    ("Clear", 3, 0), ("0", 3, 1), ("Enter", 3, 2)
]

def keypad_click(value):
    if value == "Clear":
        pin_entry.delete(0, tk.END)
    elif value == "Enter":
        display_details()
    else:
        pin_entry.insert(tk.END, value)

for text, row, column in buttons:
    tk.Button(
        keypad_frame,
        text=text,
        width=10,
        height=2,
        command=lambda value=text: keypad_click(value)
    ).grid(row=row, column=column, padx=5, pady=3)

display = tk.Text(
    root,
    width=48,
    height=5,
    bd=3,
    relief="sunken"
)
display.place(x=30, y=440)


def display_details():
    account_number = account_entry.get()
    account_name = name_entry.get()
    pin = pin_entry.get()

    display.delete("1.0", tk.END)
    display.insert(
        tk.END,
        "ATM PIN Setup Details\n"
        "----------------------\n"
        f"Account Number: {account_number}\n"
        f"Account Name: {account_name}\n"
        f"PIN: {'*' * len(pin)}"
    )



root.mainloop()