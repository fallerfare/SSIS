from tkinter import messagebox
from DATA import GlobalHash
import re



# =======================
# ACCEPTED ENTRY FORMATS
# =======================
NormalEntry = re.compile(r"^[A-Z][a-z]+(?:\s[A-Z][a-z]+)*$")
ProgramEntry = re.compile(r"^Bachelor of [A-Za-z\s]+$")
CollegeEntry = re.compile(r"^College of [A-Za-z\s]+$")
IDEntry = re.compile(r"^\d{4}-\d{4}$")
EmailEntry = re.compile(r"^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}$")
CodeEntry = re.compile(r"^[A-Za-z]{3,6}$")
YearEntry = re.compile(r"^[1-5](st|nd|rd|th) (Year|Year and Above)$")
# =======================
# ACCEPTED ENTRY FORMATS
# =======================



# =======================
#      CHECK INPUTS
# =======================
def validate_inputs(input_dict):
    """
    Validates that all inputs are filled and match the expected pattern.
    :param input_dict: Dictionary where keys are labels and values are (input_value, regex_pattern)
    :raises ValueError: If any input is empty or does not match the pattern
    """

    input_errors = []
    for label, (value, pattern) in input_dict.items():
        if not value.strip():  # Check if empty
            input_errors.append(f"{label} are empty!")
        elif not pattern.fullmatch(value):  # Check regex match
            input_errors.append(f"Invalid format for {label}!")
        
    if input_errors:
         raise ValueError("\n".join(input_errors))
    
def validate_programremove(removekey):
    if GlobalHash.showEnrolled(removekey):
        raise PermissionError("There are still Students currently enrolled!\nPlease Edit or Unenroll them First.")   

def validate_collegeremove(removekey):
    if GlobalHash.showConstituents(removekey):
        raise PermissionError("There are still Students currently enrolled!\nPlease Edit or Unenroll them First.")   

# =======================
#      CHECK INPUTS
# =======================



# =======================
#     SHOW FUNCTIONS
# =======================
def show_removeerror_message(error):
    """
    Displays an error message in a pop-up.
    :param error: The error message to display
    """
    messagebox.showerror("Remove Error", str(error))

def show_inputerror_message(error):
    """
    Displays an error message in a pop-up.
    :param error: The error message to display
    """
    messagebox.showerror("Input Error", str(error))

def show_unexpected_error(error):
    """
    Displays an unexpected error message.
    :param error: The unexpected error message
    """
    messagebox.showerror("Unexpected Error", f"An error occurred: {str(error)}")
# =======================
#     SHOW FUNCTIONS
# =======================