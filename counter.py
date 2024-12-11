from PyQt5.QtGui import QColor

class Counter:
    def __init__(self, x: int, y: int, colour: QColor):
        self.x = x
        self.y = y
        self.colour = colour

    def get_position(self):
        return (self.x, self.y)

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y
