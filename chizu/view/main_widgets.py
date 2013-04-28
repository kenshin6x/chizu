from PyQt4 import QtGui, QtCore
from chizu import settings


class HomeWidget(QtGui.QWidget):

    def __init__(self):
        super(HomeWidget, self).__init__()
        self.initUI()

    def initUI(self):
        print "TO NA INDEX!!!!!!"
        self.show()


class PlayersWidget(QtGui.QWidget):

    def __init__(self):
        super(PlayersWidget, self).__init__()
        self.initUI()

    def initUI(self):
        lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.show()
