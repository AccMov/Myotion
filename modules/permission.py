from .api import bill_management as bm
import threading
import time

def serverHeartbeat(username, password, status):
    ret = bm.heartBeat(username, password)
    if ret.status_code == 200:
        return 0
    elif ret.status_code == 401 or ret.status_code == 500:
        assert("invalid password/username or internal error")
    elif ret.status_code == 408:
        ret = bm.heartBeat(username, password)
        if ret.status_code == 408:
            status.code = -1


class permission:
    LOGOUT = -1
    BASIC = 0

    def __init__(self):
        # widgets : perm_level
        self.wlist = {}
        # store stypesheets
        self.stylesheetsBackup = {}
        # user state
        self.timer = None
        self.heartThread = None
        self.account = None
        self.th_run = 0

        # current permission level
        # disable widget when current perm_level is smaller
        self.perm_level = permission.LOGOUT

    def __del__(self):
        self.th_run = 0

    def __update(self, w):
        if w not in self.wlist:
            return
        
        if self.wlist[w] > self.perm_level:
            self.stylesheetsBackup[w] = w.styleSheet()
            w.setStyleSheet("color: gray")
            w.setDisabled(True)
        else:
            w.setStyleSheet(self.stylesheetsBackup[w])
            w.setDisabled(False)

    def register(self, widget, p_level):
        self.wlist[widget] = p_level
        self.__update(widget)

    def setPermLevel(self, target_level):
        if self.perm_level == target_level:
            return 0
        
        self.perm_level = target_level

        for w, p in self.wlist.items():
            self.__update(w)

    def serverHeartbeat(self, username, password):
        ret = bm.heartBeat(username, password)
        if ret.status_code == 401 or ret.status_code == 500:
            assert("invalid password/username or internal error")
        elif ret.status_code == 408:
            ret = bm.heartBeat(username, password)
            if ret.status_code == 408:
                return -1
        return 0

    def serverHeartRun(self):
        while self.th_run:
            th = threading.Thread(target = self.serverHeartbeat, args = (self.account.username, self.account.password))
            th.start()
            rc = th.join()
            if rc == -1:
                self.setPermLevel(permission.LOGOUT)
                mb = QMessageBox()
                mb.setIcon(QMessageBox.Icon.Warning)
                mb.setWindowTitle(self.tr("Error"))
                mb.setStyleSheet("QMessagebox{background-color: black;}"
                                "QPushButton{background-color: #333; color: white;}")
                mb.setText(self.tr("Lost connection to server, logged out!"))
                mb.exec()
                break
            else:
                time.sleep(1)     

    def startServerHeartbeat(self, _account):
        self.account = _account
        self.heartThread = threading.Thread(target = self.serverHeartRun)
        self.th_run = 1
        self.heartThread.daemon = True
        self.heartThread.start()

    def stopServerHeartbeat(self):
        if self.heartThread:
            self.th_run = 0
            self.heartThread.join()
        self.heartThread = None