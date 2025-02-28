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

root = tk.Tk()
root.title("Text Repeater")

tk.Label(root, text="How many times would you like to write the text:").pack()
times_entry = tk.Entry(root)
times_entry.pack()

tk.Label(root, text="What text would you like to write:").pack()
text_entry = tk.Entry(root)
text_entry.pack()

tk.Button(root, text="Repeat", command=copy_text).pack()

output_label = tk.Label(root, text="", justify="left")
output_label.pack()

root.mainloop()
