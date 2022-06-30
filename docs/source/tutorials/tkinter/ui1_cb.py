import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My first gui")
        self.geometry("400x300")
        self.label = tk.Label(self, text="Hello World", padx=5, pady=5) 
        self.label.pack()

root = Root()
root.mainloop()