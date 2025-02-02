import tkinter as tk
# import customtkinter
from tkinter import Grid, ttk

# MAIN WINDOW

root = tk.Tk()
root.geometry("780x420")
root.title("MSU-IIT Students")
root.resizable(width=True, height=True)

frame = ttk.Frame(root)
frame.pack(padx=20, pady=20, fill='both', expand=True)

# WIDGETS

#Header
Header = ttk.Label(             frame,   text="Welcome to MSU-IIT",                font=('Arial', 20))

# Labels
FirstNameLabel = ttk.Label(     frame,   text="First Name",                        font=('Arial', 7))
LastNameLabel = ttk.Label(      frame,   text="Last Name",                         font=('Arial', 7))
EmailLabel = ttk.Label(         frame,   text="Email",                             font=('Arial', 7))
AgeLabel = ttk.Label(           frame,   text="Age",                               font=('Arial', 7))
IDLabel = ttk.Label(            frame,   text="ID Number(YYYY-NNNN)",              font=('Arial', 7))
GenderLabel = ttk.Label(        frame,   text="Gender",                            font=('Arial', 7))
CollegeLabel = ttk.Label(       frame,   text="College",                           font=('Arial', 7))
CourseLabel = ttk.Label(        frame,   text="Course",                            font=('Arial', 7))
YearLabel = ttk.Label(          frame,   text="Year Level",                        font=('Arial', 7))
StatusLabel = ttk.Label(        frame,   text="Status",                            font=('Arial', 7))

# EntryBoxes
FirstNameEntryBox = ttk.Entry(  frame,   font=('Arial', 9), width = 35)
LastNameEntryBox = ttk.Entry(   frame,   font=('Arial', 9), width = 35)
EmailEntryBox = ttk.Entry(      frame,   font=('Arial', 9), width = 35)
AgeEntryBox = ttk.Entry(        frame,   font=('Arial', 9), width = 16)
IDEntryBox = ttk.Entry(         frame,   font=('Arial', 9), width = 35)

# Dropdowns
YearEntryBox = ttk.Combobox(    frame,  state="readonly", 
                                        values=["1st Year", "2nd Year", 
                                                "3rd Year", "4th Year"          ], 
                                        
                                        width = 35)

GenderEntryBox = ttk.Combobox(  frame,  state="readonly", 
                                        values=["Male", "Female", "Other"       ], 
                                        
                                        width = 16)

CollegeEntryBox = ttk.Combobox( frame,  state="readonly", 
                                        values=["College of Science", 
                                                "College of Arts", 
                                                "College of Engineering", 
                                                "College of Business"           ], 
                                        
                                        width = 35)

CourseEntryBox = ttk.Combobox(  frame,  state="readonly", 
                                        values=["Computer Science", 
                                                "Business Administration", 
                                                "Civil Engineering", 
                                                "Psychology"                    ], 
                                        
                                        width = 35)

StatusEntryBox = ttk.Combobox( frame,   state="readonly", 
                                        values=["Computer Science", 
                                                "Business Administration", 
                                                "Civil Engineering", 
                                                "Psychology"                    ], 
                                        
                                        width = 38)

# Buttons
SignUpButton = ttk.Button( frame, text = "Sign Up") 

# GRID SETUP

# Row 0
Header.grid(            row=0,  column=0, columnspan = 6,   padx=20, pady=20)

# Row 1
FirstNameEntryBox.grid( row=1,  column=0, columnspan = 2,   padx=7, pady=7, sticky='w')
LastNameEntryBox.grid(  row=1,  column=2, columnspan = 2,   padx=7, pady=7, sticky='w')
CollegeEntryBox.grid(   row=1,  column=4, columnspan = 2,   padx=7, pady=7, sticky='w')

# Row 2
FirstNameLabel.grid(    row=2,  column=0, columnspan = 2,   padx=5, pady=1, sticky='w')
LastNameLabel.grid(     row=2,  column=2, columnspan = 2,   padx=5, pady=1, sticky='w')
CollegeLabel.grid(      row=2,  column=4, columnspan = 2,   padx=5, pady=1, sticky='w')

# Row 3
EmailEntryBox.grid(     row=3,  column=0, columnspan = 2,   padx=7, pady=7, sticky='w')
GenderEntryBox.grid(    row=3,  column=2, columnspan = 1,   padx=2, pady=7, sticky='w')
AgeEntryBox.grid(       row=3,  column=3, columnspan = 1,   padx=2, pady=7, sticky='w')
CourseEntryBox.grid(    row=3,  column=4, columnspan = 2,   padx=7, pady=7, sticky='w')

# Row 4
EmailLabel.grid(        row=4,  column=0, columnspan = 2,   padx=5, pady=1, sticky='w')
GenderLabel.grid(       row=4,  column=2, columnspan = 1,   padx=5, pady=1, sticky='w')
AgeLabel.grid(          row=4,  column=3, columnspan = 1,   padx=5, pady=1, sticky='w')
CourseLabel.grid(       row=4,  column=4, columnspan = 2,   padx=5, pady=1, sticky='w')

# Row 5
StatusEntryBox.grid(    row=5,  column=0, columnspan = 2,   padx=7, pady=7, sticky='w')
IDEntryBox.grid(        row=5,  column=2, columnspan = 2,   padx=7, pady=7, sticky='w')
YearEntryBox.grid(      row=5,  column=4, columnspan = 2,   padx=7, pady=7, sticky='w')

# Row 6
StatusLabel.grid(       row=6,  column=0, columnspan = 2,   padx=5, pady=1, sticky='w')
IDLabel.grid(           row=6,  column=2, columnspan = 2,   padx=5, pady=1, sticky='w')
YearLabel.grid(         row=6,  column=4, columnspan = 2,   padx=5, pady=1, sticky='w')

# Row 7
SignUpButton.grid(      row=7,  column=4, columnspan = 2,   padx=5, pady=2, sticky='e')

# Grid Configurations
for i in range(7):  # 3 columns
    frame.columnconfigure(      i, weight=1)  # Allow all columns to expand

for i in range(8):  # 11 rows
    frame.rowconfigure(         i, weight=1)  # Allow all rows to expand

root.mainloop()