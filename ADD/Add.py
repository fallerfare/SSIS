import tkinter as ttk
from ADD import SignUp, CreateCollg, CreateProg

class Add:
    def __init__(self, root, text):
        self.root = root

        match(text):
            
            case("ID"):
                command = SignUp.SignUpWindow
                buttext = "Enroll New"

            case("Program Code"):
                command = CreateProg.CreateProgWindow
                buttext = "Add Program"

            case("College Code"):
                command = CreateCollg.CreateCollgWindow
                buttext = "Add College"

            case(""):
                buttext = "What, no button???"
        
        Button = ttk.Button(root, text = buttext, command = command) 
        Button.pack(padx=20, )