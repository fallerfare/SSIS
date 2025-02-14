from pandastable import Table
import pandas as pd
import tkinter as tk
from tkinter import ttk

class StudentTable():
    def __init__(self, root, dataframe):
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        # Use the passed dataframe
        self.table = Table(self.frame, dataframe=dataframe)
        self.table.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x860")
    root.title("MSU-IIT Students")
    root.resizable(width=True, height=True)

    # Load the DataFrame
    df = pd.read_csv('Students.csv')

    # Panedwindow
    RepoTable = ttk.PanedWindow(root, width = 800)
    RepoTable.grid(row=1, column=0, pady=(25, 5), sticky="nsew")

    # Pane #1
    tablepane = ttk.Frame(RepoTable)
    RepoTable.add(tablepane, weight=1)

    # Pane #2
    searchpane = ttk.Frame(RepoTable)
    RepoTable.add(searchpane, weight=1)

    # Instantiate the PandaApp with the DataFrame
    table = StudentTable(tablepane, df)

    # Start the Tkinter main loop
    root.mainloop()