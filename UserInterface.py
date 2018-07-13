
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QWidget, QPushButton, QMessageBox, QAction, QInputDialog, QLineEdit, QTabWidget, QFormLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from OntologyQueryFunctions import TypePrinting, WishedPollutants, GetMyWantedPollutantOnly, EffectPrinting, DomainPrinting
import sys
import numpy as np

class App(QMainWindow):


    def pollutant_get_method(self):
        print('method called !!')

        self.getChoicePollutant()
        self.getChoiceType()

        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to save?",
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        if buttonReply == QMessageBox.No:
            print('No clicked.')
        if buttonReply == QMessageBox.Cancel:
            print('Cancel')





    def getChoicePollutant(self):

        items = WishedPollutants
        item, okPressed = QInputDialog.getItem(self, "Get item", "Color:", items, 0, False)
        if okPressed and item:
            print(item)

    def getChoiceType(self):
        items = []
        for element in range (0,len(TypePrinting)):
            items.append(TypePrinting[element][0])

        items.append('None')
        item, okPressed = QInputDialog.getItem(self, "Get type", "Color:", items, 0, False)
        if okPressed and item:
            print(item)
            self.leType.setText(item)
        else:
            self.leType.setText('None')

    def getChoiceDomain(self):
        items = []
        for element in range (0,len(DomainPrinting)):
            items.append(DomainPrinting[element][0])

        items.append('None')
        item, okPressed = QInputDialog.getItem(self, "Get domain", "Color:", items, 0, False)
        if okPressed and item:
            print(item)
            self.leDomain.setText(item)
        else:
            self.leDomain.setText('None')

    def getChoiceEffect(self):
        items = []
        for element in range (0,len(EffectPrinting)):
            items.append(EffectPrinting[element][0])

        items.append('None')
        item, okPressed = QInputDialog.getItem(self, "Get domain", "Color:", items, 0, False)
        if okPressed and item:
            print(item)
            self.leEffect.setText(item)
        else:
            self.leEffect.setText('None')

    def getWantedPollutant(self):
        print(self.leType.text())
        print(self.leDomain.text())
        print(self.leEffect.text())

        if str(self.leType.text()) == 'None' or str(self.leType.text()) == '':
            a = None
        else:
            a = str(self.leType.text())

        if str(self.leDomain.text()) == 'None' or str(self.leDomain.text()) == '':
            b = None
        else:
            b = str(self.leDomain.text())

        if str(self.leEffect.text()) == 'None' or str(self.leEffect.text()) == '':
            c = None
        else:
            c = str(self.leEffect.text())


        PollutantList = GetMyWantedPollutantOnly(a,b,c)
        print(PollutantList)
        items = PollutantList
        item, okPressed = QInputDialog.getItem(self, "Pollutants", "Color:", items, 0, False)
        if okPressed and item:
            print(item)
            self.leWantedPollutant.setText(item)
        else:
            self.leWantedPollutant.setText('No Found')

    def __init__(self):
        super().__init__()
        self.title = 'User Interface'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')

        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)


        btn1 = QPushButton("Type!",self)
        btn1.clicked.connect(self.getChoiceType)
        self.leType = QLineEdit(self)

        btn2 = QPushButton("Domain!",self)
        btn2.clicked.connect(self.getChoiceDomain)
        self.leDomain = QLineEdit(self)

        btn3 = QPushButton("Effect!",self)
        btn3.clicked.connect(self.getChoiceEffect)
        self.leEffect = QLineEdit(self)

        btn4 = QPushButton("Find ", self)
        btn4.clicked.connect(self.getWantedPollutant)
        self.leWantedPollutant = QLineEdit(self)


        btn1.move(10,80)
        btn2.move(10,110)
        btn3.move(10,140)
        btn4.move(150,170)

        self.leType.move(150,80)
        self.leType.resize(280,20)

        self.leDomain.move(150, 110)
        self.leDomain.resize(280, 20)

        self.leEffect.move(150, 140)
        self.leEffect.resize(280, 20)

        self.leWantedPollutant.move(150,240)
        self.leWantedPollutant.resize(280,20)


        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Not now')








if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())