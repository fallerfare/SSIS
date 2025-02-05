import tkinter as tk
# import customtkinter
from tkinter import ttk
import csv

# pipenv shell --> pipenv install m

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
ProgramLabel = ttk.Label(       frame,   text="Program",                           font=('Arial', 7))
YearLabel = ttk.Label(          frame,   text="Year Level",                        font=('Arial', 7))
StatusLabel = ttk.Label(        frame,   text="Status",                            font=('Arial', 7))

# EntryBoxes
FirstNameEntryBox = ttk.Entry(  frame,   font=('Arial', 9), width = 35)
LastNameEntryBox = ttk.Entry(   frame,   font=('Arial', 9), width = 35)
EmailEntryBox = ttk.Entry(      frame,   font=('Arial', 9), width = 35)
AgeEntryBox = ttk.Entry(        frame,   font=('Arial', 9), width = 16)
IDEntryBox = ttk.Entry(         frame,   font=('Arial', 9), width = 35)

# Dropdowns

collegechoices = []
programchoices = []
with open('Colleges.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
                collegechoices.append(row['code'])

def collegechosen(event):
       College = CollegeEntryBox.get()
       programchoices.clear()

       with open('Programs.csv', 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                        if (row['collegecode']==College):
                                programchoices.append(row['code'])
                ProgramEntryBox['values'] = programchoices
                
CollegeEntryBox = ttk.Combobox( frame,  state="readonly", 
                                        values=collegechoices, 
                                        
                                        width = 35)

CollegeEntryBox.bind("<<ComboboxSelected>>", collegechosen)

ProgramEntryBox = ttk.Combobox(  frame,  state="readonly", 
                                        values=programchoices, 
                                        
                                        width = 35)

YearEntryBox = ttk.Combobox(    frame,  state="readonly", 
                                        values=["1st Year", "2nd Year", 
                                                "3rd Year", "4th Year",
                                                "5th Year and Above"            ],
                                        
                                        width = 35)

GenderEntryBox = ttk.Combobox(  frame,  state="readonly", 
                                        values=["Male", "Female", "Other"       ], 
                                        
                                        width = 16)

StatusEntryBox = ttk.Combobox( frame,   state="readonly", 
                                        values=["Student", "Admin"               ], 
                                        
                                        width = 38)

# Buttons
def SignUp():
        with open('Students.csv', 'a', newline='') as write_csv:
              csv_writer = csv.writer(write_csv)
              csv_writer.writerow([     IDEntryBox.get(),               FirstNameEntryBox.get(),        
                                        LastNameEntryBox.get(),         EmailEntryBox.get(),            
                                        YearEntryBox.get(),             GenderEntryBox.get(),        
                                        ProgramEntryBox.get(),          StatusEntryBox.get()])
SignUpButton = ttk.Button( frame, text = "Sign Up", command = SignUp) 

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
ProgramEntryBox.grid(   row=3,  column=4, columnspan = 2,   padx=7, pady=7, sticky='w')

# Row 4
EmailLabel.grid(        row=4,  column=0, columnspan = 2,   padx=5, pady=1, sticky='w')
GenderLabel.grid(       row=4,  column=2, columnspan = 1,   padx=5, pady=1, sticky='w')
AgeLabel.grid(          row=4,  column=3, columnspan = 1,   padx=5, pady=1, sticky='w')
ProgramLabel.grid(      row=4,  column=4, columnspan = 2,   padx=5, pady=1, sticky='w')

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