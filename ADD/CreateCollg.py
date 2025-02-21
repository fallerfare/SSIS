from tkinter import ttk
import pandas as pd
import TKinterModernThemes as TKMT

def CreateCollgWindow():

    # MAIN WINDOW

    window = TKMT.ThemedTKinterFrame("MSU-IIT Students","azure","dark")
    window.root.geometry("900x400")
    window.root.resizable(width=False, height=False)

    frame = ttk.Frame(window.root)
    frame.pack(padx=20, pady=20, anchor = "center")

    # WIDGETS

    #Header
    Header = ttk.Label(                 frame,   text="Add College",        font=('Arial', 20))

    # Labels
    CollegeNameLabel    = ttk.Label(    frame,   text="College Name",       font=('Arial', 7))
    CollegeCodeLabel    = ttk.Label(    frame,   text="College Code",       font=('Arial', 7))

    # EntryBoxes
    CollegeNameEntryBox = ttk.Entry(    frame,   font=('Arial', 9),         width = 35)
    CollegeCodeEntryBox = ttk.Entry(    frame,   font=('Arial', 9),         width = 35)

    # Buttons
    def CreateProg():
        newCollegedata = {  
            'College Name': [CollegeNameEntryBox.get()],
            'College Code': [CollegeCodeEntryBox.get()]
        }

        newCollegedf = pd.DataFrame(newCollegedata)
        newCollegedf.to_csv('DATA\Colleges.csv', mode='a', header=False, index=False)

    CreateProgButton = ttk.Button( frame, text = "Add College", command = CreateProg) 

    # GRID SETUP

    # Row 0
    Header.grid(                row=0,  column=0, columnspan = 6,   padx=20, pady=20)

    # Row 1
    CollegeNameEntryBox.grid(   row=1,  column=0, columnspan = 2,   padx=7, pady=7, sticky='w')
    CollegeCodeEntryBox.grid(   row=1,  column=2, columnspan = 2,   padx=7, pady=7, sticky='w')

    # Row 2
    CollegeNameLabel.grid(      row=2,  column=0, columnspan = 2,   padx=5, pady=1, sticky='w')
    CollegeCodeLabel.grid(      row=2,  column=2, columnspan = 2,   padx=5, pady=1, sticky='w')

    # Row 7
    CreateProgButton.grid(      row=7,  column=4, columnspan = 2,   padx=5, pady=2, sticky='e')

    window.root.mainloop()