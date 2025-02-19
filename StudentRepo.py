from tkinter import ttk
import pandas as pd
import TKinterModernThemes as TKMT
from DISPLAY.Table import Table
from DISPLAY.Filter import Filter

# MAIN WINDOW
if __name__ =="__main__":
      window = TKMT.ThemedTKinterFrame("MSU-IIT Students","azure","dark")
      window.root.geometry("1000x860")
      window.root.resizable(width=True, height=True)

      df = pd.read_csv(r'DATA\Students.csv')

      # Header
      Title = ttk.Label(window.root, text="MSU - IIT Students Repository", font=('Arial', 30), anchor = "center")
      Title.pack(padx = 15, pady = 25)

      # Table Display
      RepoTable = ttk.Frame(window.root, width = 900)
      RepoTable.pack(padx = 35, pady = 35, anchor= "center")

      # Search Display
      searchpane = ttk.Frame(RepoTable)
      searchpane.grid(row = 1, column=0, sticky="nsew", pady=15)

      # Table Display
      tablepane = ttk.Frame(RepoTable)
      tablepane.grid(row = 2, column=0, sticky="nsew", pady=15)

      # Display Elements
      table = Table(tablepane, df)
      search = Filter(searchpane, df, table)

      window.root.mainloop()