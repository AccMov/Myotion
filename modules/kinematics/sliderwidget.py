from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt

class SliderWidget(QSlider):
    def __init__(self, parent=None):
        super().__init__(Qt.Orientation.Horizontal, parent)
        self.setRange(0, 1000)
        self.setValue(0)
        self.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.setTickInterval(10)
        self.setSingleStep(1)

        self.valueChanged.connect(self.on_slider_value_changed)

    def on_slider_value_changed(self, value):
        print(value)
    
    def mousePressEvent(self,event):
        self.setValue(self.minimum() + (self.maximum() - self.minimum()) * event.x() / self.width())
    
    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        # if mouse is pressed and moving change value of slider
        if ev.buttons() == Qt.LeftButton:
            self.setValue(self.minimum() + (self.maximum() - self.minimum()) * ev.x() / self.width())

    def set_value(self, value):
        self.setValue(value)

    def get_value(self):
        return self.value()