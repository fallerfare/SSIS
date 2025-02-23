from tkinter import ttk
import tkinter as tk
import TKinterModernThemes as TKMT
from DISPLAY.Repo import Repo
from DATA import GlobalDFs

# MAIN WINDOW
if __name__ =="__main__":
      window = TKMT.ThemedTKinterFrame("MSU-IIT Students","azure","dark")
      window.root.geometry("1000x860")
      window.root.resizable(width=False, height=False)

      style = ttk.Style()
      style.configure(  "Treeview", 
                        background =        "#ffffff", 
                        foreground =        "#000000",
                        rowheight =         25,
                        fieldbackground =   "#ffffff")

      # Header
      HeaderFrame = tk.Frame(window.root, background = "maroon")
      HeaderFrame.pack()
      Title = ttk.Label(HeaderFrame, text="MSU - IIT Students Repository", font=('Arial', 20), anchor = "center", background = "maroon", width = 800)
      Title.pack(padx = 15, pady = 15)

      # Tabs
      notebook = ttk.Notebook(window.root)
      notebook.pack(padx = 35, pady = 35, anchor= "center")

      RepoTable1 = Repo(notebook, GlobalDFs.readStudentsDF())
      RepoTable2 = Repo(notebook, GlobalDFs.readProgramsDF())
      RepoTable3 = Repo(notebook, GlobalDFs.readCollegesDF())

      notebook.add(RepoTable1, text="Students")
      notebook.add(RepoTable2, text="Programs")
      notebook.add(RepoTable3, text="Colleges")

      window.root.mainloop()