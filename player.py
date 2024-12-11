from PyQt5.QtGui import QColor

class Player:
    def __init__(self, name: str, colour: QColor):
        self.name = name
        self.colour = colour

    def get_name(self):
        return self.name

    def get_color(self):
        return self.colour
