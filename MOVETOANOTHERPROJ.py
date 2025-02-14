# from tkinter import *
# import pandas as pd
# from tkinter import ttk, filedialog

# root = Tk()
# root.title("Ulol")
# root.geometry("500x500")

# def file_open():
#     # Open file dialog to select a CSV file
#     filename = filedialog.askopenfilename(
#         initialdir="C:/Users/joshu/Documents/2ND_YEAR_NOTES/CCC186/Project_1/",
#         title="Open",
#         filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
#     )

#     if filename:  # Check if a file was selected
#         # Read the CSV file into a DataFrame
#         df = pd.read_csv(filename)

#         cleartree()  # Clear existing data in the Treeview

#         # Set the columns of the Treeview
#         mytree["columns"] = list(df.columns)
#         mytree["show"] = "headings"

#         for column in mytree["columns"]:
#             mytree.heading(column, text=column)

#         # Insert the DataFrame rows into the Treeview
#         dfrows = df.to_numpy().tolist()
#         for row in dfrows:
#             mytree.insert("", "end", values=row)

#         mytree.pack()

# def cleartree():
#     mytree.delete(*mytree.get_children())

# # Create a frame for the Treeview
# frame = Frame(root)
# frame.pack(pady=20)

# # Create the Treeview
# mytree = ttk.Treeview(frame)

# # Create a menu
# mmenu = Menu(root)
# root.config(menu=mmenu)

# filemenu = Menu(mmenu, tearoff=False)
# mmenu.add_cascade(label="Spreadsheets", menu=filemenu)
# filemenu.add_command(label="Open", command=file_open)

# # Pack the Treeview
# mytree.pack()

# # Start the Tkinter main loop
# root.mainloop()


import tkinter as tk
from tkinter import ttk
import pandas as pd

def create_treeview(root, dataframe):

    # Create a Treeview widget
    tree = ttk.Treeview(root)

    # Define columns
    tree['columns'] = list(dataframe.columns)
    tree['show'] = 'headings'  # Hide the first empty column

    # Create headings
    for col in dataframe.columns:
        tree.heading(col, text=col)  # Set the column heading
        tree.column(col, anchor='center')  # Center align the column

    # Insert data into the treeview
    for index, row in dataframe.iterrows():
        tree.insert("", "end", values=list(row))

    # Pack the treeview into the window
    tree.pack(expand=True, fill='both')

    # Run the application

# Call the function with the DataFrame

if __name__=="__main__":
     # Create the main window
    root = tk.Tk()
    root.title("Treeview Example")
    
    df = pd.read_csv('Students.csv')

    create_treeview(root, df)
    root.mainloop()