import subprocess
import sys
import os
import threading
import time
from pathlib import Path
import socket
from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTimer,
    QUrl,
    Qt,
    QEvent,
)
from PySide6.QtWebEngineWidgets import QWebEngineView


# R server for statistic analysis
class RServer(threading.Thread):
    def __init__(self, language="en", log_file=sys.stdout):
        self.log_file = log_file
        threading.Thread.__init__(self)

        self.host = "localhost"
        self.port = 7776
        self.language = language
        self.p = None

    def run(self):
        app = Path(os.getcwd() + "/shiny/app.R")
        rscript = Path(os.getcwd() + "/R/bin/Rscript")
        envscript = 'set "R_LIBS={}"'.format(Path(os.getcwd() + "/R/library"))
        args = "--language={}".format(self.language)
        cmd = '{} && "{}" "{}" {}'.format(envscript, rscript, app, args)
        print(cmd)
        self.p = subprocess.Popen(cmd, shell=True, stdout=self.log_file, stderr=self.log_file)

        self.stdout, self.stderr = self.p.communicate()
    
    def shutdown(self):
        if self.p:
            print('Shutdown R-Server')
            self.p.terminate()  # 使用terminate更友好
            self.p = None

    def UpdateProjectPath(self, path):
        # Connect to the R server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))

            # Send messages to the server
            message = str(Path(path))
            client_socket.sendall(message.encode())

            # Receive response from the server
            # response = client_socket.recv(1024)
            # print("Received:", response.decode())

            # Close the connection
            client_socket.close()

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
            # self.parent.update()
            return

        # delay 5 sec and try again
        self.timer.start(5000)

    def tryload(self):
        self.load(self.url)
