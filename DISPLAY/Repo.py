from DISPLAY.Table import Table
from DISPLAY.Filter import Filter
from tkinter import ttk
from DISPLAY.BUTTONS.Buttons import Buttons
from DATA import GlobalDFs

class Repo(ttk.Frame):
    def __init__(self, root, dataframe):
        super().__init__(root)
        self.dataframe = GlobalDFs.updateDF(dataframe)

        self.headers = list(dataframe.columns)

        # Table Display
        RepoTable = ttk.Frame(self, width = 990)
        RepoTable.pack(padx = 20, pady = 20, anchor= "center")

        # Search Display
        searchpane = ttk.Frame(RepoTable)
        searchpane.grid(row = 1, column=0, sticky="nsew", pady=15)

        # Table Display
        tablepane = ttk.Frame(RepoTable)
        tablepane.grid(row = 2, column=0, sticky="nsew", pady=15)

        # Button
        buttonframe = ttk.Frame(RepoTable)
        buttonframe.grid(row = 3, column=0, sticky="e", pady=15)

        # Display Elements
        table = Table(tablepane, self.dataframe)
        search = Filter(searchpane, self.dataframe, table)
        button = Buttons(buttonframe, self.dataframe, table)
