from PyQt5.QtGui import QColor

from counter import Counter


class Grid:
    def __init__(self, rows: int = 6, cols: int = 7):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def initialize_grid(self):
        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]

    def drop_piece(self, col: int, colour: QColor):
        for row in range(0, self.row -1):
            if self.grid[row][col] is None:
                self.grid[row][col] = Counter(row, col, colour)

    def is_column_full(self, col: int):
        return self.grid[0][col] is not None

    def check_winner(self):
        # Check horizontal, vertical, diagonal (positive & negative slopes)
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] is None:
                    continue
                colour = self.grid[row][col].colour
                for dr, dc in directions:
                    if self._check_direction(row, col, dr, dc, colour):
                        return colour
        return None

    def _check_direction(self, row, col, dr, dc, colour):
        count = 0
        for i in range(4):  # Need 4 in a row
            r, c = row + i * dr, col + i * dc
            if 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] is not None and self.grid[r][c].colour == colour:
                count += 1
            else:
                break
        return count == 4

    def reset_grid(self):
        self.initialize_grid()
