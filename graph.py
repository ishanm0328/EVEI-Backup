import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

class Graph():
    def __init__(self, data, window):
        self.window = window
        self.data = data

        self.window.attributes('-fullscreen', True)
        self.figure, self.axs = plt.subplots(2,2)
        plt.tight_layout()
        self.stopGraph = False

        buttons = tk.Frame(self.window)
        buttons.pack(side = tk.BOTTOM)
        stopButton = tk.Button(buttons, text="Stop", command = self.stopTheGraph)
        stopButton.grid(row = 0, column = 1)
        killButton = tk.Button(buttons, text="Exit", command = self.window.destroy)
        killButton.grid(row = 0, column = 2)

        self.canvas = FigureCanvasTkAgg(self.figure, master=window)  # A tk.DrawingArea.
        #self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update(self):
        if (not self.stopGraph):
            # Timestamp values for each data point
            # Creates a list like 1,2,3,...N for N data points
            times = np.arange(1, len(self.data) + 1)

            # Get RPM values
            rpms = [ elem['rpm'] for elem in self.data ]
            # Clear RPM Graph
            self.axs[0,0].clear()
            self.axs[0,0].set_title("RPM")
            self.axs[0,0].set_xlabel("Time")
            # Plot data. [-10:] gets the last 10 data points.
            self.axs[0,0].plot(times[-10:], rpms[-10:])    

            # Get Gyro values
            gyro_x = [ elem['gyro_x'] for elem in self.data ]
            gyro_y = [ elem['gyro_y'] for elem in self.data ]
            gyro_z = [ elem['gyro_z'] for elem in self.data ]
            self.axs[0,1].clear()
            self.axs[0,1].set_title("G-Forces")
            self.axs[0,1].set_xlabel("Time")
            self.axs[0,1].plot(times[-10:], gyro_x[-10:])
            self.axs[0,1].plot(times[-10:], gyro_y[-10:])    
            self.axs[0,1].plot(times[-10:], gyro_z[-10:])
        
            # Get Throttle values
            throttle = [ elem['analog_a'] for elem in self.data ]
            self.axs[1,0].clear()
            self.axs[1,0].set_title("Throttle")
            self.axs[1,0].set_xlabel("Time")
            self.axs[1,0].plot(times[-10:], throttle[-10:])
        
            # Get Steering values
            steering = [ elem['analog_b'] for elem in self.data ]
            self.axs[1,1].clear()
            self.axs[1,1].set_title("Steering")
            self.axs[1,1].set_xlabel("Time")
            self.axs[1,1].plot(times[-10:], steering[-10:])
        
            self.canvas.draw()
    
    def stopTheGraph(self):
        self.stopGraph = not self.stopGraph
