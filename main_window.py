from PyQt5.QtWidgets import QMainWindow
from game import Game
from player import Player
from grid import Grid

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connect 4")
        self.init_ui()

    def init_ui(self):
        pass

    def start_new_game(self):
        pass

    def on_column_clicked(self, col: int):
        pass

    def update_ui(self):
        pass

    def display_winner(self, winner: Player):
        pass

    def reset_game(self):
        pass
