from tkinter import ttk
import tkinter as tk
import pandas as pd
import TKinterModernThemes as TKMT
from DISPLAY.Repo import Repo

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
      Title = ttk.Label(HeaderFrame, text="MSU - IIT Students Repository", font=('Arial', 30), anchor = "center", background = "maroon", width = 800)
      Title.pack(padx = 15, pady = 25)

      # Tabs
      notebook = ttk.Notebook(window.root)
      notebook.pack(padx = 35, pady = 35, anchor= "center")

      # Separate tables for each dataframe
      df1 = pd.read_csv(r'DATA\Students.csv')
      df2 = pd.read_csv(r'DATA\Programs.csv')
      df3 = pd.read_csv(r'DATA\Colleges.csv')

      RepoTable1 = Repo(notebook, df1)
      RepoTable2 = Repo(notebook, df2)
      RepoTable3 = Repo(notebook, df3)

      notebook.add(RepoTable1, text="Students")
      notebook.add(RepoTable2, text="Programs")
      notebook.add(RepoTable3, text="Colleges")

      window.root.mainloop()