from PyQt5.QtWidgets import QWidget, QPushButton


class Menu(QWidget):
    def __init__(self, to_wordle):
        super().__init__()
        self.to_wordle = to_wordle

        self.start()

    def start(self):
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




