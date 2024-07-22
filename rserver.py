import subprocess
import sys
import os
import threading
import time
from pathlib import Path
import socket
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
    
    def UpdateProjectPath(self, path):
        host = 'localhost'
        port = 7776

        # Connect to the R server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print("Connected to the server.")

            # Send messages to the server
            message = str(Path(path))
            client_socket.sendall(message.encode())
            print("Sent:", message)

            # Receive response from the server
            #response = client_socket.recv(1024)
            #print("Received:", response.decode())

            # Close the connection
            print("Closing connection.")
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
            #self.parent.update()
            return
        
        print("html loaded failed, retry in 5 secs")
        # delay 5 sec and try again
        self.timer.start(5000)

    def tryload(self):
        self.load(self.url)
