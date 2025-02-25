from tkinter import ttk
from DATA import GlobalDFs
from DATA import GlobalHash

# =====================
#    REMOVE BUTTON
# =====================
class Remove:
    def __init__(self, root, dataframe, table):
        # tommy innit
        self.root = root
        self.dataframe = dataframe
        self.originaltype = None
        self.table = table
        self.removekey = None 
        self.column_name = self.dataframe.columns[0]

        # Format Remove Button according to tab
        match self.column_name:  
            case "ID":
                command = self.remove_entry
                buttext = "Remove Student"
                self.originaltype = "Students"
            case "Program Code":
                command = self.remove_entry
                buttext = "Remove Program"
                self.originaltype = "Programs"
            case "College Code":
                command = self.remove_entry
                buttext = "Remove College"
                self.originaltype = "Colleges"
            case _:
                buttext = "What, no button???"

        self.Button = ttk.Button(self.root, text=buttext, command=command, state="disabled")

    # we removin dis guy
    # accessed by treeviewselect
    def setremovekey(self, key):
        self.removekey = key
        print("Setting: " + self.removekey)

    # dis guy be removed
    def remove_entry(self):
        if self.removekey is None:
            return

        print("Removing: " + self.removekey)

        self.dataframe = GlobalDFs.updateDF(self.dataframe) # Is this needed? idk but it make me feel safe. Applies to other uses TTOTT

        # Remove the row
        self.dataframe = self.dataframe[self.dataframe[self.column_name] != self.removekey]

        # Match key to current tab
        match self.column_name:
            case "ID":
                GlobalDFs.writeStudentsDF(self.dataframe)
            case "Program Code":
                GlobalDFs.writeProgramsDF(self.dataframe)
                self.removeEnrollees(self.removekey)
            case "College Code":
                GlobalDFs.writeCollegesDF(self.dataframe)
                self.removeDegrees(self.removekey)

        # Refresh tree
        match self.originaltype:
            case "Students":
                self.table.Populate(self.table.tree, GlobalDFs.readStudentsDF())
            case "Programs":
                self.table.Populate(self.table.tree, GlobalDFs.readProgramsDF())
            case "Colleges":
                self.table.Populate(self.table.tree, GlobalDFs.readCollegesDF())

        self.removekey = None

    def removeDegrees(self, collegecode):
        for program in GlobalHash.showDegrees(collegecode):
            print("Resetting key: " + program)
            self.dataframe = GlobalDFs.readProgramsDF()
            self.column_name = "Program Code"
            self.setremovekey(program)
            self.remove_entry()

    def removeEnrollees(self, programcode):
        for student in GlobalHash.showEnrolled(programcode):
            print("Resetting key: " + student)
            self.dataframe = GlobalDFs.readStudentsDF()
            self.column_name = "ID"
            self.setremovekey(student)
            self.remove_entry()
# =====================
#    REMOVE BUTTON
# =====================      