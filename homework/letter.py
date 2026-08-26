# In this assignment, you will build a Letter Writing Application using Python and Tkinter. You will open an existing letter, read its contents into a text editor, edit the text, save the letter as a new file, display the selected file path in the window title, connect button commands to functions, and arrange the interface using the grid layout.

import tkinter as tk
from tkinter import filedialog, messagebox

class LetterWriter:
    def __init__(self, root):
        self.root = root
        self.root.title("Letter Writing Application")
        self.root.geometry("700x500")

        self.text_editor = tk.Text(root, wrap="word", width=80, height=25)
        self.text_editor.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        open_button = tk.Button(root, text="Open Letter", command=self.open_letter)
        open_button.grid(row=1, column=0, padx=5, pady=10)

        save_button = tk.Button(root, text="Save As", command=self.save_letter)
        save_button.grid(row=1, column=1, padx=5, pady=10)

        clear_button = tk.Button(root, text="Clear", command=self.clear_text)
        clear_button.grid(row=1, column=2, padx=5, pady=10)

        exit_button = tk.Button(root, text="Exit", command=root.destroy)
        exit_button.grid(row=1, column=3, padx=5, pady=10)

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)
        root.grid_columnconfigure(3, weight=1)

    def open_letter(self):
        file_path = filedialog.askopenfilename(
            title="Open Letter",
            filetypes=[
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )

        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    contents = file.read()

                self.text_editor.delete("1.0", tk.END)
                self.text_editor.insert("1.0", contents)
                self.root.title(f"Letter Writing Application - {file_path}")

            except OSError as error:
                messagebox.showerror("Error", f"Could not open the file:\n{error}")

    def save_letter(self):
        file_path = filedialog.asksaveasfilename(
            title="Save Letter As",
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )

        if file_path:
            try:
                contents = self.text_editor.get("1.0", tk.END)

                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(contents)

                self.root.title(f"Letter Writing Application - {file_path}")
                messagebox.showinfo("Saved", "Your letter has been saved successfully.")

            except OSError as error:
                messagebox.showerror("Error", f"Could not save the file:\n{error}")

    def clear_text(self):
        self.text_editor.delete("1.0", tk.END)


root = tk.Tk()
app = LetterWriter(root)
root.mainloop()
