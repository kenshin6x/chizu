from PyQt4 import Qt, QtGui, QtCore
from PyQt4.QtCore import Qt

from chizu import settings


class HomeWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(HomeWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QtGui.QHBoxLayout()

        self.button = QtGui.QPushButton('Login')
        layout.addWidget(self.button)
