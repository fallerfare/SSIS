from tkinter import ttk
from DATA import GlobalDFs

class Remove:
    def __init__(self, root, dataframe, table):
        self.root = root
        self.dataframe = dataframe
        self.table = table
        self.removekey = None

        match dataframe.columns[0]:  
            case "ID":
                command = self.remove_entry
                buttext = "Remove Student"
            case "Program Code":
                command = self.remove_entry
                buttext = "Remove Program"
            case "College Code":
                command = self.remove_entry
                buttext = "Remove College"
            case _:
                buttext = "What, no button???"

        self.Button = ttk.Button(self.root, text=buttext, command=command, state="disabled")

    def setremovekey(self, key):
        self.removekey = key

    def remove_entry(self):
        if self.removekey is None:
            return

        column_name = self.dataframe.columns[0]  # Identify primary key

        self.dataframe = GlobalDFs.updateDF(self.dataframe)
        print("Before removal:", self.dataframe)

        # Remove the row
        self.dataframe = self.dataframe[self.dataframe[column_name] != self.removekey]

        print("After removal:", self.dataframe)

        match column_name:
            case "ID":
                GlobalDFs.writeStudentsDF(self.dataframe)
            case "Program Code":
                GlobalDFs.writeProgramsDF(self.dataframe)
            case "College Code":
                GlobalDFs.writeCollegesDF(self.dataframe)

        self.removekey = None

        self.table.Populate(self.table.tree, self.dataframe)
        

        
