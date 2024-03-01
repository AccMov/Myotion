import plotly
import plotly.express as px
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
        if not tst.hasChannel(channel):
            logger.error("channel not exist")
            return -1
        df = tst.toPandasFrame()
        x = tst.getLinspace()
        self.fig = px.line(df,
                     x,
                     y = channel,
                     title = title,
                     markers = True)
        return 0

    # display on webEngine
    def show(self):
        html = '<html><body>'
        html += plotly.offline.plot(self.fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></ html>'

        self.setHtml(html)
        self.update()

