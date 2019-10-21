import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

class Graph():
    def __init__(self, window, data):
        self.window = window
        self.data = data

        self.figure = Figure(figsize=(5,4), dpi=100)
        t = np.arange(0, 3, .01)
        self.figure.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        self.canvas = FigureCanvasTkAgg(self.figure, master=window)  # A tk.DrawingArea.
        #self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update():
        pass
