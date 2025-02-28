import tkinter as tk
import tkinter.messagebox as msgbox
import pyperclip

def copy_text():
    try:
        TimesPrint = int(times_entry.get())
        Text = text_entry.get()
        entire_text = ""

        for _ in range(TimesPrint):
            entire_text += Text + "\n"

        output_label.config(text=entire_text)
        pyperclip.copy(entire_text)
        msgbox.showinfo("Confirmation", "The text has been copied to the clipboard.")
    except ValueError:
        output_label.config(text="Please enter a valid number.")

def apply_mode():
    if root.tk.call("ttk::style", "theme", "use") == "default":
        root.tk.call("ttk::style", "theme", "use", "clam")
    else:
        root.tk.call("ttk::style", "theme", "use", "default")

    current_theme = root.tk.call("ttk::style", "theme", "use")
    if current_theme == "clam":
        apply_dark_mode()
    else:
        apply_light_mode()

def apply_dark_mode():
    root.configure(bg="black")
    for widget in root.winfo_children():
        widget.configure(bg="black", fg="white")

def apply_light_mode():
    root.configure(bg="white")
    for widget in root.winfo_children():
        widget.configure(bg="white", fg="black")

root = tk.Tk()
root.title("Text Copier")

# Apply the system's standard mode initially
apply_mode()

# Add a button to toggle between Dark Mode and Light Mode
toggle_button = tk.Button(root, text="Toggle Dark/Light Mode", command=apply_mode)
toggle_button.pack()

tk.Label(root, text="How many times would you like to write the text:").pack()
times_entry = tk.Entry(root)
times_entry.pack()

tk.Label(root, text="What text would you like to write:").pack()
text_entry = tk.Entry(root)
text_entry.pack()

tk.Button(root, text="Copy", command=copy_text).pack()

output_label = tk.Label(root, text="", justify="left")
output_label.pack()

root.mainloop()
