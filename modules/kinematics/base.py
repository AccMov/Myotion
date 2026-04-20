import time

from PySide6.QtGui import QMouseEvent, QWheelEvent
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import QTimer, Qt

from .input import Input

fps=60

class Base(QOpenGLWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("Base")
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.input = Input()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(int(1000 / fps))
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

    def keyPressEvent(self, event):
        self.input.receiveKeyEvent(event.key(), event.type())

    def keyReleaseEvent(self, event):
        self.input.receiveKeyEvent(event.key(), event.type())

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.input.mousePressEvent(event)
        self.update()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.input.mouseMoveEvent(event)
        self.update()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.input.mouseReleaseEvent(event)

    def wheelEvent(self, event: QWheelEvent) -> None:
        self.input.wheelEvent(event)
