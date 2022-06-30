import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My first calculator")
        self.geometry("300x150")
        num1_label = tk.Label(self, text="Number 1")
        num2_label = tk.Label(self, text="Number 2")
        submit_button = tk.Button(self, text="Compute", command=self.submit)

        self.num1_entry = tk.Entry(self)
        self.num2_entry = tk.Entry(self) 
        
        num1_label.pack(fill=tk.BOTH)
        self.num1_entry.pack(fill=tk.BOTH)
        num2_label.pack(fill=tk.BOTH)
        self.num2_entry.pack(fill=tk.BOTH)
        submit_button.pack(fill=tk.X)

    def submit(self):
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()
        sum = float(num1)+float(num2)
        print(sum)

root = Root()
root.mainloop()

