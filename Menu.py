from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt


class Menu(QWidget):
    def __init__(self, to_wordle):
        super().__init__()
        self.to_wordle = to_wordle

        self.start()

    def start(self):
        self.draw_game_name()

        button = QPushButton('Играть', self)
        button.clicked.connect(self.to_wordle)
        button.setStyleSheet("""
                        border: 2px solid #A9A9A9;
                        border-radius: 10px;
                        font-size: 20px;
                        color: #FFFFFF;
                        background-color: #000000;
                        """)
        button.setGeometry(135, 345, 250, 50)
        button.show()

    def draw_game_name(self):
        x, y = 85, 250
        for i in 'WORDLE':
            label = QLabel(i, self)
            label.setGeometry(x, y, 55, 55)
            label.setStyleSheet("""
                                    border-radius: 10px;
                                    font-size: 25px;
                                    color: #000000;
                                    background-color: #FFFF00;
                                    """)
            label.setAlignment(Qt.AlignCenter)
            label.show()
            x += 59
