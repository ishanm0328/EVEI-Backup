import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

class Graph():
    def __init__(self, data, window):
        self.window = window
        self.data = data
        # TODO: separate graph & dataset names
        # Graph names should be: RPM, G-Forces, Throttle, Steering
        self.graphNames = [["RPM","G-Forces"],["Throttle","Steering"]]
        self.dataNames =  [["rpm","gyro_x"],["analog_a","analog_b"]]

        self.figure, self.axs = plt.subplots(2,2)
        self.setGraphNames(self.axs, self.graphNames)
        plt.tight_layout()

        self.canvas = FigureCanvasTkAgg(self.figure, master=window)  # A tk.DrawingArea.
        #self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update(self):
        # Loop through all of our plots
        for i in range(len(self.dataNames)):
            for k in range(len(self.dataNames[0])):
                yar = []
                # If we have <= 10 data points, plot them all
                if(len(self.data) <= 10):
                    xar = np.arange(1,len(self.data)+1)
                    for j in range(len(self.data)):
                        yar.append(self.data[j][self.dataNames[i][k]])
                # Otherwise, plot just the most recent 10
                else:
                    xar = np.arange(len(self.data)-10,len(self.data))
                    for j in range(-10,0):
                        yar.append(self.data[j][self.dataNames[i][k]])
                # Clear graph and plot data again
                self.axs[i,k].clear()
                self.setGraphNames(self.axs,self.graphNames)
                self.axs[i,k].plot(xar,yar)
        self.canvas.draw()

    def setGraphNames(wut,axs,graphNames):
        for i in range(len(graphNames)):
            for k in range(len(graphNames[0])):
                axs[i,k].set_title(graphNames[i][k])
                axs[i,k].set_ylabel(graphNames[i][k])
                axs[i,k].set_xlabel("Time")
