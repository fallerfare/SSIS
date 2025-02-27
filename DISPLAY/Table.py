from tkinter import ttk
from DATA import GlobalDFs

class Table():
        def __init__(self, root, dataframe, notebook):
                self.root = root
                self.dataframe = GlobalDFs.updateDF(dataframe)
                self.notebook = notebook
                self.notebook.bind("<<NotebookTabChanged>>", lambda event: self.tab_change(event))

                # Scrollbar
                treeScroll = ttk.Scrollbar(root)
                treeScroll.pack(side="right", fill='y', anchor="center")

                self.tree = ttk.Treeview(root,  selectmode =        "browse", 
                                                show =              'headings', 
                                                yscrollcommand =    treeScroll.set, 
                                                style =             "Treeview"
                                        )
                self.tree['columns'] = list(self.dataframe.columns)
                
                for col in self.dataframe.columns:
                        self.tree.heading(col, text = col)
                        self.tree.column(col, width = 100, anchor = 'center')

                self.Populate(self.tree, self.dataframe, "Update")

                self.tree.pack(side="left", fill="both", anchor = "center", expand=True)
                treeScroll.config(command=self.tree.yview)

        def update_table(self, dataframe):
                self.tree.delete(*self.tree.get_children())
                
                # Fix: Convert list to string before concatenation
                print("This should be empty:", list(self.tree.get_children()))
                
                newdataframe = GlobalDFs.updateDF(dataframe)  # Update dataframe reference
                self.tree["columns"] = list(newdataframe.columns)

                for col in newdataframe.columns:
                        self.tree.heading(col, text=col)
                        self.tree.column(col, width=100, anchor="center")

                # Fix: Convert list to string before concatenation
                print("These are the headers:", list(newdataframe.columns))      
                print("Current children, should be none:", list(self.tree.get_children()))

                # Populate with new data
                self.Populate(self.tree, newdataframe, "Update")
                
                # Fix: Properly print the dataframe instead of direct concatenation
                print("This is the updated data:\n", newdataframe)

                # Force UI update
                self.tree.update_idletasks()



        def Populate(self, tree, dataframe, source):
                self.dataframe = dataframe
                self.tree.tag_configure('evenrow', background="#9ce3ff")

                # Clear table
                for row in self.tree.get_children():
                        self.tree.delete(row)

                if(source == "Filter"):
                        for index, row in dataframe.iterrows():
                                if index % 2 == 0:
                                        tree.insert("", "end", values=list(row), tags=('evenrow', ))
                                else:
                                        tree.insert("", "end", values=list(row), tags=('oddrow', ))

                if(source == "Update"):
                        for index, row in self.dataframe.iterrows():
                                if index % 2 == 0:
                                        tree.insert("", "end", values=list(row), tags=('evenrow', ))
                                else:
                                        tree.insert("", "end", values=list(row), tags=('oddrow', ))
      
        def tab_change(self, event):
                self.update()

        def update(self):
                tab_id = self.notebook.select()
                tab_text = self.notebook.tab(tab_id, "text")

                # Select correct DataFrame based on the active tab
                tab_data = {
                        "Students": GlobalDFs.readStudentsDF(),
                        "Programs": GlobalDFs.readProgramsDF(),
                        "Colleges": GlobalDFs.readCollegesDF(),
                }

                if tab_text in tab_data:
                        print(f"Switching to tab: {tab_text}")
                        print(f"Data to load:\n{tab_data[tab_text].head()}")  # Print first few rows
                        self.update_table(tab_data[tab_text])

                        # Force UI to update
                        self.tree.update_idletasks()