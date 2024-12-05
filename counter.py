from PyQt5.QtGui import QColor

class Counter:
    def __init__(self, x: int, y: int, color: QColor):
        self.x = x
        self.y = y
        self.color = color

    def get_position(self):
        pass

    def set_position(self, x: int, y: int):
        pass
