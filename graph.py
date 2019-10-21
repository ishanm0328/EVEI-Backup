from pandas import DataFrame
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [3, 5, 1, 7, 4]
}

dataFrame = DataFrame(data, columns=list(data.keys()))
#dataFrame[list(data.keys())].groupby('X').sum()

root = tk.Tk()

figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, root)
chart_type.get_tk_widget().pack()
dataFrame.plot(kind='line', legend=True, ax=ax)
ax.set_title('The Title of your chart')

root.mainloop()
