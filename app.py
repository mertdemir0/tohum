import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button

class LineGraphGenerator:
    def __init__(self):
        # Create main window
        self.root = Tk()
        self.root.title("Line Graph Generator")

        # Create widgets
        self.x_label = Label(self.root, text="Enter x-values:")
        self.x_entry = Entry(self.root)
        self.y_label = Label(self.root, text="Enter y-values:")
        self.y_entry = Entry(self.root)
        self.generate_button = Button(self.root, text="Generate", command=self.generate_graph)

        # Add widgets to window
        self.x_label.pack()
        self.x_entry.pack()
        self.y_label.pack()
        self.y_entry.pack()
        self.generate_button.pack()

        # Start the main event loop
        self.root.mainloop()

    def generate_graph(self):
        # Get input values
        x_values = [int(x) for x in self.x_entry.get().split(",")]
        y_values = [int(y) for y in self.y_entry.get().split(",")]

        # Generate line graph
        plt.plot(x_values, y_values)
        plt.show()

# Create instance of LineGraphGenerator class and start the program
LineGraphGenerator()
