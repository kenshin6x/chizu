#! /usr/bin/python

from PyQt4 import QtGui

from chizu.gui.main import Main


if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = Main()
    window.show()
    app.exec_()
