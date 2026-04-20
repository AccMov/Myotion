import subprocess
import sys
import threading
import time
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

class Server(threading.Thread):
    def __init__(self):
        self.stdout = None
        self.stderr = None
        threading.Thread.__init__(self)

    def run(self):
        print("launching R server...")
        p = subprocess.Popen("Rscript app.R".split(),
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        self.stdout, self.stderr = p.communicate()
        print(self.stdout)
        print(self.stderr)

class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        #QMainWindow.__init__(self)

        # we create an instance of QWebEngineView and set the html code
        webwidget = QWebEngineView()
        url = QUrl("http://127.0.0.1:7775")
        webwidget.load(url)

        # set the QWebEngineView instance as main widget
        self.setCentralWidget(webwidget)

# run plot as html
#fig.show()
server = Server()
server.start()
print("Sleep 10 secs") 
time.sleep(10)

print("launching GUI") 
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
server.join()
