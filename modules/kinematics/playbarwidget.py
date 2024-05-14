from enum import Enum

from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QSlider, QPushButton, QStyle, QWidget, QHBoxLayout
from PySide6.QtCore import Qt, QTimer


class State(Enum):
    STOP = 0
    PLAY = 1
    PAUSE = 2


class SliderWidget(QSlider):
    def __init__(self, parent=None, model=None):
        super().__init__(Qt.Orientation.Horizontal, parent)
        self.setRange(0, 1000)
        self.setValue(0)
        self.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.setTickInterval(10)
        self.setSingleStep(1)

        self.valueChanged.connect(self.on_slider_value_changed)

    def on_slider_value_changed(self, value):
        print(f"Slider value changed to {value}")

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

    def set_value(self, value):
        self.setValue(value)

    def get_value(self):
        return self.value()


class PlayBarWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initui(parent)

    def initui(self, parent=None):
        self.slider = SliderWidget(parent)
        self.playbutton = QPushButton("Play", parent)
        self.State = State.STOP
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
        if self.State == State.STOP or self.State == State.PAUSE:
            self.State = State.PLAY
            self.playbutton.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
            )
        elif self.State == State.PLAY:
            self.State = State.PAUSE
            self.playbutton.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
            )
