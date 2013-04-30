#! /usr/bin/python

from PyQt4 import QtGui

from chizu.view import main_window


if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = main_window.MainWindow()
    window.show()
    app.exec_()
