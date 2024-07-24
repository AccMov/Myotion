from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QVBoxLayout
import numpy as np

from modules.kinematics.model import Model
from modules.kinematics.playbarwidget import PlayBarWidget
from modules.kinematics.playplotview import PlayPlotWidget
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
        top: PlayPlotWidget,
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
        self.playbar.slider.setRange(0,model.kinematic_frames())
        self.playbar.slider.valueChanged.connect(self.slider_valuechange)
        self.playbar.playbutton.clicked.connect(self.on_play_button_clicked)
        self.playbar.prevFrameButton.clicked.connect(self.on_prev_frame_button_clicked)
        self.playbar.nextFrameButton.clicked.connect(self.on_next_frame_button_clicked)
        self.labeltree.itemDoubleClicked.connect(self.tree_item_select)

        self.timer = QTimer()
        self.timer.start(int(1000 / self.model.kinematic_frame_rate()))

        self.timer.timeout.connect(self.update)

    def update(self):
        if self.playbar.is_playing():
            frames = self.model.kinematic_frames()
            rate = self.model.kinematic_frame_rate()
            self.frame += 1
            if self.frame >= frames:
                self.frame = 0
        self.render.bodyrender.setFrame(self.frame)
        self.notify()

    def on_play_button_clicked(self):
        self.notify()
    
    def on_prev_frame_button_clicked(self):
        self.frame -= 1
        if self.frame < 0:
            self.frame = 0
        self.notify()
    def on_next_frame_button_clicked(self):
        self.frame += 1
        if self.frame >= self.model.kinematic_frames():
            self.frame = self.model.kinematic_frames() - 1
        self.notify()
        
    def slider_valuechange(self, value):
        self.render.bodyrender.setFrame(value)
        self.playbar.slider.setValue(value)
        self.frame = value
        self.notify()

    def notify(self):
        self.render.notify(self.frame)
        self.playbar.notify(self.frame)
        self.top.update(self.frame)
        # self.bottom.notify(self.frame)

    def tree_item_select(self, index):
        self.top.clear()
        name = index.text(0)
        if name in self.model.kinematic.data.data:
            d = self.model.kinematic.data[name]
            xs, ys, zs = [], [], []
            for p in d:
                xs.append(p.xyz[0])
                ys.append(p.xyz[2])
                zs.append(p.xyz[1])
            self.top.add_line(np.arange(0, len(xs)), xs, name + ".x")
            self.top.add_line(np.arange(0, len(ys)), ys, name + ".y")
            self.top.add_line(np.arange(0, len(zs)), zs, name + ".z")
        if name in self.model.emg.Channels:
            x = self.model.emg.getLinspace()
            y = self.model.emg[name]
            self.top.add_line(x, y, name)
