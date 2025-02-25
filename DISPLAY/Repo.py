from DISPLAY.Table import Table
from DISPLAY.Filter import Filter
from tkinter import ttk
from DISPLAY.BUTTONS.Buttons import Buttons
from DATA import GlobalDFs

class Repo:
    def __init__(self, root, notebook, dataframe):
        self.root = root
        self.notebook = notebook
        self.dataframe = GlobalDFs.updateDF(dataframe)

        self.headers = list(dataframe.columns)

        # Table Display
        self.RepoTable = ttk.Frame(self.root, width=990, height=600)  
        self.RepoTable.grid_rowconfigure(0, weight=1) 
        self.RepoTable.grid_columnconfigure(0, weight=1)

        # Search Display
        self.searchpane = ttk.Frame(self.RepoTable)
        self.searchpane.grid(row = 1, column=0, sticky="nsew", pady=15)

        # Table Display
        self.tablepane = ttk.Frame(self.RepoTable)
        self.tablepane.grid(row = 2, column=0, sticky="nsew", pady=15)

        # Button
        self.buttonframe = ttk.Frame(self.RepoTable)
        self.buttonframe.grid(row = 3, column=0, sticky="e", pady=15)

        # Display Elements
        self.table = Table(self.tablepane, self.dataframe)
        self.search = Filter(self.searchpane, self.dataframe, self.table)
        self.button = Buttons(self.buttonframe, self.dataframe, self.table)

        self.notebook.bind("<<NotebookTabChanged>>", self.on_change)

    def on_change(self, event):
        print("Tab changed")
        selected_tab = self.notebook.select()
        tab_name = self.notebook.tab(selected_tab, "text")
        print(tab_name)

        match tab_name:
            case "Students":
                self.dataframe = GlobalDFs.readStudentsDF()
                self.table.Populate(self.table.tree, self.dataframe)
            case "Programs":
                self.dataframe = GlobalDFs.readProgramsDF()
                self.table.Populate(self.table.tree, self.dataframe)
            case "Colleges":
                self.dataframe = GlobalDFs.readCollegesDF()
                self.table.Populate(self.table.tree, self.dataframe)

    def returnFrame(self):
        return self.RepoTable