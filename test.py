import tkinter as tk
# import customtkinter
from tkinter import ttk
import csv


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
        Repository = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=12, show='headings')
        Repository.pack(expand=True, fill="both")
        treeScroll.config(command=Repository.yview)

        canvas = tk.Canvas(treeFrame, bg="white")
        canvas.pack(expand=True, fill="both")

        with open('Students.csv', newline = '') as t:
                          StudentDetails = csv.reader(t)
                          headers = next(StudentDetails)
                          Repository['columns'] = headers

                          for header in headers:
                                i = 1
                                Repository.heading(header, text = header)
                                Repository.column(header, anchor = 'center')

                          for row in StudentDetails:
                                Repository.insert("","end",values=row)

                                x = Repository.bbox(i)[0] + Repository.winfo_x()  # Get the x position of the column
                                canvas.create_line(x, 0, x, treeFrame.winfo_height(), fill="black")

                                y = Repository.bbox(i)[0] + Repository.winfo_y()  # Get the x position of the column
                                canvas.create_line(0, y, treeFrame.winfo_width(), fill="black")

                
        for i in range(1, 3, 5, 7):  
                y = Repository.bbox(i)[1] + Repository.winfo_y()  # Get the y position of the column
                canvas.create_line(y, 0, y, treeFrame.winfo_wight(), fill="black")

        # Define the columns
        Repository.column(0, width=75, anchor="center")
        Repository.column(1, width=100, anchor="center")          
        Repository.column(2, width=100, anchor="center")  
        Repository.column(3, width=100, anchor="center")  
        Repository.column(4, width=100, anchor="center")  
        Repository.column(5, width=100, anchor="center")  
        Repository.column(6, width=100, anchor="center")  
        Repository.column(7, width=100, anchor="center") 

        root.mainloop()