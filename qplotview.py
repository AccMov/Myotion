import plotly
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.graph_objects import Figure, Scatter, FigureWidget
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QByteArray, QBuffer, QIODevice,
    QSize, QTime, QUrl, Qt)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import (QWebEngineUrlScheme, 
                                     QWebEngineUrlSchemeHandler, QWebEngineUrlRequestJob,
                                     QWebEngineProfile, QWebEnginePage)
import pandas as pd
#from modules.pyMotion import logger as logger

# set max points
PLOTY_MAX_POINTS = -1
# url scheme name
URL_SCHEME = 'local'
# axis label
X_LABEL = 'Time(s)'
Y_LABEL = 'Magnitude'

# html load handler with custom scheme
class UrlSchemeHandler(QWebEngineUrlSchemeHandler):
    def __init__(self, parent):
        super(UrlSchemeHandler, self).__init__(parent)
        self.data = None

    def setHtml(self, data):
        self.data = str(data).encode()

    def requestStarted(self, job):
        mime = QByteArray(b'text/html')
        buffer = QBuffer(job)
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        buffer.write(self.data)
        job.reply(mime, buffer)

# Plot timerSeriesTable using plotly
class QPlotView(QWebEngineView):
    def __init__(self, parent=None):
        super(QPlotView, self).__init__(parent)
        self.parent = parent
        self.fig = None

        # create new profile
        self.profile = QWebEngineProfile(parent)

        # install handler
        self.schemeHandler = UrlSchemeHandler(self)
        self.schemeHandler.setHtml('<html><body></body></html>')
        self.profile.installUrlSchemeHandler(
            bytes(URL_SCHEME, 'ascii'), self.schemeHandler)

        # create new page
        self.page = QWebEnginePage(self.profile, parent)
        self.setPage(self.page)

        # set URL
        self.url = QUrl('any_url_works_to_trigger_handler')
        self.url.setScheme(URL_SCHEME)
        self.setUrl(self.url)

    # style setting
    def update_layout(self):
        # set label to be on the bottom of the fig
        self.fig.update_layout(legend=dict(yanchor='bottom', xanchor='center', y=-0.5, x=0.5, orientation='h'))
        self.fig.update_layout(yaxis_title=Y_LABEL)

    # bar, plot by timeSeriesTable
    def bar(self, tst, channel, title='', color=''):
        chans = []
        if type(channel) is not list:
            chans = [channel]

        for c in chans:    
            if not tst.hasChannel(c):
                logger.error("channel {} not exist".format(c))
                return -1
            
        df = tst.toPandasFrame()
        df[X_LABEL] = tst.getLinspace()
        df = df[:PLOTY_MAX_POINTS]
        self.fig = px.bar(df,
                     x = X_LABEL,
                     y = chans,
                     barmode="relative",
                     title = title,
                     markers = True)
        
    # bar, plot by list
    def bar(self, x_, y_, channel, title='', color=[]):
        chans = []
        data = []
        # type and sanity check
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
        df[X_LABEL] = x_
        df = df[:PLOTY_MAX_POINTS]
        self.fig = px.bar(df,
                     x = X_LABEL,
                     y = chans,
                     title = title,
                     barmode="relative")
        self.update_layout()
        return 0
        
        
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
        df[X_LABEL] = tst.getLinspace()
        df = df[:PLOTY_MAX_POINTS]
        self.fig = px.line(df,
                     x = X_LABEL,
                     y = chans,
                     title = title,
                     markers = False,
                     ender_mode='webgl')
        self.update_layout()
        return 0
    
    # line, plot by list
    def line(self, x_, y_, channel, title='', color=[]):
        chans = []
        data = []
        # type and sanity check
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
        df[X_LABEL] = x_
        df = df[:PLOTY_MAX_POINTS]
        self.fig = px.line(df,
                     x = X_LABEL,
                     y = chans,
                     title = title,
                     markers = False,
                     render_mode='webgl')
        self.update_layout()
        return 0

    # display on webEngine
    def show(self):
        html = plotly.io.to_html(self.fig, include_plotlyjs=True)
        self.schemeHandler.setHtml(html)

        self.setUrl(self.url)
        self.update()
    
    def hide(self):
        html = '<html><body></body></html>'
        self.setHtml(html)
        self.update()

# QPlotViews with subplot which shared x_axis
class QPlotViews(QWebEngineView):
    def __init__(self, rows, cols, parent=None):
        super(QPlotView, self).__init__(parent)

        self.parent = parent
        self.fig = None
