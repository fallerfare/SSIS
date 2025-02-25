from tkinter import ttk
import tkinter as tk

class ConfirmWin:
    def __init__(self):

        self.root = tk.Toplevel()
        self.root.geometry("900x400")
        self.root.resizable(width=False, height=False)

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=20, pady=20, anchor="center")