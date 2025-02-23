from tkinter import messagebox
import re

NormalEntry = re.compile(r"^[A-Z][a-z]+(?:\s[A-Z][a-z]+)*$")
IDEntry = re.compile(r"^\d{4}-\d{4}$")
EmailEntry = re.compile(r"^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}$")
CodeEntry = re.compile(r"^[A-Za-z]{3,6}$")
YearEntry = re.compile(r"^[1-5](st|nd|rd|th) (Year|Year and Above)$")

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
