import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("fourier synth")
        self.geometry("600x400")
        frame1 = tk.Frame(self, width=200, height=400)
        frame1.pack(side="left", expand=1, anchor="c")
        label = tk.Label(frame1, text="an", padx=5) 
        label.pack(fill=tk.BOTH)
        entry_list = []
        for l in range(8):
            entry_temp = tk.Entry(frame1)
            entry_temp.insert(-1, '0')
            entry_temp.pack(fill=tk.BOTH)
            entry_list.append(entry_temp)

        self.entry_list = entry_list
        self.submit_button = tk.Button(frame1, text="Compute")
        self.submit_button.pack(fill=tk.X)

        frame2 = tk.Frame(self, width=400, height=400)
        frame2.pack(side="left", expand=1, anchor="c")
        figure = Figure(figsize=(6, 4), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, frame2)
        NavigationToolbar2Tk(figure_canvas, frame2)

        axes = figure.add_subplot()
        axes.plot([0,1],[0,1])
        axes.set_title('My title')
        axes.set_ylabel('my ylabel')
        axes.set_xlabel('my xlabel')
        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        

if __name__ == "__main__":
    root = Root()
    root.mainloop()