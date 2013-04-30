from PyQt4 import Qt, QtGui, QtCore
from PyQt4.QtCore import Qt

from chizu import settings
from chizu.controller import PlayerController


class PlayersWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(PlayersWidget, self).__init__(parent)

        self.initUI()

    def initUI(self):
        boxLayout = QtGui.QVBoxLayout()
        boxLayout.addWidget(PlayersTableView(self))
        self.setLayout(boxLayout)


class PlayersTableView(QtGui.QTableView):

    def __init__(self, parent=None):
        super(PlayersTableView, self).__init__(parent)

        self.playerController = PlayerController()
        self.initUI()

    def initUI(self):
        # maximize table headers to layout
        self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        # set table model & data
        data = PlayersTableModel()


        save = self.playerController.save("Junior Andrade", "kenshin6x")

        players = self.playerController.getAll()

        print players

        if players:
            for p in players:
                data.addPlayer(p)

        self.setModel(data)


class PlayersTableModel(QtCore.QAbstractTableModel):

    def __init__(self):
        super(PlayersTableModel, self).__init__()

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
