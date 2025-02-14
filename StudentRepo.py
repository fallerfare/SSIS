import tkinter as tk
# import customtkinter
from tkinter import ttk
import pandas as pd

class StudentTable:
      def __init__(self, root, dataframe):
            self.root = root
            self.dataframe = dataframe

           
            treeFrame = ttk.Frame(root)
            treeFrame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

            # Scrollbar
            treeScroll = ttk.Scrollbar(treeFrame)
            treeScroll.pack(side="right", fill="y")

            self.tree = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set)
            self.tree['columns'] = list(dataframe.columns)
            self.tree['show'] = 'headings'

            for col in dataframe.columns:
                  self.tree.heading(col, text = col)
                  self.tree.column(col, anchor = 'center')

            for index, row in dataframe.iterrows():
                  self.tree.insert("", "end", values=list(row))

            self.tree.pack(side="left", fill="y")
        
            # Define the columns
            self.tree.column(0, width=75, anchor="center")
            self.tree.column(1, width=100, anchor="center")          
            self.tree.column(2, width=100, anchor="center")  
            self.tree.column(3, width=100, anchor="center")  
            self.tree.column(4, width=100, anchor="center")  
            self.tree.column(5, width=100, anchor="center")  
            self.tree.column(6, width=100, anchor="center")  
            self.tree.column(7, width=75, anchor="center") 

            treeScroll.config(command=self.tree.yview)

class searchnsort:
      def __init__(self, root, table):
            self.root = root
            self.table = table
            self.searchbar = ttk.Entry(root, font=('Arial', 9), width=35)
            self.searchbar.pack(pady=10, padx=10, anchor="center")  
            self.searchbar.bind("<KeyRelease>", self.perform_search)  

      def perform_search(self, event):
            # TODO: Implement search functionality
            search_term = self.searchbar.get().lower()
            
            # Clear table
            for row in self.table.tree.get_children():
                  self.table.tree.delete(row)
            
            filtered_df = self.table.dataframe[self.table.dataframe.apply(lambda row: row.astype(str).str.lower().str.contains(search_term).any(), axis=1)]

            for index, row in filtered_df.iterrows():
                  self.table.tree.insert("", "end", values = list(row))

# MAIN WINDOW
if __name__ =="__main__":
      root = tk.Tk()
      root.geometry("900x860")
      root.title("MSU-IIT Students")
      root.resizable(width=True, height=True)

      df = pd.read_csv('Students.csv')

      # Panedwindow
      RepoTable = ttk.PanedWindow(root, width = 800)
      RepoTable.pack(padx = 35, pady = 35, anchor= "center")

      # Pane #1
      searchpane = ttk.Frame(RepoTable)
      RepoTable.add(searchpane, weight=1)

      # Pane #2
      tablepane = ttk.Frame(RepoTable)
      RepoTable.add(tablepane, weight=1)

      table = StudentTable(tablepane, df)
      search = searchnsort(searchpane, table)

      root.mainloop()