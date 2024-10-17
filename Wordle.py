from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt, QTimer
import random as rnd


class Wordle(QWidget):
    def __init__(self, to_information):
        super().__init__()
        self.to_information = to_information
        self.window_size = (521, 750)

        self.start()

    def start(self):
        self.word = self.get_word()
        self.buttons = {}
        self.input_fields = []
        self.row = 0
        self.column = 0
        self.win = False
        self.timer = QTimer()

        self.draw_game_name()
        self.create_manage_buttons()
        self.create_input_fields()
        self.create_buttons()

    def draw_game_name(self):
        x, y = 12, 10
        for i in 'WORDLE':
            label = QLabel(i, self)
            label.setGeometry(x, y, 40, 40)
            label.setStyleSheet("""
                                    border-radius: 10px;
                                    font-size: 20px;
                                    color: #000000;
                                    background-color: #FFFF00;
                                    """)
            label.setAlignment(Qt.AlignCenter)
            label.show()
            x += 42

    def create_manage_buttons(self):
        button_settings = QPushButton('i', self)
        button_settings.clicked.connect(self.to_information)
        button_settings.setStyleSheet("""
                                        border-radius: 10px;
                                        font-size: 30px;
                                        color: #FFFFFF;
                                        background-color: #A9A9A9;
                                        """)
        button_settings.setGeometry(469, 10, 40, 40)
        button_settings.show()
        self.buttons['i'] = button_settings

    def create_buttons(self):
        x, y = 4, self.window_size[1] - 200
        for letter in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
            self.create_button_letter(x, y, 40, 55, letter)
            x += 43
            if letter == 'Ъ':
                x, y = 25, self.window_size[1] - 135
            elif letter == 'Э':
                x, y = 68, self.window_size[1] - 70

        button_erase = QPushButton('⌫', self)
        button_erase.clicked.connect(self.on_click_button_erase)
        button_erase.setStyleSheet("""
                                    border-radius: 10px;
                                    font-size: 25px;
                                    color: #FFFFFF;
                                    background-color: #A9A9A9;
                                    """)
        button_erase.setGeometry(x, y, 61, 55)
        button_erase.show()
        self.buttons['⌫'] = button_erase

        button_ok = QPushButton('✓', self)
        button_ok.clicked.connect(self.on_click_button_ok)
        button_ok.setStyleSheet("""
                                border-radius: 10px;
                                font-size: 25px;
                                color: #000000;
                                background-color: #FFFF00;
                                """)
        button_ok.setGeometry(4, self.window_size[1] - 70, 61, 55)
        button_ok.show()
        self.buttons['✓'] = button_ok

    def create_input_fields(self):
        x, y = 96, 110
        for i in range(6):
            self.input_fields.append([])
            for j in range(5):
                label = QLabel('', self)
                label.setGeometry(x, y, 60, 60)
                label.setStyleSheet("""
                                border: 2px solid #FFFF00;
                                border-radius: 10px;
                                font-size: 20px;
                                color: #FFFFFF;
                                background-color: #000000;
                                """)
                label.setAlignment(Qt.AlignCenter)
                label.show()
                self.input_fields[i].append(label)
                x += 67
            x, y = 96, y + 68

    def create_button_letter(self, x, y, width, height, text):
        button = QPushButton(text, self)
        button.clicked.connect(lambda: self.on_click_button_letter(text))
        button.setStyleSheet("""
                            border: 2px solid #A9A9A9;
                            border-radius: 10px;
                            font-size: 20px;
                            color: #FFFFFF;
                            background-color: #000000;
                            """)
        button.setGeometry(x, y, width, height)
        button.show()
        self.buttons[text] = button

    def on_click_button_letter(self, button_name):
        input_field = self.input_fields[self.row][self.column]

        if len(input_field.text()) == 0:
            input_field.setText(input_field.text() + button_name)
            if self.column < 4:
                self.column += 1

    def on_click_button_erase(self):
        input_field = self.input_fields[self.row][self.column]

        if len(input_field.text()) > 0:
            input_field.setText('')
        else:
            if self.column > 0:
                self.column -= 1
                self.on_click_button_erase()

    def on_click_button_ok(self):
        input_field = self.input_fields[self.row][self.column]

        if self.row < 6 and self.column == 4 and len(input_field.text()) > 0:

            c = self.count_and_draw_right_letters()

            if c == 5 or self.row == 5:
                self.win = c == 5
                self.timer.timeout.connect(self.show_result)
                self.timer.start(500)

            self.row += 1
            self.column = 0

    def count_and_draw_right_letters(self):
        c = 0
        for i in range(len(self.input_fields[self.row])):
            input_field = self.input_fields[self.row][i]
            b = input_field.text()
            button = self.buttons[b]
            b = b.lower()

            color = '#A9A9A9'
            font_color = '#FFFFFF'
            if b == self.word[i]:
                color = '#FFFF00'
                font_color = '#000000'
                c += 1
            elif b in self.word:
                color = '#FFFFFF'
                font_color = '#000000'

            input_field.setStyleSheet(f"""
                                border: 2px solid {color};
                                border-radius: 10px;
                                font-size: 20px;
                                color: {font_color};
                                background-color: {color};
                                """)

            cur_style_button = button.styleSheet()
            if 'background-color: #FFFF00;' not in cur_style_button:
                button.setStyleSheet(f"""
                                    border: 2px solid {color};
                                    border-radius: 10px;
                                    font-size: 20px;
                                    color: {font_color};
                                    background-color: {color};
                                    """)
        return c

    def show_result(self):
        self.timer.stop()
        result = 'ПРОИГРЫШ'
        color = '#FF0000'
        if self.win:
            result = 'ПОБЕДА'
            color = '#00FF00'

        frame = QFrame(self)
        frame.setGeometry(0, 0, self.window_size[0], self.window_size[1])
        frame.setStyleSheet('background-color: rgba(0, 0, 0, 0.9);')
        frame.show()

        label = QLabel(result, self)
        label.setGeometry(135, 270, 250, 50)
        label.setStyleSheet(f"""
                            border: 2px solid #FFFF00;
                            border-radius: 10px;
                            font-size: 20px;
                            color: {color};
                            background-color: #000000;
                            """)
        label.setAlignment(Qt.AlignCenter)
        label.show()

        button = QPushButton('Продолжить', self)
        button.clicked.connect(self.nex_level)
        button.setStyleSheet("""
                                border: 2px solid #A9A9A9;
                                border-radius: 10px;
                                font-size: 20px;
                                color: #FFFFFF;
                                background-color: #000000;
                                """)
        button.setGeometry(135, 345, 250, 50)
        button.show()

    def nex_level(self):
        for widget in self.findChildren(QWidget):
            widget.deleteLater()

        self.update()
        self.start()

    def get_word(self):
        with open('resources/words.txt') as file:
            return rnd.choice(file.readlines())
