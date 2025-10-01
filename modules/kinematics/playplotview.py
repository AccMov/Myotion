import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout


class PlayPlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.lo = QVBoxLayout()
        self.playline = []
        self.setLayout(self.lo)
        self.pen = pg.mkPen(color="#586cdb", width=2)

    def add_line(self, x, y, name, type="emg", rate=1):
        plt = pg.plot(x, y, name=name, pen=self.pen, clear=True, autoDownsample=True)
        self.playline.append({ 'line': plt.addLine(x=5, pen=pg.mkPen(color="r", width=2)), 'rate': rate })
        plt.setBackground("#e5ecf6")
        plt.setRange(xRange=[0, max(x)])
        self.lo.addWidget(plt)
        
        # self.update()

    def update(self, frame):
        for line in self.playline:
            line['line'].setValue(frame / line['rate'])

    def clear(self):
        for i in reversed(range(self.lo.count())):
            self.lo.itemAt(i).widget().close()
            self.playline.remove(self.playline[i])
