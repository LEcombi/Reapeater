import tkinter as tk

def apply_mode(root):
    if root.tk.call("ttk::style", "theme", "use") == "default":
        root.tk.call("ttk::style", "theme", "use", "clam")
    else:
        root.tk.call("ttk::style", "theme", "use", "default")

    current_theme = root.tk.call("ttk::style", "theme", "use")
    if current_theme == "clam":
        apply_dark_mode(root)
    else:
        apply_light_mode(root)

def apply_dark_mode(root):
    root.configure(bg="black")
    for widget in root.winfo_children():
        widget.configure(bg="black", fg="white")

def apply_light_mode(root):
    root.configure(bg="white")
    for widget in root.winfo_children():
        widget.configure(bg="white", fg="black")

def toggle_mode(root):
    if root.tk.call("ttk::style", "theme", "use") == "default":
        root.tk.call("ttk::style", "theme", "use", "clam")
        apply_dark_mode(root)
    else:
        root.tk.call("ttk::style", "theme", "use", "default")
        apply_light_mode(root)
