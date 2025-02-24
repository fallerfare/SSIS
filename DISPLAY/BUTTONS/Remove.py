from tkinter import ttk
from DATA import GlobalDFs

# =====================
#    REMOVE BUTTON
# =====================
class Remove:
    def __init__(self, root, dataframe, table):
        # tommy innit
        self.root = root
        self.dataframe = dataframe
        self.table = table
        self.removekey = None 

        # Format Remove Button according to tab
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

    # we removin dis guy
    def setremovekey(self, key):
        self.removekey = key

    # dis guy be removed
    def remove_entry(self):
        if self.removekey is None:
            return

        column_name = self.dataframe.columns[0]  # Identify primary key
                                                 # This is to see
                                                 # The current df from which
                                                 # An item is to cease
                                                 # bow

        
        self.dataframe = GlobalDFs.updateDF(self.dataframe)
        
        # Debugging
        # print("Before removal:", self.dataframe) 

        # Remove the row
        self.dataframe = self.dataframe[self.dataframe[column_name] != self.removekey]
        
        # Debugging
        # print("After removal:", self.dataframe)

        # Match key to current tab
        match column_name:
            case "ID":
                GlobalDFs.writeStudentsDF(self.dataframe)
            case "Program Code":
                GlobalDFs.writeProgramsDF(self.dataframe)
            case "College Code":
                GlobalDFs.writeCollegesDF(self.dataframe)

        # Refresh key
        self.removekey = None

        # Refresh tree
        self.table.Populate(self.table.tree, self.dataframe)
# =====================
#    REMOVE BUTTON
# =====================      