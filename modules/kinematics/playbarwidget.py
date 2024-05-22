from enum import Enum

from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QSlider, QPushButton, QStyle, QWidget, QHBoxLayout
from PySide6.QtCore import Qt, QTimer


class State(Enum):
    STOP = 0
    PLAY = 1
    PAUSE = 2


class SliderWidget(QSlider):
    def __init__(self, parent=None):
        super().__init__(Qt.Orientation.Horizontal, parent)
        self.setMinimum(0)
        self.setValue(0)
        self.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.setTickInterval(10)
        self.setSingleStep(1)
        self.setPalette

    def mousePressEvent(self, event):
        self.setValue(
            self.minimum()
            + (self.maximum() - self.minimum()) * event.x() / self.width()
        )

    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        # if mouse is pressed and moving change value of slider
        if ev.buttons() == Qt.LeftButton:
            self.setValue(
                self.minimum()
                + (self.maximum() - self.minimum()) * ev.x() / self.width()
            )

    def get_value(self):
        return self.value()
    
    def setController(self,controller):
        self.valueChanged.connect(controller.slider_valuechange)

class PlayBarWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initui(parent)

    def initui(self, parent=None):
        self.slider = SliderWidget(parent)
        self.playbutton = QPushButton("Play", parent)
        self.playbutton.clicked.connect(self.on_play_button_clicked)
        self.state = State.STOP
        self.playbutton.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        )
        self.playbutton.setCheckable(True)
        self.playbutton.setStyleSheet("QPushButton:hover {background-color: #5e5959;}")

        hboxlayout = QHBoxLayout()
        hboxlayout.setContentsMargins(0, 0, 0, 0)
        hboxlayout.addWidget(self.playbutton)
        hboxlayout.addWidget(self.slider)

        self.setLayout(hboxlayout)

    def on_play_button_clicked(self):
        if self.state == State.STOP or self.state == State.PAUSE:
            self.state = State.PLAY
            self.playbutton.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
            )
            self.playbutton.setText("Pause")
        elif self.state == State.PLAY:
            self.state = State.PAUSE
            self.playbutton.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
            )
            self.playbutton.setText("Play")

    def is_playing(self):
        return self.state == State.PLAY

    def notify(self, frame):
        self.slider.setValue(frame)

    def setController(self, controller):
        self.slider.setController(controller)
        # self.playbutton.clicked.connect(controller.on_play_button_clicked)
