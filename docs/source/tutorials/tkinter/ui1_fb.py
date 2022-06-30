import tkinter as tk

root = tk.Tk()
root.title("My first gui")
root.geometry("400x300")
label = tk.Label(root, text="Hello World", padx=5, pady=5) 
label.pack()
root.mainloop()