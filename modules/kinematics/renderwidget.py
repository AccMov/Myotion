from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QBoxLayout
from PySide6 import QtCore

from .bodyrender import BodyRender


class RenderWidget(QWidget):
    """a top widget for bodyrender and placeholder
    if there is no model set for render it should show placeholder
    otherwise, render the model in bodyrender and set it as central widget
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.bodyrender = BodyRender()
        self.placeholder = QLabel("No model to render")
        self.vblayout = QVBoxLayout()
        self.vblayout.addWidget(self.placeholder)
        self.setLayout(self.vblayout)

    def update(self):
        if self.bodyrender.model:
            self.vblayout.removeWidget(self.placeholder)
            self.vblayout.addWidget(self.bodyrender)
        else:
            self.vblayout.removeWidget(self.bodyrender)
            self.vblayout.addWidget(self.placeholder)

    def setModel(self, model):
        self.bodyrender.setModel(model)
        self.update()
