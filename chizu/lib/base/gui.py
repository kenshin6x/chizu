from PyQt4 import Qt, QtGui, QtCore
from PyQt4.QtCore import Qt

from chizu.lib import settings

class BaseWindow(QtGui.QMainWindow):

    title = settings.APP_NAME_DISPLAY
    icon = settings.ICON_APP

    def __init__(self, parent=None):
        super(BaseWindow, self).__init__(parent);

    def setupUi(self):
        self.setGeometry(550, 600, 550, 600)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.centerWindow()

        # create the central
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class BaseSlave(QtGui.QWidget):

    def __init__(self, parent=None):
        super(BaseSlave, self).__init__(parent);

    def setupUi(self):
        pass
