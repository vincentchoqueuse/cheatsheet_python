import tkinter as tk

def submit():
    sum = 0
    for l in range(4):
        num_temp =  entry_list[l].get()
        sum += float(num_temp)
    print(sum)


root = tk.Tk()
root.title("My first gui")
root.geometry("600x200")
label = tk.Label(root, text="List of Numbers", padx=5, pady=5) 
label.pack(fill=tk.BOTH)

entry_list = []
for l in range(4):
    entry_temp = tk.Entry(root)
    entry_temp.insert(-1, '0')
    entry_temp.pack(fill=tk.BOTH)
    entry_list.append(entry_temp)

root.entry_list = entry_list
submit_button = tk.Button(root, text="Compute", command=submit)
submit_button.pack(fill=tk.X)
root.mainloop()