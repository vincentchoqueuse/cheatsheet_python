import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My first gui")

        figure = Figure(figsize=(6, 4), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, self)
        NavigationToolbar2Tk(figure_canvas, self)

        axes = figure.add_subplot()
        axes.plot([0,1],[0,1])
        axes.set_title('My title')
        axes.set_ylabel('my ylabel')
        axes.set_xlabel('my xlabel')
        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


root = Root()
root.mainloop()