import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, \
    QPushButton, QMessageBox


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'Moja aplikacja'
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 300)
        self.setGeometry(600, 300, 300, 300)
        self.setWindowTitle(self.name)

        buttonMsg = QPushButton('WIADOMOŚĆ', self)
        buttonMsg.setStyleSheet("background-color:#FFB6C1;")

        buttonMsg.resize(300, 300)
        buttonMsg.clicked.connect(self.showMsg)

        self.show()

    def showMsg(self):

       message = QMessageBox.question(self, 'Definitywnie', 'Czy na pewno chcesz wyświetlić wiadomość?', QMessageBox.Yes | QMessageBox.No | QMessageBox.No)

       if message == QMessageBox.Yes:
        self.close()
        print('Wiadomość odczytana')
       elif message == QMessageBox.No:
        print('Wiadomość nieodczytana')
       else:
        print('Error')


app = QApplication(sys.argv)
ex = MyWindow()
sys.exit(app.exec_())
