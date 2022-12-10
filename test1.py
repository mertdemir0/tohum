import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# create the figure and the line chart
figure = plt.Figure(figsize=(5, 4), dpi=100)
line_chart = figure.add_subplot(111)
line_chart.plot(x, y)

# create the tkinter GUI
window = tk.Tk()
window.title("Line Chart")

# add a text entry widget for manually entering data
entry_x = tk.Entry(window)
entry_y = tk.Entry(window)
label_x = tk.Label(window, text="x:")
label_y = tk.Label(window, text="y:")
label_x.pack()
entry_x.pack()
label_y.pack()
entry_y.pack()

# add a button for adding the data to the line chart
def add_data():
    x_value = int(entry_x.get())
    y_value = int(entry_y.get())
    x.append(x_value)
    y.append(y_value)
    line_chart.plot(x, y)
    canvas.draw()
button = tk.Button(window, text="Add Data", command=add_data)
button.pack()

# add the line chart to the GUI
canvas = FigureCanvasTkAgg(figure, window)
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# show the GUI
window.mainloop()
