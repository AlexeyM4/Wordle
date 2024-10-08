from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt, QTimer
import random as rnd


class Wordle(QWidget):
    def __init__(self, to_menu):
        super().__init__()
        self.to_menu = to_menu
        self.__window_size = (521, 750)

        self.__start()

    def __start(self):
        self.__word = 'ворон'  # self.__get_word()
        self.__buttons = {}
        self.__input_fields = []
        self.__row = 0
        self.__column = 0
        self.__win = False
        self.timer = QTimer()

        self.__draw_game_name()
        self.__create_manage_buttons()
        self.__create_input_fields()
        self.__create_buttons()

    def __draw_game_name(self):
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

    def __create_manage_buttons(self):
        button_menu = QPushButton('☰', self)
        button_menu.clicked.connect(self.to_menu)
        button_menu.setStyleSheet("""
                                    border-radius: 10px;
                                    font-size: 30px;
                                    color: #FFFFFF;
                                    background-color: #A9A9A9;
                                    """)
        button_menu.setGeometry(420, 10, 40, 40)
        button_menu.show()
        self.__buttons['☰'] = button_menu

        button_settings = QPushButton('⚙', self)
        button_settings.clicked.connect(lambda: print('⚙'))
        button_settings.setStyleSheet("""
                                                border-radius: 10px;
                                                font-size: 30px;
                                                color: #FFFFFF;
                                                background-color: #A9A9A9;
                                                """)
        button_settings.setGeometry(469, 10, 40, 40)
        button_settings.show()
        self.__buttons['⚙'] = button_settings

    def __create_buttons(self):
        x, y = 4, self.__window_size[1] - 200
        for letter in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
            self.__create_button_letter(x, y, 40, 55, letter)
            x += 43
            if letter == 'Ъ':
                x, y = 25, self.__window_size[1] - 135
            elif letter == 'Э':
                x, y = 68, self.__window_size[1] - 70

        button_erase = QPushButton('⌫', self)
        button_erase.clicked.connect(self.__on_click_button_erase)
        button_erase.setStyleSheet("""
                                    border-radius: 10px;
                                    font-size: 25px;
                                    color: #FFFFFF;
                                    background-color: #A9A9A9;
                                    """)
        button_erase.setGeometry(x, y, 61, 55)
        button_erase.show()
        self.__buttons['⌫'] = button_erase

        button_ok = QPushButton('✓', self)
        button_ok.clicked.connect(self.__on_click_button_ok)
        button_ok.setStyleSheet("""
                                border-radius: 10px;
                                font-size: 25px;
                                color: #000000;
                                background-color: #FFFF00;
                                """)
        button_ok.setGeometry(4, self.__window_size[1] - 70, 61, 55)
        button_ok.show()
        self.__buttons['✓'] = button_ok

    def __create_input_fields(self):
        x, y = 96, 110
        for i in range(6):
            self.__input_fields.append([])
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
                self.__input_fields[i].append(label)
                x += 67
            x, y = 96, y + 68

    def __create_button_letter(self, x, y, width, height, text):
        button = QPushButton(text, self)
        button.clicked.connect(lambda: self.__on_click_button_letter(text))
        button.setStyleSheet("""
                            border: 2px solid #A9A9A9;
                            border-radius: 10px;
                            font-size: 20px;
                            color: #FFFFFF;
                            background-color: #000000;
                            """)
        button.setGeometry(x, y, width, height)
        button.show()
        self.__buttons[text] = button

    def __on_click_button_letter(self, button_name):
        input_field = self.__input_fields[self.__row][self.__column]

        if len(input_field.text()) == 0:
            input_field.setText(input_field.text() + button_name)
            if self.__column < 4:
                self.__column += 1

    def __on_click_button_erase(self):
        input_field = self.__input_fields[self.__row][self.__column]

        if len(input_field.text()) > 0:
            input_field.setText('')
        else:
            if self.__column > 0:
                self.__column -= 1
                self.__on_click_button_erase()

    def __on_click_button_ok(self):
        input_field = self.__input_fields[self.__row][self.__column]

        if self.__row < 6 and self.__column == 4 and len(input_field.text()) > 0:

            c = self.__count_and_draw_right_letters()

            if c == 5 or self.__row == 5:
                self.__win = c == 5
                self.timer.timeout.connect(self.__show_result)
                self.timer.start(500)

            self.__row += 1
            self.__column = 0

    def __count_and_draw_right_letters(self):
        c = 0
        for i in range(len(self.__input_fields[self.__row])):
            input_field = self.__input_fields[self.__row][i]
            b = input_field.text()
            button = self.__buttons[b]
            b = b.lower()

            color = '#A9A9A9'
            font_color = '#FFFFFF'
            if b == self.__word[i]:
                color = '#FFFF00'
                font_color = '#000000'
                c += 1
            elif b in self.__word:
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

    def __show_result(self):
        self.timer.stop()
        result = 'ПРОИГРЫШ'
        color = '#FF0000'
        if self.__win:
            result = 'ПОБЕДА'
            color = '#00FF00'

        frame = QFrame(self)
        frame.setGeometry(0, 0, self.__window_size[0], self.__window_size[1])
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
        button.clicked.connect(self.__nex_level)
        button.setStyleSheet("""
                                border: 2px solid #A9A9A9;
                                border-radius: 10px;
                                font-size: 20px;
                                color: #FFFFFF;
                                background-color: #000000;
                                """)
        button.setGeometry(135, 345, 250, 50)
        button.show()

    def __nex_level(self):
        for widget in self.findChildren(QWidget):
            widget.deleteLater()

        self.update()
        self.__start()

    def __get_word(self):
        with open('resources/words.txt') as file:
            return rnd.choice(file.readlines())
