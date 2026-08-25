# In this assignment, you will build an After-School Routine Checker using Python and Tkinter. You will create a simple app that responds when you type a task, click the routine area, or press a button. The app will display the last character you typed, react to a mouse click, show a warning when no task is entered, and display the next task in your routine.

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("After-School Routine Checker")
root.geometry("500x400")

routine = [
    "Put away your school bag",
    "Have a snack",
    "Do your homework",
    "Take a break",
    "Prepare for tomorrow"
]

current_task = 0

def show_last_character(event):
    text = task_entry.get()
    if text:
        last_character_label.config(text=f"Last character typed: {text[-1]}")
    else:
        last_character_label.config(text="Last character typed: None")

def routine_clicked(event):
    click_label.config(text="You clicked the routine area!")

def check_task():
    task = task_entry.get().strip()
    if not task:
        messagebox.showwarning("No Task", "Please enter a task.")
    else:
        result_label.config(text=f"Task entered: {task}")

def next_task():
    global current_task
    result_label.config(text=f"Next task: {routine[current_task]}")
    current_task = (current_task + 1) % len(routine)

title_label = tk.Label(
    root,
    text="After-School Routine Checker",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

task_label = tk.Label(root, text="Enter a task:")
task_label.pack()

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)
task_entry.bind("<KeyRelease>", show_last_character)

last_character_label = tk.Label(
    root,
    text="Last character typed: None",
    font=("Arial", 11)
)
last_character_label.pack(pady=10)

routine_area = tk.Frame(
    root,
    width=400,
    height=80,
    bg="lightblue",
    borderwidth=2,
    relief="solid"
)
routine_area.pack(pady=10)
routine_area.bind("<Button-1>", routine_clicked)

routine_area_label = tk.Label(
    routine_area,
    text="Click the routine area",
    bg="lightblue",
    font=("Arial", 12)
)
routine_area_label.place(relx=0.5, rely=0.5, anchor="center")

click_label = tk.Label(root, text="", font=("Arial", 10))
click_label.pack()

check_button = tk.Button(
    root,
    text="Check Task",
    command=check_task
)
check_button.pack(pady=5)

next_button = tk.Button(
    root,
    text="Show Next Task",
    command=next_task
)
next_button.pack(pady=5)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    fg="green"
)
result_label.pack(pady=15)

root.mainloop()
