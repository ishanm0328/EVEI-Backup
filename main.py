import config
from serial_handler import SerialHandler
from window import Window
from graph import Graph
import tkinter as tk

# TODO: setup root with toolbars/buttons

# TODO: setup window with graphs

config = config.get_config
data = []
serial = SerialHandler(data, config)
window = Window() # Tk window object
graph = Graph(data, window)

while True:
    serial.update()
    window.update_idletasks()
    window.update()
    #graph.update()

# TODO: register exit handler
save_config(config)
# TODO: save
