from tkinter import ttk
import pandas as pd
import tkinter as tk
from DATA import GlobalDFs
from EXCEPTIONS import Exceptions

class CreateCollgWindow:
    def __init__(self, table, Wintype):
        self.table = table
        self.WinType = Wintype

        self.root = tk.Toplevel()
        self.root.geometry("900x400")
        self.root.resizable(width=False, height=False)

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=20, pady=20, anchor="center")

        # WIDGETS
        self.Header = ttk.Label(self.frame, text="Add College", font=('Arial', 20))

        # Labels
        self.CollegeNameLabel = ttk.Label(self.frame, text="College Name", font=('Arial', 7))
        self.CollegeCodeLabel = ttk.Label(self.frame, text="College Code", font=('Arial', 7))

        # EntryBoxes
        self.CollegeNameEntryBox = ttk.Entry(self.frame, font=('Arial', 9), width=35)
        self.CollegeCodeEntryBox = ttk.Entry(self.frame, font=('Arial', 9), width=35)

        # Buttons
        self.CreateCollgButton = ttk.Button(self.frame, text="Add College", command=self.CreateCollg)

        # GRID SETUP
        self.Header.grid(row=0, column=0, columnspan=6, padx=20, pady=20)

        # Row 1
        self.CollegeNameEntryBox.grid(row=1, column=0, columnspan=2, padx=7, pady=7, sticky='w')
        self.CollegeCodeEntryBox.grid(row=1, column=2, columnspan=2, padx=7, pady=7, sticky='w')

        # Row 2
        self.CollegeNameLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=1, sticky='w')
        self.CollegeCodeLabel.grid(row=2, column=2, columnspan=2, padx=5, pady=1, sticky='w')

        # Row 7
        self.CreateCollgButton.grid(row=7, column=4, columnspan=2, padx=5, pady=2, sticky='e')

        self.root.mainloop()

    def CreateCollg(self):
        try:

            college_name = self.CollegeNameEntryBox.get().strip()
            college_code = self.CollegeCodeEntryBox.get().strip()
            
            Exceptions.validate_inputs({
                                        "College Name" : (college_name, Exceptions.CollegeEntry),
                                        "College Code" : (college_code, Exceptions.CodeEntry)

            })

            if self.WinType == "Add":
                newCollegedata = {
                'College Name': [college_name],
                'College Code': [college_code]
                }

                newCollegedf = pd.DataFrame(newCollegedata)
                newdataframe = pd.concat([GlobalDFs.readCollegesDF(), newCollegedf], ignore_index=True)

            elif self.WinType == "Edit":
                selected_item = self.table.tree.selection()
                item_values = self.table.tree.item(selected_item, "values")
                new_item_values = list(item_values)

                new_item_values[0] = college_code
                new_item_values[1] = college_name

                newdataframe = GlobalDFs.readCollegesDF()

                selected_row_index = list(newdataframe.index[newdataframe['ID'] == item_values[0]])

                if selected_row_index:
                    newdataframe.loc[selected_row_index[0]] = new_item_values

            GlobalDFs.writeCollegesDF(newdataframe)
            self.table.Populate(self.table.tree, newdataframe)

            self.root.destroy()

        except ValueError as ve:
            Exceptions.show_inputerror_message(ve)
        except Exception as e:
            Exceptions.show_unexpected_error(e)
        
