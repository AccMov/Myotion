import time
from PySide6.QtGui import QMouseEvent
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import QTimer

from modules.kinematics.input import Input
from PySide6.QtCore import Qt


class Base(QOpenGLWidget):
    def __init__(self,parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("Base")
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.input=Input()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.fps = 60
        self.timer.start(int(1000 / self.fps))
        self.time = 0

    def initializeGL(self) -> None:
        self.lastTime = time.time()

    def paintGL(self) -> None:
        self.deltaTime = time.time() - self.lastTime
        self.time += self.deltaTime
        self.lastTime = time.time()
        # print("FPS: ", 1 / self.deltaTime)
        self.input.update()

    def update(self):
        super().update()
        # self.hide()
        # self.show()
    
    def keyPressEvent(self, event):
        self.input.receiveKeyEvent(event.key(), event.type())
        self.update()

    def keyReleaseEvent(self, event):
        self.input.receiveKeyEvent(event.key(), event.type())
        self.update() 
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.input.mosePressEvent(event)
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        return super().mouseMoveEvent(event)