import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

from windows.gameWithFriend import GameWithFriendWindow


def exit_app():
    sys.exit()


class MenuGame(QtWidgets.QMainWindow):
    def __init__(self):
        super(MenuGame, self).__init__()
        self.game_friend = None
        loadUi("ui/menuGame.ui", self)
        self.init_app()

    def init_app(self):
        self.game_friend = GameWithFriendWindow()

        triple_agent = QPixmap('ui/resourse/logo.png').scaled(100, 100)
        self.logoLabel.setPixmap(triple_agent)
        self.gameFriend.clicked.connect(self.set_friend_game)

    def set_friend_game(self):
        self.setCentralWidget(self.game_friend)


