import sys

from PyQt5 import QtWidgets

from windows.menuGame import MenuGame


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MenuGame()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
