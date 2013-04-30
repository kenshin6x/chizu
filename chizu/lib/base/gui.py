from PyQt4 import Qt, QtGui, QtCore
from PyQt4.QtCore import Qt

from chizu.lib import settings


class BaseWindow(QtGui.QMainWindow):

    title = settings.APP_NAME_DISPLAY
    icon = settings.ICON_APP
    dimensions = None

    def __init__(self, parent=None):
        super(BaseWindow, self).__init__(parent)

    def setupUi(self):
        self.setGeometry(*self.dimensions)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.centerWindow()
        self.createActions()
        self.createMenus()

        # create the central
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def createActions(self):
        pass

    def createMenus(self):
        pass


class BaseSlave(QtGui.QWidget):

    def __init__(self, parent=None):
        super(BaseSlave, self).__init__(parent)

    def setupUi(self):
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.show()


class BaseDialog(QtGui.QDialog):

    title = None
    icon = settings.ICON_APP
    dimensions = [300, 300, 300, 300]

    def __init__(self, parent=None):
        super(BaseDialog, self).__init__(parent)

    def setupUi(self):
        self.setGeometry(*self.dimensions)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.show()

class BaseEditor(QtGui.QWidget):

    grid_spacing = 0

    def __init__(self, parent=None):
        super(BaseEditor, self).__init__(parent)

    def setupUi(self):
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(self.grid_spacing)

        self.setLayout(self.grid)
        self.show()
