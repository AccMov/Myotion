import webbrowser
from PySide6.QtWidgets import QDialog, QMessageBox

from modules.ui_login import Ui_Form

from .api import bill_management as bm


class LoginDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.register)

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        ret = bm.login(username, password)
        if ret.status_code == 200:
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password")

    def register(self):
        webbrowser.open("https://www.accmov.com")

    def accept(self):
        super().accept()
        return "Accepted"
