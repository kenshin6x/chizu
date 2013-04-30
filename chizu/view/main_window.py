from PyQt4 import Qt, QtGui, QtCore
from PyQt4.QtCore import Qt

from chizu import settings
from chizu.view.home_widget import HomeWidget
from chizu.view.player_widget import PlayersWidget


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.homeWidget = HomeWidget(self)
        self.playersWidget = PlayersWidget(self)

        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 600, 400)
        self.setWindowTitle(settings.APP_NAME_DISPLAY)
        self.setWindowIcon(QtGui.QIcon(settings.ICON_APP))
        self.centerWindow()

        self.createActions()
        self.createMenus()

        # create the central
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # define all avaliabre widgets to main window
        self.central_widget.addWidget(self.homeWidget)
        self.central_widget.addWidget(self.playersWidget)

        # the initial widget to display
        self.central_widget.setCurrentWidget(self.homeWidget)

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def createActions(self):
        self.exitAction = QtGui.QAction(QtGui.QIcon(settings.ICON_TOOLBAR_EXIT), '&Exit', self)
        self.exitAction.setShortcut('Super+Q')
        self.exitAction.setStatusTip('Quit Chizu')
        self.exitAction.triggered.connect(QtGui.qApp.quit)

        self.homeAction = QtGui.QAction(QtGui.QIcon(settings.ICON_TOOLBAR_HOME), '&Home', self)
        self.homeAction.setShortcut('Super+I')
        self.homeAction.setStatusTip('Index')
        self.homeAction.triggered.connect(self.setHomeWidget)

        self.playersAction = QtGui.QAction(QtGui.QIcon(settings.ICON_TOOLBAR_PLAYERS), '&Players', self)
        self.playersAction.setShortcut('Super+Q')
        self.playersAction.setStatusTip('Players')
        self.playersAction.triggered.connect(self.setPlayersWidget)

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

    def setHomeWidget(self):
        self.central_widget.setCurrentWidget(self.homeWidget)

    def setPlayersWidget(self):
        self.central_widget.setCurrentWidget(self.playersWidget)
