from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTreeWidget


class CustomTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mimeData(self, item):
        super().mimeData(item)
    
    def startDrag(self, supportedActions: Qt.DropAction) -> None:
        return super().startDrag(supportedActions)
