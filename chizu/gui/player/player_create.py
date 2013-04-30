class CreatePlayer(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(CreatePlayer, self).__init__(parent)

        self.playerController = PlayerController()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle(u"New Player")

        self.nameLabel = QtGui.QLabel('Name')
        self.nicknameLabel = QtGui.QLabel('Nickname')

        self.nameEdit = QtGui.QLineEdit()
        self.nicknameEdit = QtGui.QLineEdit()

        self.submitButton = QtGui.QPushButton(u'Save')
        self.submitButton.clicked.connect(self.submit)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.nameLabel, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)

        grid.addWidget(self.nameEdit, 2, 0)
        grid.addWidget(self.nicknameEdit, 2, 1)

        grid.addWidget(self.submitButton, 3, 0)

        self.setLayout(grid)
        self.show()

    def submit(self):
        self.playerController.save(self.nameEdit, self.nicknameEdit)
        self.hide()
