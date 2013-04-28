#! /usr/bin/python

import sys
from PyQt4 import QtGui

from chizu.view import main_window

def runApp():
    app = QtGui.QApplication(sys.argv)
    window = main_window.MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    runApp()