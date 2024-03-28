import sys
sys.path.insert(0, '../')

import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure, Scatter
import plotly
import numpy as np
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QToolBar,
    QWidget)
from PySide6.QtWebEngineWidgets import QWebEngineView
from modules import *
from qplotview import *


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        
        self.main = QWidget()
        self.stackedWidget = QStackedWidget(self.main)

        self.plot_widget = QPlotView()

        a = c3dFile('D:/Myotion/pyMotion/tests/Sample_data/Sample_data/c3d_emg/ERRPT.c3d')
        b = a.analog.convertToTST()
        channel = 'Fx1'
        self.plot_widget.line(b, channel)
        self.plot_widget.show()

        self.stackedWidget.addWidget(self.plot_widget)

        self.blank = QWidget()
        self.stackedWidget.addWidget(self.blank)

        self.stackedWidget.setCurrentWidget(self.plot_widget)
        self.setCentralWidget(self.main)

# run plot as html
#fig.show()
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
