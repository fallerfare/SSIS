from tkinter import ttk
from DATA import GlobalDFs

class Filter():
    def __init__(self, root, dataframe, table):
        self.root = root
        self.dataframe = GlobalDFs.updateDF(dataframe)
        self.table = table

        searchnsortframe = ttk.Frame(root)
        searchnsortframe.pack(anchor="center")

        searchlabel = ttk.Label(searchnsortframe, text="Search", font=('Arial', 12))
        sortwithlabel = ttk.Label(searchnsortframe, text="Sort with", font=('Arial', 12))
        sortbylabel = ttk.Label(searchnsortframe, text="Sort by", font=('Arial', 12))

        self.searchbar = ttk.Entry(searchnsortframe, font=('Arial', 9), width=20)

        self.sortwithbar = ttk.Combobox(searchnsortframe, state="readonly",
                                        values=list(self.dataframe.columns),
                                        width=15)

        self.sortbybar = ttk.Combobox(searchnsortframe, state="readonly",
                                      values=["Ascending", "Descending"],
                                      width=15)

        self.searchbar.bind("<KeyRelease>", self.perform_search)
        self.sortwithbar.bind("<<ComboboxSelected>>", self.perform_sort)
        self.sortbybar.bind("<<ComboboxSelected>>", self.perform_sort)

        searchlabel.grid(row=0, column=0)
        self.searchbar.grid(row=0, column=1)
        sortwithlabel.grid(row=0, column=2)
        self.sortwithbar.grid(row=0, column=3)
        sortbylabel.grid(row=0, column=4)
        self.sortbybar.grid(row=0, column=5)

    def perform_search(self, event):
        search_term = self.searchbar.get().lower()
        self.dataframe = GlobalDFs.updateDF(self.dataframe)  # Ensure latest dataframe
        self.table.dataframe = GlobalDFs.updateDF(self.table.dataframe)  # Ensure table has updated dataframe
        
        if self.table.dataframe.empty:
            return

        filtered_df = self.table.dataframe[
            self.table.dataframe.apply(lambda row: row.astype(str).str.lower().str.contains(search_term).any(), axis=1)
        ]

        self.table.Populate(self.table.tree, filtered_df, "Filter")

    def perform_sort(self, event):
        self.dataframe = GlobalDFs.updateDF(self.dataframe)
        self.table.dataframe = GlobalDFs.updateDF(self.table.dataframe)  # Ensure table has updated dataframe

        sortwithkey = self.sortwithbar.get()
        sortbykey = self.sortbybar.get()

        if not sortwithkey or not sortbykey or self.table.dataframe.empty:
            return

        ascending = sortbykey == "Ascending"

        sorted_df = self.table.dataframe.sort_values(by=[sortwithkey], ascending=ascending)

        self.table.dataframe = sorted_df
        self.table.Populate(self.table.tree, sorted_df, "Filter")
