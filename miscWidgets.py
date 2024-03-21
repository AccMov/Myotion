from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTimer, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QToolBar, QMessageBox, QDialog,
    QWidget, QFileDialog, QTableWidgetItem, QComboBox, QLineEdit, QCompleter,
    QCheckBox, QLabel)

from path import *

class statusLED(QLabel):
    red = None
    green = None

    def __init__(self, w, h, status = False, parent=None):
        super(statusLED, self).__init__(parent)

        if self.red is None:
            self.red = QPixmap(IconPath + '/redcross.png')
        if self.green is None:
            self.green = QPixmap(IconPath + '/greencheckmark.png')

        self.g = self.green.scaled (w, h, Qt.KeepAspectRatio)
        self.r = self.red.scaled (w, h, Qt.KeepAspectRatio)
        self.status = status 
        self.show()

    def set(self, status):
        self.status = status
        self.show()

    def show(self):
        if self.status:
            self.setPixmap(self.g)
        else:
            self.setPixmap(self.r)
