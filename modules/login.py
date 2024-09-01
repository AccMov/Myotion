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
        ret = bm.get_tenant(username, password)
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Icon.Warning)
        mb.setWindowTitle("Error")
        mb.setStyleSheet("QMessagebox{background-color: black;}"
                         "QPushButton{background-color: #333; color: white;}")
        if ret.status_code == 200:
            self.user = ret.json()
            self.accept()
            return
        elif ret.status_code == 401:
            mb.setText("Invalid username or password")
        elif ret.status_code == 500:
            if "can not find tenant for key" in ret.json()["message"]:
                mb.setText("User is not registered, please contact admin")
            mb.setText("Unknown error, please contact support")
        mb.exec()
            

    def register(self):
        webbrowser.open("https://www.accmov.com")
