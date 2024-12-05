from PyQt5.QtGui import QColor

class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = []

    def initialize_grid(self):
        pass

    def drop_piece(self, col: int, color: QColor):
        pass

    def is_column_full(self, col: int):
        pass

    def check_winner(self):
        pass

    def reset_grid(self):
        pass
