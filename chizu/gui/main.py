from PyQt4 import Qt, QtGui, QtCore
from PyQt4.QtCore import Qt

from chizu.lib import settings
from chizu.lib.base.gui import BaseWindow

from chizu.gui.slaves import playerslave

class Main(BaseWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.playerListSlave = playerslave.PlayerListSlave(self)

        self.setupUi()

    def setupUi(self):
        super(Main, self).setupUi()

        self.createActions()
        self.createMenus()

        # create
        self.homeDetailSlave = QtGui.QWidget()

        # define all avaliabre widgets to main window
        self.central_widget.addWidget(self.homeDetailSlave)
        self.central_widget.addWidget(self.playerListSlave)

        # the initial widget to display
        self.central_widget.setCurrentWidget(self.homeDetailSlave)


    def createActions(self):
        self.exitAction = QtGui.QAction(QtGui.QIcon(settings.ICON_TOOLBAR_EXIT), '&Exit', self)
        self.exitAction.setShortcut('Super+Q')
        self.exitAction.setStatusTip('Quit Chizu')
        self.exitAction.triggered.connect(QtGui.qApp.quit)

        self.homeAction = QtGui.QAction(QtGui.QIcon(settings.ICON_TOOLBAR_HOME), '&Home', self)
        self.homeAction.setShortcut('Super+I')
        self.homeAction.setStatusTip('Index')
        self.homeAction.triggered.connect(self.setHomeDetailSlave)

        self.playersAction = QtGui.QAction(QtGui.QIcon(settings.ICON_TOOLBAR_PLAYERS), '&Players', self)
        self.playersAction.setShortcut('Super+Q')
        self.playersAction.setStatusTip('Players')
        self.playersAction.triggered.connect(self.setPlayerListSlave)

    def createMenus(self):
        # create toolbar
        toolbar = QtGui.QToolBar()
        toolbar.setFloatable(False)
        toolbar.setMovable(False)

        toolbar.addAction(self.homeAction)
        toolbar.addAction(self.playersAction)
        toolbar.addSeparator()
        toolbar.addAction(self.exitAction)

        self.addToolBar(Qt.LeftToolBarArea, toolbar)

        # create menubar

    def setHomeDetailSlave(self):
        self.central_widget.setCurrentWidget(self.homeDetailSlave)

    def setPlayerListSlave(self):
        self.central_widget.setCurrentWidget(self.playerListSlave)
