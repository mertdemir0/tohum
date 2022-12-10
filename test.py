import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd

# Sample time-series data
data = {
    "date": ["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04", "2022-01-05"],
    "value": [1, 4, 9, 16, 25]
}

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)

# Set the 'date' column as the index of the DataFrame
df.set_index("date", inplace=True)

class LineChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the matplotlib figure and axes
        fig, ax = plt.subplots()

        # Create the line chart
        ax.plot(df.index, df["value"])

        # Set the x-axis label
        ax.set_xlabel("Date")

        # Create a FigureCanvas object, which can be added to a GUI
        self.canvas = FigureCanvas(fig)

        # Create labels and input fields for entering dates and values
        date_label = QLabel("Enter date:")
        self.date_input = QLineEdit()
        value_label = QLabel("Enter value:")
        self.value_input = QLineEdit()

        # Create a button for adding the date and value to the chart
        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_to_chart)

        # Create a vertical layout to add the figure and other widgets
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(value_label)
        layout.addWidget(self.value_input)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def add_to_chart(self):
        # Get the date and value from the input fields
        date = self.date_input.text()
        value = self.value_input.text()

        # Add the date and value to the DataFrame
        df.loc[date] = value

        # Update the line chart
        ax = self.canvas.figure.axes[0]
        ax.clear()
        ax.plot(df.index, df["value"])

        # Redraw the figure
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chart = LineChartWidget()
    chart.show()
    
