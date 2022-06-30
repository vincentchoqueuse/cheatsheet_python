import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


root = tk.Tk()
root.title("My first gui")
figure = Figure(figsize=(6, 4), dpi=100)
figure_canvas = FigureCanvasTkAgg(figure, root)
NavigationToolbar2Tk(figure_canvas, root)

axes = figure.add_subplot()
axes.plot([0,1],[0,1])
axes.set_title('My title')
axes.set_ylabel('my ylabel')
axes.set_xlabel('my xlabel')
figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()