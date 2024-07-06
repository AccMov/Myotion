import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout


class PlayPlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.lo = QVBoxLayout()
        self.playline = []
        self.setLayout(self.lo)
        self.pen = pg.mkPen(color="#586cdb", width=2)

    def add_line(self, x, y, name):
        plt = pg.plot(x, y, name=name, pen=self.pen, clear=True, autoDownsample=True)
        plt.addLegend()
        self.playline.append(plt.addLine(x=5, pen=pg.mkPen(color="r", width=2)))
        plt.setBackground("#e5ecf6")
        plt.setRange(xRange=[0, len(x)])
        self.lo.addWidget(plt)
        # self.update()

    def update(self, frame):
        for i in range(len(self.playline)):
            self.playline[i].setValue(frame)

    def clear(self):
        for i in reversed(range(self.lo.count())):
            self.lo.itemAt(i).widget().close()
