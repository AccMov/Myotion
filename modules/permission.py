class permission:
    LOGOUT = -1
    BASIC = 0

    def __init__(self):
        # widgets : perm_level
        self.wlist = {}
        # store stypesheets
        self.stylesheetsBackup = {}

        # current permission level
        # disable widget when current perm_level is smaller
        self.perm_level = permission.LOGOUT

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