from PyQt4 import Qt, QtGui, QtCore
from PyQt4.QtCore import Qt

from chizu.lib import settings
from chizu.lib.base.gui import BaseSlave

from chizu.gui.dialogs.playerdialog import PlayerCreateDialog
from chizu.domain.player import Player


class PlayerListSlave(BaseSlave):

    def __init__(self, parent=None):
        super(PlayerListSlave, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        super(PlayerListSlave, self).setupUi()

        self.createPlayerButton = QtGui.QPushButton(u'New Player')
        self.createPlayerButton.clicked.connect(self.onCreatePlayerButtonClicked)

        self.layout.addWidget(PlayerTableView(self))
        self.layout.addWidget(self.createPlayerButton)

    def onCreatePlayerButtonClicked(self):
        self.playerCreateDialog = PlayerCreateDialog(self)



class PlayerTableView(QtGui.QTableView):

    def __init__(self, parent=None):
        super(PlayerTableView, self).__init__(parent)

        self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        data = PlayerTableModel()
        players = Player.fetchAll()

        if players:
            for p in players:
                data.addPlayer(p)

        self.setModel(data)


class PlayerTableModel(QtCore.QAbstractTableModel):

    def __init__(self):
        super(PlayerTableModel, self).__init__()

        self.headers = ['Name', 'Nickname']
        self.players = []

    def rowCount(self,index=QtCore.QModelIndex()):
        return len(self.players)

    def addPlayer(self, player):
        self.beginResetModel()
        self.players.append(player)
        self.endResetModel()

    def columnCount(self, index=QtCore.QModelIndex()):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        col = index.column()
        player = self.players[index.row()]
        if role == Qt.DisplayRole:
            if col == 0:
                return QtCore.QVariant(player.name)
            elif col == 1:
                return QtCore.QVariant(player.nickname)
            return QtCore.QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == Qt.Horizontal:
            return QtCore.QVariant(self.headers[section])
        return QtCore.QVariant(int(section + 1))
