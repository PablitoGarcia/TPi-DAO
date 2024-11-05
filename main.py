import tkinter as tk
from tkinter import ttk
from app import App

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('1000x700')
    app = App(root)
    root.mainloop()