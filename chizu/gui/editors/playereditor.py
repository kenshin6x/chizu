from PyQt4 import Qt, QtGui, QtCore
from PyQt4.QtCore import Qt

from chizu.lib import settings
from chizu.lib.base.gui import BaseEditor

class PlayerCreateEditor(BaseEditor):

    def __init__(self, parent=None):
        super(PlayerCreateEditor, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        super(PlayerCreateEditor, self).setupUi()

        self.nameLabel = QtGui.QLabel(u'Name')
        self.nicknameLabel = QtGui.QLabel(u'Nickname')

        self.nameEdit = QtGui.QLineEdit()
        self.nicknameEdit = QtGui.QLineEdit()

        self.submitButton = QtGui.QPushButton(u'Create')
        self.submitButton.clicked.connect(self.onSubmit)

        self.grid.addWidget(self.nameLabel, 1, 0)
        self.grid.addWidget(self.nameEdit, 1, 1)

        self.grid.addWidget(self.nicknameLabel, 2, 0)
        self.grid.addWidget(self.nicknameEdit, 2, 1)

        self.grid.addWidget(self.submitButton, 3, 0)

    def onSubmit(self):
        print "submit do add plauyer"