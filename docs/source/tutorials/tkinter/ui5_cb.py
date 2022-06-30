import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My first gui")
        self.geometry("600x200")
        label = tk.Label(self, text="List of Numbers", padx=5, pady=5) 
        label.pack(fill=tk.BOTH)

        entry_list = []
        for l in range(4):
            entry_temp = tk.Entry(self)
            entry_temp.insert(-1, '0')
            entry_temp.pack(fill=tk.BOTH)
            entry_list.append(entry_temp)
        
        self.entry_list = entry_list
        submit_button = tk.Button(self, text="Compute", command=self.submit)
        submit_button.pack(fill=tk.X)

    def submit(self):
        sum = 0
        for l in range(4):
            num_temp =  self.entry_list[l].get()
            sum += float(num_temp)
        print(sum)


root = Root()
root.mainloop()