import matplotlib.pyplot as plt
import sqlite3
from tkinter import Tk, Label, Entry, Button, filedialog

class LineGraphGenerator:
    def __init__(self):
        # Connect to the database
        self.conn = sqlite3.connect("line_graphs.db")

        # Create main window
        self.root = Tk()
        self.root.title("Line Graph Generator")

        # Create widgets
        self.chart_name_label = Label(self.root, text="Enter chart name:")
        self.chart_name_entry = Entry(self.root)
        self.teacher_name_label = Label(self.root, text="Enter teacher name:")
        self.teacher_name_entry = Entry(self.root)
        self.student_name_label = Label(self.root, text="Enter student name:")
        self.student_name_entry = Entry(self.root)
        self.x_label = Label(self.root, text="Enter x-values:")
        self.x_entry = Entry(self.root)
        self.y_label = Label(self.root, text="Enter y-values:")
        self.y_entry = Entry(self.root)
        self.edit_button = Button(self.root, text="Edit", command=self.edit_graph)
        self.png_button = Button(self.root, text="Export as PNG", command=self.export_png)
        self.jpeg_button = Button(self.root, text="Export as JPEG", command=self.export_jpeg)

        # Add widgets to window
        self.chart_name_label.pack()
        self.chart_name_entry.pack()
        self.teacher_name_label.pack()
        self.teacher_name_entry.pack()
        self.student_name_label.pack()
        self.student_name_entry.pack()
        self.x_label.pack()
        self.x_entry.pack()
        self.y_label.pack()
        self.y_entry.pack()
        self.edit_button.pack()
        self.png_button.pack()
        self.jpeg_button.pack()

        # Start the main event loop
        self.root.mainloop()

    def edit_graph(self):
        # Get input values
        x_values = [int(x) for x in self.x_entry.get().split(",")]
        y_values = [int(y) for x in self.y_entry.get().split(",")]

        # Generate line graph
        plt.plot(x_values, y_values)
        plt.show()

    def export_png(self):
        # Get input values
        x_values = [int(x) for x in self.x_entry.get().split(",")]
        y_values = [int(y) for x in self.y_entry.get().split(",")]

        # Generate line graph
        plt.plot(x_values, y_values
