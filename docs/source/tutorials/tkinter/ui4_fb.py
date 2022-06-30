import tkinter as tk

def submit():
    val1 = num1_entry.get()
    val2 = num2_entry.get()
    sum = float(val1)+float(val2)
    print(sum)


root = tk.Tk()
root.title("My first calculator")
root.geometry("300x150")
num1_label = tk.Label(root, text="Number 1")
num1_entry = tk.Entry(root)
num2_label = tk.Label(root, text="Number 2")
num2_entry = tk.Entry(root) 
submit_button = tk.Button(root, text="Compute", command=submit)

num1_label.pack(fill=tk.BOTH)
num1_entry.pack(fill=tk.BOTH)
num2_label.pack(fill=tk.BOTH)
num2_entry.pack(fill=tk.BOTH)
submit_button.pack(fill=tk.X)

root.mainloop()
