from tkinter import ttk
import pandas as pd
import TKinterModernThemes as TKMT


def CreateProgWindow():

    # MAIN WINDOW

    window = TKMT.ThemedTKinterFrame("MSU-IIT Students","azure","dark")
    window.root.geometry("900x400")
    window.root.resizable(width=False, height=False)

    frame = ttk.Frame(window.root)
    frame.pack(padx=20, pady=20, anchor = "center")

    # dataframe
    Colleges = pd.read_csv(r'DATA\Colleges.csv')


    # WIDGETS

    #Header
    Header = ttk.Label(                 frame,   text="Add a Program",      font=('Arial', 20))

    # Labels
    ProgramNameLabel    = ttk.Label(    frame,   text="Program Name",       font=('Arial', 7))
    ProgramCodeLabel    = ttk.Label(    frame,   text="Program Code",       font=('Arial', 7))
    CollegeLabel        = ttk.Label(    frame,   text="College",            font=('Arial', 7))

    # EntryBoxes
    ProgramNameEntryBox = ttk.Entry(    frame,   font=('Arial', 9),         width = 35)
    ProgramCodeEntryBox = ttk.Entry(    frame,   font=('Arial', 9),         width = 35)

    # Dropdowns

    collegechoices = list(Colleges['College Code'])
                    
    CollegeEntryBox = ttk.Combobox( frame,  state="readonly", 
                                            values=collegechoices, 
                                            
                                            width = 35)

    # Buttons
    def CreateProg():
        newProgramdata = {  
            'Program Name': [ProgramNameEntryBox.get()],
            'Program Code': [ProgramCodeEntryBox.get()],
            'College Code': [CollegeEntryBox.get()]
        }

        newProgramdf = pd.DataFrame(newProgramdata)
        newProgramdf.to_csv('DATA\Programs.csv', mode='a', header=False, index=False)

    CreateProgButton = ttk.Button( frame, text = "Add Program", command = CreateProg) 

    # GRID SETUP

    # Row 0
    Header.grid(                row=0,  column=0, columnspan = 6,   padx=20, pady=20)

    # Row 1
    ProgramNameEntryBox.grid(   row=1,  column=0, columnspan = 2,   padx=7, pady=7, sticky='w')
    ProgramCodeEntryBox.grid(   row=1,  column=2, columnspan = 2,   padx=7, pady=7, sticky='w')
    CollegeEntryBox.grid(       row=1,  column=4, columnspan = 2,   padx=7, pady=7, sticky='w')

    # Row 2
    ProgramNameLabel.grid(      row=2,  column=0, columnspan = 2,   padx=5, pady=1, sticky='w')
    ProgramCodeLabel.grid(      row=2,  column=2, columnspan = 2,   padx=5, pady=1, sticky='w')
    CollegeLabel.grid(          row=2,  column=4, columnspan = 2,   padx=5, pady=1, sticky='w')

    # Row 7
    CreateProgButton.grid(      row=7,  column=4, columnspan = 2,   padx=5, pady=2, sticky='e')

    window.root.mainloop()