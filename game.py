from player import Player
from grid import Grid

class Game:
    def __init__(self, player1: Player, player2: Player, grid: Grid):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.grid = grid

    def switch_turn(self):
        pass

    def play_turn(self, col: int):
        pass

    def check_game_over(self):
        pass

    def reset_game(self):
        pass
