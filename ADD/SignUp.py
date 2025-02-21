from tkinter import ttk
import pandas as pd
import TKinterModernThemes as TKMT


def SignUpWindow():

    # MAIN WINDOW

    window = TKMT.ThemedTKinterFrame("MSU-IIT Students","azure","dark")
    window.root.geometry("900x400")
    window.root.resizable(width=False, height=False)

    frame = ttk.Frame(window.root)
    frame.pack(padx=20, pady=20, anchor = "center")

    # Separate dataframes
    Programs = pd.read_csv(r'DATA\Programs.csv')
    Colleges = pd.read_csv(r'DATA\Colleges.csv')


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
    FirstNameEntryBox = ttk.Entry(  frame,   font=('Arial', 9),                         width = 35)
    LastNameEntryBox = ttk.Entry(   frame,   font=('Arial', 9),                         width = 35)
    EmailEntryBox = ttk.Entry(      frame,   font=('Arial', 9),                         width = 35)
    AgeEntryBox = ttk.Entry(        frame,   font=('Arial', 9),                         width = 14)
    IDEntryBox = ttk.Entry(         frame,   font=('Arial', 9),                         width = 35)

    # Dropdowns

    collegechoices = list(Colleges['College Code'])
    programchoices = []

    def collegechosen(event):
        College = CollegeEntryBox.get()
        
        # Filter programs based on selected college
        programsincollege = Programs[Programs['College Code'] == College]['Program Code'].tolist()

        # Update the combobox values
        ProgramEntryBox['values'] = programsincollege
        
        # Clear any previous selection
        ProgramEntryBox.set('')
                    
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
        newStudentdata = {  
            'ID Number':    [IDEntryBox.get()],
            'First Name':   [FirstNameEntryBox.get()],
            'Last Name':    [LastNameEntryBox.get()],
            'Email':        [EmailEntryBox.get()],
            'Year Level':   [YearEntryBox.get()],
            'Gender':       [GenderEntryBox.get()],
            'Program':      [ProgramEntryBox.get()],
            'Status':       [StatusEntryBox.get()]
        }

        newStudentdf = pd.DataFrame(newStudentdata)
        newStudentdf.to_csv('DATA\Students.csv', mode='a', header=False, index=False)

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

    window.root.mainloop()