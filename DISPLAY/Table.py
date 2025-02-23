from tkinter import ttk
from DATA import GlobalDFs

class Table():
      def __init__(self, root, dataframe):
            self.root = root
            self.dataframe = GlobalDFs.updateDF(dataframe)

            # Scrollbar
            treeScroll = ttk.Scrollbar(root)
            treeScroll.pack(side="right", fill='y')

            self.tree = ttk.Treeview(root,  selectmode =        "browse", 
                                            show =              'headings', 
                                            yscrollcommand =    treeScroll.set, 
                                            style =             "Treeview"
                                    )
            self.tree['columns'] = list(self.dataframe.columns)
            
            for col in dataframe.columns:
                  self.tree.heading(col, text = col)
                  self.tree.column(col, width = 100, anchor = 'center')

            self.Populate(self.tree, self.dataframe)

            self.tree.pack(side="left", fill="both", anchor = "center", expand=True)
            treeScroll.config(command=self.tree.yview)

      def Populate(self, tree, dataframe):
            self.dataframe = GlobalDFs.updateDF(self.dataframe)
            tree.tag_configure('evenrow', background="#9ce3ff")

            # Clear table
            for row in tree.get_children():
                  tree.delete(row)

            for index, row in dataframe.iterrows():
                  if index % 2 == 0:
                        tree.insert("", "end", values=list(row), tags=('evenrow', ))
                  else:
                        tree.insert("", "end", values=list(row), tags=('oddrow', ))

            