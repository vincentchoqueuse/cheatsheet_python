import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My first gui")
        self.geometry("600x400")
        leftFrame = tk.Frame(self, width=200, height=400)
        leftFrame.pack(side="left", expand=1, anchor="c")
        label1 = tk.Label(leftFrame, text="Hello Frame1", padx=5, pady=5) 
        label1.pack()
        rightFrame = tk.Frame(self, width=400, height=400)
        rightFrame.pack(side="right", expand=1, anchor="c")
        label2 = tk.Label(rightFrame, text="Hello Frame2", padx=5, pady=5) 
        label2.pack()

root = Root()
root.mainloop()