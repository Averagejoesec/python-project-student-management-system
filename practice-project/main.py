from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
        QLineEdit, QPushButton, QComboBox
import sys
from datetime import datetime


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        
        self.output_label = QLabel("")

        combo = QComboBox()
        combo.addItems(['Metric (km)', 'Imperial (miles)'])
        if combo.currentText() == 'Metric (km)':
            calculate_button.clicked.connect(self.calculate_speed_metric)
        if combo.currentText() == 'Imperial (miles)':
            calculate_button.clicked.connect(self.calculate_speed_imperial)

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        grid.addWidget(combo, 0, 3)
        
        self.setLayout(grid)

    def calculate_speed_metric(self):
        time = float(self.time_line_edit.text())
        distance = float(self.distance_line_edit.text())
        speed = distance / time

        self.output_label.setText(f"Average Speed: {speed} km/h")

    def calculate_speed_imperial(self):
        time = float(self.time_line_edit.text())
        distance = float(self.distance_line_edit.text())
        speed = distance / time

        self.output_label.setText(f"Average Speed: {speed} mph")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())