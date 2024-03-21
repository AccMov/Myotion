from PySide6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout
import pyqtgraph as pg

class EMGWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)     
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSizeConstraint(QGridLayout.SetDefaultConstraint)
        self.plot_graph = pg.PlotWidget(self)
        self.plot_graph.setBackground("w")
        pen = pg.mkPen(color=(255, 0, 0))
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self.plot_graph.plot(time, temperature, pen=pen)
        self.verticalLayout.addWidget(self.plot_graph)
