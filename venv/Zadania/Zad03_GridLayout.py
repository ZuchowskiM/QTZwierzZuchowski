import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel,QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.name = "Moja aplikacja"
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 800)
        self.setGeometry(0, 0, 800, 800)

        gridLayout = QGridLayout(self)
        gridLayout.setSpacing(0)
        x = 1
        for i in range(3):
            for j in range(3):
                btn = QPushButton(f'{x}', self)
                x = x+1
                btn.setFixedSize(100,100)
                gridLayout.addWidget(btn, i, j)

        self.setLayout(gridLayout)
        self.show()



app = QApplication(sys.argv)
ex = MyWindow()
sys.exit(app.exec_())