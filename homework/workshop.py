#In this assignment, you will build a Workshop Participant Greeting application using Python and Tkinter. You will create a desktop window, display instructions with Label widgets, collect a participant's name with an Entry widget, and show a multi-line welcome message with the workshop date inside a Text widget. A Check In button will run a function that reads the typed name and updates the output area.


import tkinter as tk


root = tk.Tk()
root.title("Workshop Participant Greeting")
root.geometry("500x400")
root.resizable(False, False)


title_label = tk.Label(
    root,
    text="Workshop Participant Check-In",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=20)

instruction_label = tk.Label(
    root,
    text="Welcome to our workshop!",
    font=("Arial", 12)
)
instruction_label.pack(pady=5)

instruction_label2 = tk.Label(
    root,
    text="Please enter your name below and click Check In."
)
instruction_label2.pack(pady=5)


name_label = tk.Label(
    root,
    text="Participant Name:"
)
name_label.pack(pady=(20, 5))

# Name entry
name_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)
name_entry.pack()

def check_in():
    name = name_entry.get()

    output_text.delete("1.0", tk.END)

    message = (
        f"Welcome, {name}!\n\n"
        "Thank you for participating in our workshop.\n"
        "We are excited to have you join us.\n\n"
        "Workshop Date: August 14, 2026"
    )

    output_text.insert(tk.END, message)



check_in_button = tk.Button(
    root,
    text="Check In",
    width=15,
    command=check_in
)
check_in_button.pack(pady=20)


output_text = tk.Text(
    root,
    width=50,
    height=8,
    font=("Arial", 11)
)
output_text.pack(pady=5)


root.mainloop()