import tkinter as tk
from tkinter import filedialog

class Window(tk.Tk):
    def __init__(self, config, *args, **kwargs):
        self.config = config
        super(Window, self).__init__(*args, **kwargs)

    def prompt_serial(self):
        if platform == "linux" or platform == "linux2":    
            filetypes = [('serial ports', 'ttyS*'), ('usb serial', 'ttyUSB*')]
            port = filedialog.askopenfilename(parent=self, initialdir='/dev',
                                       title='Select Serial Port',
                                       filetypes=filetypes)
            self.config['serial']['port'] = port
        elif platform == "win32":
            pattern = re.compile(r'COM\d')
        
            query = "SELECT * FROM Win32_PnPEntity WHERE Name LIKE '%(COM%)'"
            coms  = wmi.WMI().query(query)
        
            name = []
            for com in coms:
                name.append(re.search(pattern, com.Name, flags = 0).group())
                print(name)
