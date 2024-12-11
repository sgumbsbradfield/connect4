from player import Player
from grid import Grid

class Game:
    def __init__(self, player1: Player, player2: Player, grid: Grid):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.grid = grid

    def switch_turn(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play_turn(self, col: int):
        if self.grid.is_column_full(col):
            raise ValueError(f"Column {col} is full")
        row, col = self.grid.drop_piece(col, self.current_player.get_color())
        return row, col

    def check_game_over(self):
        winner_color = self.grid.check_winner()
        if winner_color:
            if winner_color == self.player1.get_color():
                return self.player1
            elif winner_color == self.player2.get_color():
                return self.player2
        return None

    def reset_game(self):
        self.grid.reset_grid()
        self.current_player = self.player1
