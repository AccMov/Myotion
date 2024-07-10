import subprocess
import sys
import os
import threading
import time
from pathlib import Path
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTimer, QUrl, Qt, QEvent)
from PySide6.QtWebEngineWidgets import QWebEngineView

# R server for statistic analysis
class RServer(threading.Thread):
    def __init__(self):
        self.stdout = None
        self.stderr = None
        threading.Thread.__init__(self)

    def run(self):
        print("launching R server...")
        app = Path(os.getcwd() + '/shiny/app.R')
        rscript = Path(os.getcwd() + '/R/bin/Rscript')
        envscript = 'set "R_LIBS={}"'.format(Path(os.getcwd() + '/R/library'))
        cmd = '{} && "{}" "{}"'.format(envscript, rscript, app)
        print(cmd)
        p = subprocess.Popen(cmd,
                             shell=True,
                             stdout=sys.stdout,
                             stderr=sys.stderr)

        self.stdout, self.stderr = p.communicate()

class RServerBrowser(QWebEngineView):
    def __init__(self, parent=None):
        super(RServerBrowser, self).__init__(parent)

        self.url = QUrl("http://127.0.0.1:7775")
        self.parent = parent

        self.connected = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.tryload)

        self.loadFinished.connect(self.loadFinishedCB)
        self.tryload()
        

    def loadFinishedCB(self, ok):
        if ok:
            self.connected = True
            self.timer.stop()
            #self.parent.update()
            return
        
        print("html loaded failed, retry in 5 secs")
        # delay 5 sec and try again
        self.timer.start(5000)

    def tryload(self):
        self.load(self.url)

