import tkinter as tk
# import customtkinter
from tkinter import ttk
import csv
# import PyQt6
# import pandas as pd

# # TABLE
# class TableApp:
#         def __init__(self, root, StudentsFile):
#                 self.root = root

#                 # self.df = pd.read_csv(StudentsFile)

#                 frame = ttk.Frame(root)
#                 frame.grid(row=0, column=0, sticky='nsew')

#                 self.tree = ttk.Treeview(frame, show = 'headings')
#                 self.tree.grid(row=0, column=0, sticky='nsew')

#                 scrollbar = ttk.Scrollbar(frame, orient = "vertical", command = self.tree.yview)
#                 self.tree.configure(yscroll = scrollbar.set)
#                 scrollbar.grid(row=0, column=1, sticky='ns')

#                 with open(StudentsFile, newline = '') as t:
#                         StudentDetails = csv.reader(t)
#                         headers = next(StudentDetails)
#                         self.tree['columns'] = headers

#                         for header in headers:
#                                 self.tree.heading(header, text = header)
#                                 self.tree.column(header, anchor = 'center')

#                         for row in StudentDetails:
#                                 self.tree.insert("","end",values=row)


# MAIN WINDOW
if __name__ =="__main__":
        root = tk.Tk()
        root.geometry("900x860")
        root.title("MSU-IIT Students")
        root.resizable(width=True, height=True)

        # Panedwindow
        paned = ttk.PanedWindow(root, width = 800)
        paned.grid(row=1, column=0, pady=(25, 5), sticky="nsew")

        # Pane #1
        pane_1 = ttk.Frame(paned)
        paned.add(pane_1, weight=1)

        # Create a Frame for the Treeview
        treeFrame = ttk.Frame(pane_1)
        treeFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Scrollbar
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")

        # Treeview
        treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=12)
        treeview.pack(expand=True, fill="both")
        treeScroll.config(command=treeview.yview)

        # Treeview columns
        treeview.column("#0", width=120)
        treeview.column(1, anchor="w", width=120)
        treeview.column(2, anchor="w", width=120)

        # Treeview headings
        treeview.heading("#0", text="Column 1", anchor="center")
        treeview.heading(1, text="Column 2", anchor="center")
        treeview.heading(2, text="Column 3", anchor="center")

        # Define treeview data
        treeview_data = [
        ("", "end", 1, "Parent", ("Item 1", "Value 1")),
        (1, "end", 2, "Child", ("Subitem 1.1", "Value 1.1")),
        (1, "end", 3, "Child", ("Subitem 1.2", "Value 1.2")),
        (1, "end", 4, "Child", ("Subitem 1.3", "Value 1.3")),
        (1, "end", 5, "Child", ("Subitem 1.4", "Value 1.4")),
        ("", "end", 6, "Parent", ("Item 2", "Value 2")),
        (6, "end", 7, "Child", ("Subitem 2.1", "Value 2.1")),
        (6, "end", 8, "Sub-parent", ("Subitem 2.2", "Value 2.2")),
        (8, "end", 9, "Child", ("Subitem 2.2.1", "Value 2.2.1")),
        (8, "end", 10, "Child", ("Subitem 2.2.2", "Value 2.2.2")),
        (8, "end", 11, "Child", ("Subitem 2.2.3", "Value 2.2.3")),
        (6, "end", 12, "Child", ("Subitem 2.3", "Value 2.3")),
        (6, "end", 13, "Child", ("Subitem 2.4", "Value 2.4")),
        ("", "end", 14, "Parent", ("Item 3", "Value 3")),
        (14, "end", 15, "Child", ("Subitem 3.1", "Value 3.1")),
        (14, "end", 16, "Child", ("Subitem 3.2", "Value 3.2")),
        (14, "end", 17, "Child", ("Subitem 3.3", "Value 3.3")),
        (14, "end", 18, "Child", ("Subitem 3.4", "Value 3.4")),
        ("", "end", 19, "Parent", ("Item 4", "Value 4")),
        (19, "end", 20, "Child", ("Subitem 4.1", "Value 4.1")),
        (19, "end", 21, "Sub-parent", ("Subitem 4.2", "Value 4.2")),
        (21, "end", 22, "Child", ("Subitem 4.2.1", "Value 4.2.1")),
        (21, "end", 23, "Child", ("Subitem 4.2.2", "Value 4.2.2")),
        (21, "end", 24, "Child", ("Subitem 4.2.3", "Value 4.2.3")),
        (19, "end", 25, "Child", ("Subitem 4.3", "Value 4.3"))
        ]

        # Insert treeview data
        for item in treeview_data:
                treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])
                if item[0] == "" or item[2] in (8, 12):
                        treeview.item(item[2], open=True) # Open parents

        # Select and scroll
        treeview.selection_set(10)
        treeview.see(7)


        # table = TableApp(root, csv_file)

        root.mainloop()