from tkinter import ttk
from DISPLAY.Display import Display

class Table(Display):
      def __init__(self, root, dataframe):
            super().__init__(root, dataframe)

            # Scrollbar
            treeScroll = ttk.Scrollbar(root)
            treeScroll.pack(side="right", fill="y")

            self.style = ttk.Style()
            self.style.configure(   "Treeview", 
                                    background =        "#ffffff", 
                                    foreground =        "#000000",
                                    rowheight =         25,
                                    fieldbackground =   "#ffffff")

            self.tree = ttk.Treeview(root,  selectmode =        "browse", 
                                            show =              'headings', 
                                            yscrollcommand =    treeScroll.set, 
                                            style =             "Treeview")
            self.tree['columns'] = self.headers
            
            for col in dataframe.columns:
                  self.tree.heading(col, text = col)
                  self.tree.column(col, width= 100, anchor = 'center')

            self.Populate(self.tree, self.dataframe)

            self.tree.pack(side="left", fill="y")
            treeScroll.config(command=self.tree.yview)