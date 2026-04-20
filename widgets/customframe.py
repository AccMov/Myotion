from PySide6.QtWidgets import QFrame
from PySide6.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent


type = "application/x-qabstractitemmodeldatalist"


class CustomFrame(QFrame):
    def __init__(self, parent: QFrame | None = ...) -> None:
        super().__init__(parent)
        self.setAcceptDrops(True)

    def setModel(self, model, tree):
        self.model = model
        self.tree = tree

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasFormat(type):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        if event.mimeData().hasFormat(type):
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent) -> None:
        pass
    