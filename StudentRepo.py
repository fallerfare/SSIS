import tkinter as tk
# import customtkinter
from tkinter import ttk
import pandas as pd
import TKinterModernThemes as TKMT

class Table:
      def __init__(self, root, dataframe):
            self.root = root
            self.dataframe = dataframe

            treeFrame = ttk.Frame(root)
            treeFrame.pack(anchor= "center")

            # Scrollbar
            treeScroll = ttk.Scrollbar(treeFrame)
            treeScroll.pack(side="right", fill="y")

            self.style = ttk.Style()
            self.style.configure(   "Treeview", 
                                    background = "#ffffff", 
                                    foreground = "#000000",
                                    rowheight = 25,
                                    fieldbackground = "#ffffff")

            self.tree = ttk.Treeview(treeFrame, selectmode="browse", show = 'headings', yscrollcommand=treeScroll.set, style = "Treeview")
            self.tree['columns'] = list(dataframe.columns)
            
            for col in dataframe.columns:
                  self.tree.heading(col, text = col)
                  self.tree.column(col, width= 100, anchor = 'center')

            populatetable(self.tree, df)

            self.tree.pack(side="left", fill="y")

            treeScroll.config(command=self.tree.yview)

def populatetable(tree, dataframe):
            
            tree.tag_configure('evenrow', background="#9ce3ff")

            # Clear table
            for row in tree.get_children():
                  tree.delete(row)

            for index, row in dataframe.iterrows():
                  if index % 2 == 0:
                        tree.insert("", "end", values=list(row), tags=('evenrow', ))
                  else:
                        tree.insert("", "end", values=list(row), tags=('oddrow', ))

class searchnsort:
      def __init__(self, root, table, df):
            self.root = root
            self.table = table
            self.dataframe = df

            searchnsortframe = ttk.Frame(root)
            searchnsortframe.pack(anchor= "center")

            searchlabel = ttk.Label(searchnsortframe, text="Search", font=('Arial', 12))
            searchlabel.grid(row = 0, column = 0)

            self.searchbar = ttk.Entry(searchnsortframe, font=('Arial', 9), width=20)
            self.searchbar.grid(row = 0, column = 1)  
            self.searchbar.bind("<KeyRelease>", self.perform_search)

            sortwithlabel = ttk.Label(searchnsortframe, text="Sort with", font=('Arial', 12))
            sortwithlabel.grid(row = 0, column = 2)

            self.sortwithbar = ttk.Combobox(searchnsortframe,   state="readonly", 
                                        values=["ID", "First Name", "Last Name",
                                                "Email", "Year Level", "Status"          ],
                                        
                                        width = 15)
            self.sortwithbar.grid(row = 0, column = 3)

            sortbylabel = ttk.Label(searchnsortframe, text="Sort by", font=('Arial', 12))
            sortbylabel.grid(row = 0, column = 4)

            self.sortbybar = ttk.Combobox(searchnsortframe,   state="readonly", 
                                        values=["Ascending", "Descending"          ],
                                        
                                        width = 15)
            self.sortbybar.grid(row = 0, column = 5)
            self.sortbybar.bind("<<ComboboxSelected>>", self.perform_sort)

      def perform_sort(self, event):
            sortwithkey = self.sortwithbar.get()
    
            if not sortwithkey:
                  return  # Avoid sorting if no column is selected

            # Ensure column names match DataFrame column names exactly
            column_mapping = {
                              "ID": "ID",
                              "First Name": "First Name",
                              "Last Name": "Last Name",
                              "Email": "Email",
                              "Year Level": "Year Level",
                              "Status": "Status"
            }

            dataframe_column = column_mapping.get(sortwithkey)

            if dataframe_column is None:
                  return  # Avoid sorting if mapping fails

            ascending = self.sortbybar.get() == "Ascending"

            # Sort the dataframe
            self.dataframe = self.dataframe.sort_values(by=[dataframe_column], ascending=ascending)

            # Repopulate the table with sorted data
            populatetable(self.table.tree, self.dataframe)



      def perform_search(self, event):
            search_term = self.searchbar.get().lower()
            
            filtered_df = self.table.dataframe[self.table.dataframe.apply(lambda row: row.astype(str).str.lower().str.contains(search_term).any(), axis=1)]

            populatetable(self.table.tree, filtered_df)

            

# MAIN WINDOW
if __name__ =="__main__":
      window = TKMT.ThemedTKinterFrame("MSU-IIT Students","azure","dark")
      window.root.geometry("1000x860")
      window.root.resizable(width=True, height=True)

      df = pd.read_csv('Students.csv')

      # Panedwindow
      RepoTable = ttk.PanedWindow(window.root, width = 900)
      RepoTable.pack(padx = 35, pady = 35, anchor= "center")

      # Pane #1
      searchpane = ttk.Frame(RepoTable)
      RepoTable.add(searchpane, weight=0)

      # Pane #2
      tablepane = ttk.Frame(RepoTable)
      RepoTable.add(tablepane, weight=0)

      

      table = Table(tablepane, df)
      search = searchnsort(searchpane, table, df)

      window.root.mainloop()