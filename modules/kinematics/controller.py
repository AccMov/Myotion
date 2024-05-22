from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QVBoxLayout

from modules.kinematics.model import Model
from modules.kinematics.playbarwidget import PlayBarWidget
from modules.kinematics.renderwidget import RenderWidget


class Controller:
    """
    controller for kinematics module
    which receive the model and responsible for storing all states of the model
    """

    def __init__(
        self,
        model: Model,
        render: RenderWidget,
        playbar: PlayBarWidget,
        top: QVBoxLayout,
        bottom: QVBoxLayout,
        labeltree,
    ) -> None: 
        self.model = model
        self.frame = 0
        self.render = render
        self.playbar = playbar
        self.top = top
        self.bottom = bottom
        self.labeltree = labeltree

        self.render.setModel(model.kinematic)
        self.render.setController(self)

        self.playbar.setController(self)
        self.playbar.slider.setMaximum(model.kinematic_frames())
        self.playbar.slider.valueChanged.connect(self.slider_valuechange)
        self.playbar.playbutton.clicked.connect(self.on_play_button_clicked)

        self.timer = QTimer()
        self.timer.start(int(1000/self.model.kinematic_frame_rate()))

        self.timer.timeout.connect(self.update)

    def update(self):
        if self.playbar.is_playing():
            self.frame += 1
            if self.frame >= self.model.kinematic_frames():
                self.frame = 0
        self.notify()

    def on_play_button_clicked(self):
        if self.playbar.is_playing():
            self.frame += 1
            if self.frame >= self.model.kinematic_frames():
                self.frame = 0
        self.notify()

    def slider_valuechange(self, value):
        self.render.bodyrender.setFrame(value)
        self.playbar.slider.setValue(value)
        self.frame = value
        self.notify()

    def notify(self):
        self.render.notify(self.frame)
        self.playbar.notify(self.frame)
        # self.top.notify(self.frame)
        # self.bottom.notify(self.frame)
