import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox, QVBoxLayout
from PyQt6.QtCore import Qt

class Demineur(QWidget):
    def __init__(self, rows=10, cols=10, mines=15):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.mines_positions = set()
        self.flags = set()
        
        self.initUI()
        self.place_mines()
        self.calculate_numbers()
    
    def initUI(self):
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()
        
        for i in range(self.rows):
            for j in range(self.cols):
                btn = QPushButton(" ")
                btn.setFixedSize(40, 40)
                btn.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                btn.clicked.connect(lambda _, x=i, y=j: self.reveal_cell(x, y))
                btn.customContextMenuRequested.connect(lambda _, x=i, y=j: self.toggle_flag(x, y))
                grid_layout.addWidget(btn, i, j)
                self.buttons[i][j] = btn
        
        self.help_button = QPushButton("Aide IA")
        self.help_button.clicked.connect(self.ai_help)
        
        main_layout.addLayout(grid_layout)
        main_layout.addWidget(self.help_button)
        
        self.setLayout(main_layout)
        self.setWindowTitle("Démineur")
        self.show()
    
    def place_mines(self):
        count = 0
        while count < self.mines:
            x, y = random.randint(0, self.rows-1), random.randint(0, self.cols-1)
            if (x, y) not in self.mines_positions:
                self.mines_positions.add((x, y))
                self.grid[x][y] = -1
                count += 1
    
    def calculate_numbers(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for x, y in self.mines_positions:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] != -1:
                    self.grid[nx][ny] += 1
    
    def reveal_cell(self, x, y):
        if (x, y) in self.flags:
            return
        
        if self.grid[x][y] == -1:
            self.buttons[x][y].setText("💣")
            self.game_over(False)
        else:
            self.buttons[x][y].setText(str(self.grid[x][y]) if self.grid[x][y] > 0 else "")
            self.buttons[x][y].setEnabled(False)
            if self.grid[x][y] == 0:
                self.expand_empty_cells(x, y)
        self.check_win()
    
    def expand_empty_cells(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.buttons[nx][ny].isEnabled():
                self.reveal_cell(nx, ny)
    
    def toggle_flag(self, x, y):
        if not self.buttons[x][y].isEnabled():
            return
        
        if (x, y) in self.flags:
            self.buttons[x][y].setText(" ")
            self.flags.remove((x, y))
        else:
            self.buttons[x][y].setText("🚩")
            self.flags.add((x, y))
    
    def check_win(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] != -1 and self.buttons[i][j].isEnabled():
                    return
        self.game_over(True)
    
    def game_over(self, won):
        for x, y in self.mines_positions:
            self.buttons[x][y].setText("💣")
        
        msg = QMessageBox()
        msg.setWindowTitle("Fin du jeu")
        msg.setText("Bravo, vous avez gagné !" if won else "Dommage, vous avez perdu !")
        msg.exec()
        self.close()
    
    def ai_help(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.buttons[i][j].isEnabled() and self.grid[i][j] == 0:
                    self.buttons[i][j].setStyleSheet("background-color: lightgreen;")
                    return  # On suggère un seul coup sûr
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.buttons[i][j].isEnabled() and self.grid[i][j] != -1:
                    self.buttons[i][j].setStyleSheet("background-color: yellow;")
                    return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Demineur()
    sys.exit(app.exec())