import sys

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi


def exit_app():
    sys.exit()


def set_place_default_position():
    GAME_PLACE = [[0 for j in range(3)] for i in range(3)]


class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(ExampleApp, self).__init__()
        self.turn = None
        self.buttons_game = None
        self.game_place = None
        loadUi("ui/gamePlace.ui", self)
        self.init_app()

    def init_app(self):
        self.exitButton.clicked.connect(exit_app)
        self.resetButton.clicked.connect(self.reset_game)
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

    def reset_game(self):
        self.game_place = [[0 for j in range(3)] for i in range(3)]
        self.turn = 0
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
                if self.game_place[index_row][index_col] == 0:
                    self.buttons_game[index_row][index_col].setText(' ')
                elif self.game_place[index_row][index_col] == 1:
                    self.buttons_game[index_row][index_col].setText('X')
                elif self.game_place[index_row][index_col] == 2:
                    self.buttons_game[index_row][index_col].setText('O')



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()
