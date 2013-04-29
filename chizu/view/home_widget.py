from PyQt4 import Qt, QtGui, QtCore
from PyQt4.QtCore import Qt

from chizu import settings


class HomeWidget(QtGui.QWidget):

    def __init__(self):
        super(HomeWidget, self).__init__()
        self.initUI()

    def initUI(self):
        print "TO NA INDEX!!!!!!"
        self.show()