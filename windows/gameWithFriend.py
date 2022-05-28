import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

from tools import connection_of_elements_place, remove_duplicate_characters


def exit_app():
    sys.exit()


class GameWithFriendWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(GameWithFriendWindow, self).__init__()
        self.turn = None
        self.buttons_game = None
        self.game_place = None
        loadUi("ui/gamePlace.ui", self)
        self.init_app()

    def init_app(self):
        self.exitButton.clicked.connect(exit_app)
        self.resetButton.clicked.connect(self.reset_game)
        self.backButton.clicked.connect(self.back_to_menu)
        self.game_place = [[0 for j in range(3)] for i in range(3)]
        self.buttons_game = [[self.btn00, self.btn01, self.btn02],
                             [self.btn10, self.btn11, self.btn12],
                             [self.btn20, self.btn21, self.btn22]]
        self.turn = 0
        for index_row, row in enumerate(self.buttons_game):
            for index_col, col in enumerate(row):
                self.buttons_game[index_row][index_col].clicked.connect(
                    lambda checked, coord=(index_row, index_col): self.click_place(coord)
                )

    def back_to_menu(self):
        # self.setCentralWidget()
        pass

    def reset_game(self):
        self.game_place = [[0 for j in range(3)] for i in range(3)]
        self.turn = 0
        self.infoLabel.setText(' ')
        self.infoLabel.setStyleSheet("QLabel {margin: 10px; border-radius: 10px; font-size: 28px; background-color: transparent;}")
        self.update_btn()

    def click_place(self, coord):
        el_game_place = self.game_place[coord[0]][coord[1]]
        if el_game_place == 0:
            if self.turn == 0:
                self.game_place[coord[0]][coord[1]] = 1
                self.turn = 1
            else:
                self.game_place[coord[0]][coord[1]] = 2
                self.turn = 0
        self.update_btn()

    def update_btn(self):
        for index_row, row in enumerate(self.game_place):
            for index_col, col in enumerate(row):
                element_index = {0: ' ', 1: 'X', 2: 'О'}
                for i in element_index:
                    if self.game_place[index_row][index_col] == i:
                        self.buttons_game[index_row][index_col].setText(element_index[i])
        self.check_win()

    def check_win(self):
        code_win = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)]
        element_index = {0: ' ', 1: 'X', 2: 'О'}

        for code in code_win:
            elements_string = connection_of_elements_place(code, self.game_place)
            string_without_repetition = remove_duplicate_characters(elements_string)
            if len(string_without_repetition) == 1 and string_without_repetition != '0':
                self.infoLabel.setText(f'{element_index[int(string_without_repetition)]} win!')
                self.infoLabel.setStyleSheet("QLabel {margin: 10px; border-radius: 10px; font-size: 28px; background-color: #9FADBD;}")