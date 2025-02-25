from tkinter import ttk
from DATA import GlobalDFs

class Table():
      def __init__(self, root, dataframe, notebook):
            self.root = root
            self.dataframe = GlobalDFs.updateDF(dataframe)
            self.notebook = notebook
            self.notebook.bind("<<NotebookTabChanged>>", self.tab_change)

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

            self.update_table(dataframe)

      def update_table(self, dataframe):
            self.dataframe = GlobalDFs.updateDF(dataframe)  # Update dataframe reference
            self.tree["columns"] = list(self.dataframe.columns)

            for col in self.dataframe.columns:
                  self.tree.heading(col, text=col)
                  self.tree.column(col, width=100, anchor="center")

            self.Populate(self.tree, self.dataframe, "Update")


      def Populate(self, tree, dataframe, source):
            self.dataframe = dataframe
            tree.tag_configure('evenrow', background="#9ce3ff")

            print(self.dataframe)

            print(dataframe)

            # Clear table
            for row in tree.get_children():
                  tree.delete(row)

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
                  self.update_table(tab_data[tab_text])

                  # Force UI to update
                  self.tree.update_idletasks()  # Ensures UI refresh
                                                                                                                                                

            