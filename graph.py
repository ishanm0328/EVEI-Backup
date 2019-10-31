import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

class Graph():
    def __init__(self, window, data):
        self.window = window
        self.data = data
        self.graphNames = [["RPM","Energy"],["Acceleration","Position"]]

        self.figure, self.axs = plt.subplots(2,2)
        self.setGraphNames(self.axs, self.graphNames)

        self.canvas = FigureCanvasTkAgg(self.figure, master=window)  # A tk.DrawingArea.
        #self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update():
        for i in range(len(graphNames)):
            for k in range(len(graphNames[0])):
                yar = []
                if(len(data) <= 10):
                    xar = np.arange(1,11)
                    for j in range(10):
                        yar.append(data[j][graphNames[i][k]])
                else:
                    xar = np.arange(len(data)-10,len(data)+1)
                    for j in range(-10,0):
                        yar.append(data[j][graphNames[i][k]])
                axs[i,k].clear()
                setGraphNames(axs,graphNames)
                axs[i,k].plot(xar,yar)
        self.canvas.draw()

    def setGraphNames(wut,axs,graphNames):
        print(wut)
        print(axs)
        print(graphNames)
        for i in range(len(graphNames)):
            for k in range(len(graphNames[0])):
                axs[i,k].set_title(graphNames[i][k])
                axs[i,k].set_ylabel(graphNames[i][k])
                axs[i,k].set_xlabel("Time")
