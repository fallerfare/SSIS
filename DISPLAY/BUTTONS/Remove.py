from tkinter import ttk
from DATA import GlobalDFs, GlobalHash

class Remove:
    def __init__(self, root, dataframe, table):
        self.root = root
        self.dataframe = dataframe
        self.originaltype = None
        self.table = table
        self.removekey = None
        self.column_name = self.dataframe.columns[0]

        # Define button behavior based on the DataFrame type
        button_config = {
            "ID": ("Remove Student", "Students"),
            "Program Code": ("Remove Program", "Programs"),
            "College Code": ("Remove College", "Colleges"),
        }
        
        buttext, self.originaltype = button_config.get(self.column_name, ("What, no button???", None))
        self.Button = ttk.Button(self.root, text=buttext, command=self.remove_entry, state="disabled")

    # Assign key to be removed
    def setremovekey(self, key):
        self.removekey = key
        print(f"Setting: {self.removekey}")

    # Remove the selected entry
    def remove_entry(self):
        if not self.removekey:
            return
        
        print(f"Removing: {self.removekey}")

        # Ensure DataFrame is up-to-date before modification
        self.dataframe = GlobalDFs.updateDF(self.dataframe)

        # Remove selected entry
        self.dataframe = self.dataframe[self.dataframe[self.column_name] != self.removekey]

        # Handle dependencies if needed
        if self.originaltype == "Students":
            GlobalDFs.writeStudentsDF(self.dataframe)
        elif self.originaltype == "Programs":
            GlobalDFs.writeProgramsDF(self.dataframe)
            self.batch_remove_students(self.removekey)  # Remove associated students
        elif self.originaltype == "Colleges":
            GlobalDFs.writeCollegesDF(self.dataframe)
            self.batch_remove_programs(self.removekey)  # Remove associated programs

        # Refresh UI
        self.refresh_tree()
        self.removekey = None

    # Refresh the treeview UI
    def refresh_tree(self):
        self.table.tree.delete(*self.table.tree.get_children())  # Clear items
        data_fetch = {
            "Students": GlobalDFs.readStudentsDF,
            "Programs": GlobalDFs.readProgramsDF,
            "Colleges": GlobalDFs.readCollegesDF,
        }
        new_data = data_fetch.get(self.originaltype, lambda: None)()
        if new_data is not None:
            self.table.Populate(self.table.tree, new_data, "Update")

    # Remove all students enrolled in a deleted program (batch processing)
    def batch_remove_students(self, program_code):
        students_df = GlobalDFs.readStudentsDF()
        enrolled_students = GlobalHash.showEnrolled(program_code)  # Get students from hash
        students_df = students_df[~students_df["ID"].isin(enrolled_students)]  # Remove in batch
        GlobalDFs.writeStudentsDF(students_df)

    # Remove all programs linked to a deleted college (batch processing)
    def batch_remove_programs(self, college_code):
        programs_df = GlobalDFs.readProgramsDF()
        programs_to_remove = GlobalHash.showDegrees(college_code)  # Get programs from hash
        programs_df = programs_df[~programs_df["Program Code"].isin(programs_to_remove)]  # Remove in batch
        GlobalDFs.writeProgramsDF(programs_df)
        for program in programs_to_remove:
            self.batch_remove_students(program)  # Remove students linked to deleted programs