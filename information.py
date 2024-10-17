from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt


class Information(QWidget):
    def __init__(self, to_wordle):
        super().__init__()
        self.to_wordle = to_wordle

        self.start()

    def start(self):
        self.back_button()
        self.page_name()
        self.show_letters()
        self.show_information()


    def back_button(self):
        button = QPushButton('←', self)
        button.clicked.connect(self.to_wordle)
        button.setStyleSheet("""
                                border-radius: 10px;
                                font-size: 30px;
                                color: #000000;
                                background-color: #FFFF00;
                                """)
        button.setGeometry(10, 10, 75, 40)
        button.show()

    def page_name(self):
        label = QLabel('ОБ ИГРЕ', self)
        label.setGeometry(90, 10, 350, 40)
        label.setStyleSheet("""
                            font-size: 25px;
                            color: #FFFFFF;
                            background-color: #000000;
                            """)
        label.setAlignment(Qt.AlignCenter)
        label.show()

    def show_letters(self):
        label = QLabel('A', self)
        label.setGeometry(15, 100, 60, 60)
        label.setStyleSheet("""
                                border: 2px solid #FFFF00;
                                border-radius: 10px;
                                font-size: 20px;
                                color: #000000;
                                background-color: #FFFF00;
                                """)
        label.setAlignment(Qt.AlignCenter)
        label.show()

        label = QLabel('A', self)
        label.setGeometry(15, 180, 60, 60)
        label.setStyleSheet("""
                                border: 2px solid #FFFFFF;
                                border-radius: 10px;
                                font-size: 20px;
                                color: #000000;
                                background-color: #FFFFFF;
                                """)
        label.setAlignment(Qt.AlignCenter)
        label.show()

        label = QLabel('A', self)
        label.setGeometry(15, 260, 60, 60)
        label.setStyleSheet("""
                                border: 2px solid #A9A9A9;
                                border-radius: 10px;
                                font-size: 20px;
                                color: #FFFFFF;
                                background-color: #A9A9A9
                                """)
        label.setAlignment(Qt.AlignCenter)
        label.show()

    def show_information(self):
        x, y = 90, 100
        text = ('- Буква стоит на правильном месте',
                '- Белый цвет говорит о наличии буквы в слове',
                '- Буквы нет в слове')

        for i in text:
            label = QLabel(i, self)
            label.setGeometry(x, y, 400, 60)
            label.setStyleSheet("""
                                    font-size: 20px;
                                    color: #FFFFFF;
                                    """)
            label.show()
            y += 80

