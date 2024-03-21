from PySide6.QtCore import QEvent


class KeyEvent:
    def __init__(self, key, type):
        self.key = key
        self.type = type


class MouseEvent:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Input:
    def __init__(self) -> None:
        self.mouseLocation = MouseEvent(0, 0)
        self.mouseDrageLocation = MouseEvent(0, 0)
        self.mousePressed = False
        self.wheelMovement = 0

        self.keyDownList = []
        self.keyUpList = []
        self.keyPressedList = []
        self.keyEvents = []

    def update(self):
        self.keyDownList.clear()
        self.keyUpList.clear()
        # iterate over all user input events (such as keyboard or
        #  mouse) that occurred since the last time events were checked
        for event in self.keyEvents:
            # Check for keydown and keyup events;
            # get name of key from event
            # and append to or remove from corresponding lists
            if event.type == QEvent.KeyPress:
                self.keyDownList.append(event.key)
                self.keyPressedList.append(event.key)
            elif event.type == QEvent.KeyRelease:
                self.keyUpList.append(event.key)
                self.keyPressedList.remove(event.key)
        self.keyEvents = []

    # functions to check key states
    def isKeyDown(self, key):
        return key in self.keyDownList

    def isKeyUp(self, key):
        return key in self.keyUpList

    def isKeyPressed(self, key):
        return key in self.keyPressedList

    def receiveKeyEvent(self, key, type):
        self.keyEvents.append(KeyEvent(key, type))

    def isMouseDown(self, key):
        return self.mousePressed

    def mousePressEvent(self, event):
        print("Mouse pressed event")
        self.mouseLocation = MouseEvent(event.x(), event.y())
        self.mouseDrageLocation = MouseEvent(event.x(), event.y())
        self.mousePressed = True

    def mouseMoveEvent(self, event):
        print("Mouse move event")
        self.mouseDrageLocation = MouseEvent(event.x(), event.y())

    def mouseMovement(self):
        print("Mouse movement")
        x, y = (
            self.mouseLocation.x - self.mouseDrageLocation.x,
            self.mouseLocation.y - self.mouseDrageLocation.y,
        )
        self.mouseLocation = self.mouseDrageLocation
        return x, y

    def mouseReleaseEvent(self, event):
        print("Mouse released event")
        self.mousePressed = False
    
    def wheelEvent(self, event):
        self.wheelMovement= -event.angleDelta().y()
