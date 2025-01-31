import tkinter as tk

root = tk.Tk()

root.geometry("780x420")

root.title("MSU-IIT Students")

label = tk.Label(root, text = "Students Repository", font = ('Arial', 20))
label.pack(padx = 20, pady = 6)

textbox = tk.Text(root, height=1, font = ('Arial', 16))
textbox.pack(padx = 10, pady = 10)

button = tk.Button(root, text = "Confirm", font = ('Arial', 16))
button.pack(padx = 10, pady = 10)

root.mainloop()