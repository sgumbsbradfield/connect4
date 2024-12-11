from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from game import Game
from player import Player
from grid import Grid

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connect 4")
        self.game = Game(
            Player("Player 1", QColor("red")),
            Player("Player 2", QColor("yellow")),
            Grid()
        )
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        self.buttons = []

        for col in range(self.game.grid.cols):
            button = QPushButton(f"Drop in {col + 1}")
            button.clicked.connect(lambda _, col: self.on_column_clicked(col))
            self.grid_layout.addWidget(button, 0, col)
            self.buttons.append(button)

        self.grid_labels = [[QLabel("") for _ in range(self.game.grid.cols)] for _ in range(self.game.grid.rows)]
        for row in range(self.game.grid.rows):
            for col in range(self.game.grid.cols):
                self.grid_layout.addWidget(self.grid_labels[row][col], row + 1, col)

        central_widget = QWidget()
        central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(central_widget)

    def on_column_clicked(self, col: int):
        try:
            row, col = self.game.play_turn(col)
            self.update_ui(row, col)
            winner = self.game.check_game_over()
            if winner:
                self.display_winner(winner)
        except ValueError as e:
            QMessageBox.warning(self, "Invalid Move", str(e))

    def update_ui(self, row: int, col: int):
        piece = self.game.grid.grid[row][col]
        color = piece.color.name()
        self.grid_labels[row][col].setStyleSheet(f"background-color: {color}; border: 1px solid black;")

    def display_winner(self, winner: Player):
        QMessageBox.information(self, "Game Over", f"{winner.get_name()} wins!")
        self.game.reset_game()
        self.reset_game()

    def reset_game(self):
        for row in range(self.game.grid.rows):
            for col in range(self.game.grid.cols):
                self.grid_labels[row][col].setStyleSheet("")
