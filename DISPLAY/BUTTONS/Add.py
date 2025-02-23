from tkinter import ttk
from DISPLAY.BUTTONS import SignUp, CreateCollg, CreateProg
from DATA import GlobalDFs

class Add:
    def __init__(self, root, dataframe, table):
        self.root = root
        self.dataframe = GlobalDFs.updateDF(dataframe)
        self.table = table

        match dataframe.columns[0]:  
            case "ID":
                command = lambda: SignUp.SignUpWindow(self.table, "Add")
                buttext = "Enroll New"
            case "Program Code":
                command = lambda: CreateProg.CreateProgWindow(self.table, "Add")
                buttext = "Add Program"
            case "College Code":
                command = lambda: CreateCollg.CreateCollgWindow(self.table, "Add")
                buttext = "Add College"
            case _:
                buttext = "What, no button???"

        self.Button = ttk.Button(self.root, text=buttext, command=command)
