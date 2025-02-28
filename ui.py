import tkinter as tk
import pyperclip
import tkinter.messagebox as msgbox

def copy_text(times_entry, text_entry, output_label):
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

def create_ui(root):
    from modes import toggle_mode

    toggle_button = tk.Button(root, text="Toggle Dark/Light Mode", command=lambda: toggle_mode(root))
    toggle_button.pack()

    tk.Label(root, text="How many times would you like to write the text:").pack()
    times_entry = tk.Entry(root)
    times_entry.pack()

    tk.Label(root, text="What text would you like to write:").pack()
    text_entry = tk.Entry(root)
    text_entry.pack()

    copy_button = tk.Button(root, text="Copy", command=lambda: copy_text(times_entry, text_entry, output_label))
    copy_button.pack()

    output_label = tk.Label(root, text="", justify="left")
    output_label.pack()
