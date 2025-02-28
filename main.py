import tkinter as tk
from ui import create_ui
from modes import apply_mode

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Text Copier")

    apply_mode(root)
    create_ui(root)

    root.mainloop()
