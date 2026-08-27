# In this assignment, you will build a Reading Schedule Planner using Python and Tkinter. You will create a main window and open a separate Toplevel window where you can enter the total number of pages in a book and the number of pages you plan to read each day. The program will calculate complete reading days and remaining pages using floor division and modulo, while try/except will handle invalid input.

import tkinter as tk
from tkinter import messagebox

def open_reading_planner():
    planner_window = tk.Toplevel(root)
    planner_window.title("Reading Schedule Planner")
    planner_window.geometry("400x300")
    planner_window.resizable(False, False)

    tk.Label(
        planner_window,
        text="Reading Schedule Planner",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    tk.Label(planner_window, text="Total number of pages:").pack()

    total_pages_entry = tk.Entry(planner_window)
    total_pages_entry.pack(pady=5)

    tk.Label(planner_window, text="Pages to read each day:").pack()

    pages_per_day_entry = tk.Entry(planner_window)
    pages_per_day_entry.pack(pady=5)

    result_label = tk.Label(
        planner_window,
        text="",
        font=("Arial", 11)
    )
    result_label.pack(pady=15)

    def calculate_schedule():
        try:
            total_pages = int(total_pages_entry.get())
            pages_per_day = int(pages_per_day_entry.get())

            if total_pages <= 0 or pages_per_day <= 0:
                raise ValueError

            complete_days = total_pages // pages_per_day
            remaining_pages = total_pages % pages_per_day

            result_label.config(
                text=f"Complete reading days: {complete_days}\n"
                     f"Remaining pages: {remaining_pages}"
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter positive whole numbers."
            )

    tk.Button(
        planner_window,
        text="Calculate Schedule",
        command=calculate_schedule
    ).pack(pady=5)

    tk.Button(
        planner_window,
        text="Close",
        command=planner_window.destroy
    ).pack(pady=5)


root = tk.Tk()
root.title("Reading Planner")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(
    root,
    text="Reading Schedule Planner",
    font=("Arial", 18, "bold")
).pack(pady=30)

tk.Button(
    root,
    text="Open Reading Planner",
    font=("Arial", 12),
    command=open_reading_planner
).pack()

root.mainloop()
