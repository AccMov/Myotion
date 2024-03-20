import plotly
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.graph_objects import Figure, Scatter
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
from PySide6.QtWebEngineWidgets import QWebEngineView
import pandas as pd
import pyMotion as pm
from pyMotion import logger

# Plot timerSeriesTable using plotly
class QPlotView(QWebEngineView):
    def __init__(self, parent=None):
        super(QPlotView, self).__init__(parent)

        self.parent = parent
        self.fig = None

    # bar, plot by timeSeriesTable
    def bar(self, tst, x='', y='', title='', color=''):
        df = tst.toPandasFrame()
        self.fig = px.bar(df,
                     x = x,
                     y = y,
                     barmode="relative",
                     title = title,
                     markers = True)
        
    # line, plot by timeSeriesTable
    def line(self, tst, channel, title='', color=[]):
        chans = []
        if type(channel) is not list:
            chans = [channel]

        for c in chans:    
            if not tst.hasChannel(c):
                logger.error("channel {} not exist".format(c))
                return -1
        
        df = tst.toPandasFrame()
        df['t'] = tst.getLinspace()
        self.fig = px.line(df,
                     x = 't',
                     y = chans,
                     title = title,
                     markers = False)
        return 0
    
    # line, plot by list
    def line(self, x_, y_, channel, title='', color=[]):
        chans = []
        data = []
        if type(channel) is not list:
            chans = [channel]
        else:
            chans = channel
        if len(y_) == 0:
            logger.error('data y is empty')
            return -1
        if type(y_[0]) is list:
            n = len(y_[0])
            m = len(y_)
            data = y_
        else:
            n = len(y_)
            m = 1
            data = [ y_ ]
        if n != len(x_):
            logger.error('x and y need to have same dimension')
            return -1
        if m != len(chans):
            logger.error('row of data and channel labels should have same dimension')
            return -1
        table = {}
        for i in range(0, m):
            table[chans[i]] = data[i]
        df = pd.DataFrame(table)
        df['t'] = x_
        self.fig = px.line(df,
                     x = 't',
                     y = chans,
                     title = title,
                     markers = False)
        return 0

    # display on webEngine
    def show(self):
        html = '<html><body>'
        html += plotly.offline.plot(self.fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        self.setHtml(html)
        self.update()

# QPlotViews with subplot which shared x_axis
class QPlotViews(QWebEngineView):
    def __init__(self, rows, cols, parent=None):
        super(QPlotView, self).__init__(parent)

        self.parent = parent
        self.fig = None
