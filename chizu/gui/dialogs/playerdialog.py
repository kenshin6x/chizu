from PyQt4 import Qt, QtGui, QtCore
from PyQt4.QtCore import Qt

from chizu.lib import settings
from chizu.lib.base.gui import BaseDialog

from chizu.gui.editors.playereditor import PlayerCreateEditor


class PlayerCreateDialog(BaseDialog):

    title = u"Create Player"

    def __init__(self, parent=None):
        super(PlayerCreateDialog, self).__init__(parent)

        self.playerCreateEditor = PlayerCreateEditor(self)

        self.setupUi()

    def setupUi(self):
        super(PlayerCreateDialog, self).setupUi()
        self.layout.addWidget(self.playerCreateEditor)