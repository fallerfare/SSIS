import tkinter as tk
from tkinter import Grid, ttk

# MAIN WINDOW

root = tk.Tk()
root.geometry("780x420")
root.title("MSU-IIT Students")

# WIDGETS

#Header
Header = ttk.Label(             root,   text="Welcome to MSU-IIT",                font=('Arial', 20))

# Labels
FirstNameLabel = ttk.Label(     root,   text="First Name",                        font=('Arial', 7))
LastNameLabel = ttk.Label(      root,   text="Last Name",                         font=('Arial', 7))
EmailLabel = ttk.Label(         root,   text="Email",                             font=('Arial', 7))
AgeLabel = ttk.Label(           root,   text="Age",                               font=('Arial', 7))
IDLabel = ttk.Label(            root,   text="ID Number(YYYY-NNNN)",              font=('Arial', 7))
GenderLabel = ttk.Label(        root,   text="Gender",                            font=('Arial', 7))
CollegeLabel = ttk.Label(       root,   text="College",                           font=('Arial', 7))
CourseLabel = ttk.Label(        root,   text="Course",                            font=('Arial', 7))
YearLabel = ttk.Label(          root,   text="Year Level",                        font=('Arial', 7))
StatusLabel = ttk.Label(        root,   text="Status",                            font=('Arial', 7))

# EntryBoxes
FirstNameEntryBox = ttk.Entry(  root,   font=('Arial', 9), width = 35)
LastNameEntryBox = ttk.Entry(   root,   font=('Arial', 9), width = 35)
EmailEntryBox = ttk.Entry(      root,   font=('Arial', 9), width = 35)
AgeEntryBox = ttk.Entry(        root,   font=('Arial', 9), width = 16)
IDEntryBox = ttk.Entry(         root,   font=('Arial', 9), width = 35)

# Dropdowns
YearEntryBox = ttk.Combobox(    root,   state="readonly", 
                                        values=["1st Year", "2nd Year", 
                                                "3rd Year", "4th Year"], 
                                                width = 35)

GenderEntryBox = ttk.Combobox(  root,   state="readonly", 
                                        values=["Male", "Female", "Other"], 
                                        width = 16)

CollegeEntryBox = ttk.Combobox( root,   state="readonly", 
                                        values=["College of Science", "College of Arts", 
                                                "College of Engineering", "College of Business"], 
                                        width = 35)

CourseEntryBox = ttk.Combobox(  root,   state="readonly", 
                                        values=["Computer Science", "Business Administration", 
                                                "Civil Engineering", "Psychology"], 
                                        width = 35)

StatusEntryBox = ttk.Combobox( root,   state="readonly", 
                                        values=["Computer Science", "Business Administration", 
                                                "Civil Engineering", "Psychology"], 
                                        width = 38)

# Buttons
SignUpButton = ttk.Button( root, text = "Sign Up") 

# GRID SETUP

# Row 0
Header.grid(            row=0,  column=0, columnspan = 6,   padx=20, pady=20)

# Row 1
FirstNameEntryBox.grid( row=1,  column=0, columnspan = 2,   padx=7, pady=7)
LastNameEntryBox.grid(  row=1,  column=2, columnspan = 2,   padx=7, pady=7)
CollegeEntryBox.grid(   row=1,  column=4, columnspan = 2,   padx=7, pady=7)

# Row 2
FirstNameLabel.grid(    row=2,  column=0, columnspan = 2,   padx=5, pady=1, sticky='w')
LastNameLabel.grid(     row=2,  column=2, columnspan = 2,   padx=5, pady=1, sticky='w')
CollegeLabel.grid(      row=2,  column=4, columnspan = 2,   padx=5, pady=1, sticky='w')

# Row 3
EmailEntryBox.grid(     row=3,  column=0, columnspan = 2,   padx=7, pady=7)
GenderEntryBox.grid(    row=3,  column=2, columnspan = 1,   padx=2, pady=7)
AgeEntryBox.grid(       row=3,  column=3, columnspan = 1,   padx=2, pady=7)
CourseEntryBox.grid(    row=3,  column=4, columnspan = 2,   padx=7, pady=7)

# Row 4
EmailLabel.grid(        row=4,  column=0, columnspan = 2,   padx=5, pady=1, sticky='w')
GenderLabel.grid(       row=4,  column=2, columnspan = 1,   padx=5, pady=1, sticky='w')
AgeLabel.grid(          row=4,  column=3, columnspan = 1,   padx=5, pady=1, sticky='w')
CourseLabel.grid(       row=4,  column=4, columnspan = 2,   padx=5, pady=1, sticky='w')

# Row 5
StatusEntryBox.grid(    row=5,  column=0, columnspan = 2,   padx=7, pady=7)
IDEntryBox.grid(        row=5,  column=2, columnspan = 2,   padx=7, pady=7)
YearEntryBox.grid(      row=5,  column=4, columnspan = 2,   padx=7, pady=7)

# Row 6
StatusLabel.grid(       row=6,  column=0, columnspan = 2,   padx=5, pady=1, sticky='w')
IDLabel.grid(           row=6,  column=2, columnspan = 2,   padx=5, pady=1, sticky='w')
YearLabel.grid(         row=6,  column=4, columnspan = 2,   padx=5, pady=1, sticky='w')

# Row 7
SignUpButton.grid(      row=7,  column=4, columnspan = 2,   padx=5, pady=2, sticky='e')

# Grid Configurations
# Grid.rowconfigure(      root, 0, weight=3)
# Grid.rowconfigure(      root, 1, weight=1)
# Grid.rowconfigure(      root, 2, weight=1)
# Grid.rowconfigure(      root, 3, weight=1)
# Grid.rowconfigure(      root, 4, weight=1)
# Grid.rowconfigure(      root, 5, weight=1)
# Grid.rowconfigure(      root, 6, weight=1)
# Grid.rowconfigure(      root, 7, weight=1)

# Grid.columnconfigure(   root, 0, weight=1)
# Grid.columnconfigure(   root, 1, weight=1)
# Grid.columnconfigure(   root, 2, weight=1)
# Grid.columnconfigure(   root, 3, weight=1)
# Grid.columnconfigure(   root, 4, weight=1)
# Grid.columnconfigure(   root, 5, weight=1)
# Grid.columnconfigure(   root, 6, weight=1)

root.mainloop()