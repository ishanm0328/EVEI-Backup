import tkinter as tk
from tkinter import filedialog

class Window(tk.Tk):
    def __init__(self, config, *args, **kwargs):
        self.config = config
        super(Window, self).__init__(*args, **kwargs)

    def prompt_serial(self):
        filetypes = [('serial ports', 'ttyS*'), ('usb serial', 'ttyUSB*')]
        port = filedialog.askopenfilename(parent=self, initialdir='/dev',
                                   title='Select Serial Port',
                                   filetypes=filetypes)
        self.config['serial']['port'] = port
