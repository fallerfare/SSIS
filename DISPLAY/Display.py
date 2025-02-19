class Display:
    def __init__(self, root, dataframe):
        self.root = root
        self.dataframe = dataframe
        self.headers = list(dataframe.columns)

    def Populate(self, tree, dataframe):
            
        tree.tag_configure('evenrow', background="#9ce3ff")

        # Clear table
        for row in tree.get_children():
            tree.delete(row)

        for index, row in dataframe.iterrows():
            if index % 2 == 0:
                    tree.insert("", "end", values=list(row), tags=('evenrow', ))
            else:
                    tree.insert("", "end", values=list(row), tags=('oddrow', ))

