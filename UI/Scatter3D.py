from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        super().__init__(self.fig)
        self.setParent(parent)

    def plot(self, data, box_size):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111, projection='3d')
        x, y, z, values = tuple(list(i) for i in zip(*data))
        
        scatter = self.ax.scatter(x, y, z, c=values, cmap='coolwarm', s=25)
        self.ax.set_xlabel('X axis (cm)')
        self.ax.set_ylabel('Y axis (cm)')
        self.ax.set_zlabel('Z axis (cm)')

        # Draw the bounding box
        MIN_X = 0
        MIN_Y = 0
        MIN_Z = 0
        MAX_X, MAX_Y, MAX_Z = box_size

        corners = [
            (MIN_X, MIN_Y, MIN_Z), (MIN_X, MIN_Y, MAX_Z),
            (MIN_X, MAX_Y, MIN_Z), (MIN_X, MAX_Y, MAX_Z),
            (MAX_X, MIN_Y, MIN_Z), (MAX_X, MIN_Y, MAX_Z),
            (MAX_X, MAX_Y, MIN_Z), (MAX_X, MAX_Y, MAX_Z)
        ]
        
        edges = [
            (0, 1), (0, 2), (0, 4),
            (1, 3), (1, 5),
            (2, 3), (2, 6),
            (3, 7),
            (4, 5), (4, 6),
            (5, 7),
            (6, 7)
        ]

        for edge in edges:
            point1, point2 = corners[edge[0]], corners[edge[1]]
            self.ax.plot([point1[0], point2[0]], [point1[1], point2[1]], [point1[2], point2[2]], color='black')

        # Add color bar
        cbar = self.fig.colorbar(scatter, ax=self.ax, shrink=0.25, aspect=5)
        cbar.set_label('Value')

        self.draw()

class ScatterGraph(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.canvas = MatplotlibCanvas()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
    
    def plot(self, data, box):
        self.canvas.plot(data, box)