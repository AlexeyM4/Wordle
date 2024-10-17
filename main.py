from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow
from PyQt5.QtGui import QIcon
import sys

from information import Information
from Wordle import Wordle
from Menu import Menu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()

        self.menu = Menu(self.to_wordle)
        self.wordle = Wordle(self.to_information)
        self.information = Information(self.to_wordle)

        self.stacked_widget.addWidget(self.menu)
        self.stacked_widget.addWidget(self.wordle)
        self.stacked_widget.addWidget(self.information)

        self.initUI()

    def initUI(self):
        self.setCentralWidget(self.stacked_widget)

        self.setWindowIcon(QIcon('resources/icon.png'))
        self.setWindowTitle('Wordle')
        self.setFixedSize(521, 750)
        self.move(500, 0)
        self.setStyleSheet("background-color: black;")

    def to_wordle(self):
        self.stacked_widget.setCurrentIndex(1)

    def to_menu(self):
        self.stacked_widget.setCurrentIndex(0)

    def to_information(self):
        self.stacked_widget.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('resources/icon.png'))

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
