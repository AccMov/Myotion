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

        if len(username.strip()) == 0 or len(password.strip()) == 0:
            QMessageBox.warning(
                self,
                self.tr("Error"),
                self.tr("Username and password are required"),
            )
            return

        ret = bm.login(username, password)
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Icon.Warning)
        mb.setWindowTitle(self.tr("Error"))
        mb.setStyleSheet("QMessagebox{background-color: black;}"
                         "QPushButton{background-color: #333; color: white;}")
        if ret.status_code == 200:
            self.user = ret.json()
            self.accept()
            return
        elif ret.status_code == 401:
            mb.setText(self.tr("Invalid username or password"))
        elif ret.status_code == 403:
            mb.setText(self.tr("User is already logged in in another place, please log out first!"))
        elif ret.status_code == 408:
            mb.setText(self.tr("Connection to server timed out. Please try again."))
        elif ret.status_code == 495:
            mb.setText(self.tr("Secure connection to server failed. Please contact support."))
        elif ret.status_code == 503:
            mb.setText(self.tr("Unable to connect to server. Please check your network or try again later."))
        elif ret.status_code == 500:
            if "can not find tenant for key" in ret.json().get("message", ""):
                mb.setText(self.tr("User is not registered, please contact admin"))
            elif ret.error_message:
                mb.setText(self.tr(ret.error_message))
            else:
                mb.setText(self.tr("Unknown error, please contact support"))
        else:
            mb.setText(self.tr(ret.error_message or "Login failed, please try again."))
        mb.exec()
            

    def register(self):
        webbrowser.open("https://www.accmov.com")
