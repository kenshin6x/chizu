from PyQt4 import QtGui, QtCore
from chizu import settings

from chizu.view.main_widgets import *


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        # base properties
        self.setGeometry(600, 400, 600, 400)
        self.setWindowTitle(settings.APP_NAME_DISPLAY)
        self.setWindowIcon(QtGui.QIcon(settings.ICON_APP))
        self.center()

        # create statusbar
        self.statusBar().showMessage(u'Ready')

        # create menubar and toolbar
        self.menubar()
        self.toolbar()

        # create init widget
        self.setCentralWidget(HomeWidget())

        # display window
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def closeEvent(self, event):
    #         reply = QtGui.QMessageBox.question(self,
    #             u'Quit',
    #             u"You really want to quit?",
    #             QtGui.QMessageBox.Yes,
    #             QtGui.QMessageBox.No
    #         )
    #
    #         if reply == QtGui.QMessageBox.Yes:
    #             event.accept()
    #         else:
    #             event.ignore()

    def toolbar(self):
        # create toolbar actions
        exitAction = QtGui.QAction(QtGui.QIcon(
            settings.ICON_TOOLBAR_EXIT), '&Exit', self)
        exitAction.setShortcut('Super+Q')
        exitAction.setStatusTip('Quit Chizu')
        exitAction.triggered.connect(QtGui.qApp.quit)

        homeAction = QtGui.QAction(QtGui.QIcon(
            settings.ICON_TOOLBAR_HOME), '&Home', self)
        homeAction.setShortcut('Super+I')
        homeAction.setStatusTip('Index')
        homeAction.triggered.connect(self.setHomeWidget)

        playersAction = QtGui.QAction(QtGui.QIcon(
            settings.ICON_TOOLBAR_PLAYERS), '&Players', self)
        playersAction.setShortcut('Super+Q')
        playersAction.setStatusTip('Players')
        playersAction.triggered.connect(self.setPlayersWidget)

        # create toolbar and define actions
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.setFloatable(False)

        self.toolbar.addAction(homeAction)
        self.toolbar.addAction(playersAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(exitAction)

    def menubar(self):
        pass

    def setHomeWidget(self):
        self.setCentralWidget(HomeWidget())

    def setPlayersWidget(self):
        self.setCentralWidget(PlayersWidget())
