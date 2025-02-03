import tkinter as tk
# import customtkinter
from tkinter import ttk
import csv
# import pandas as pd

# TABLE
class TableApp:
        def __init__(self, root, StudentsFile):
                self.root = root

                # self.df = pd.read_csv(StudentsFile)

                frame = ttk.Frame(root)
                frame.grid(row=0, column=0, sticky='nsew')

                self.tree = ttk.Treeview(frame, show = 'headings')
                self.tree.grid(row=0, column=0, sticky='nsew')

                scrollbar = ttk.Scrollbar(frame, orient = "vertical", command = self.tree.yview)
                self.tree.configure(yscroll = scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns')

                with open(StudentsFile, newline = '') as t:
                        StudentDetails = csv.reader(t)
                        headers = next(StudentDetails)
                        self.tree['columns'] = headers

                        for header in headers:
                                self.tree.heading(header, text = header)
                                self.tree.column(header, anchor = 'center')

                        for row in StudentDetails:
                                self.tree.insert("","end",values=row)

# MAIN WINDOW
if __name__ =="__main__":
        root = tk.Tk()
        root.geometry("900x860")
        root.title("MSU-IIT Students")
        root.resizable(width=True, height=True)

        csv_file = 'Students.csv'

        table = TableApp(root, csv_file)

        root.mainloop()