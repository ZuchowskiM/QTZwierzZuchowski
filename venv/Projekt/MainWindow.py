# Autors: Michał Żuchowski, Lidia Zwierz
# Created using: PyQt5 UI code generator 5.15.1
# Simple photo editing app, created using QT and Pillow libraries.

import EditorEngine as EE
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider, QLabel, QMessageBox, QVBoxLayout
from PIL.ImageQt import ImageQt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Main Window section
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(900, 650)
        MainWindow.setWindowIcon(QtGui.QIcon("Icons/logo.png"))
        MainWindow.setStyleSheet("background-color: rgb(255, 239, 213)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Horizontal menu
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 791, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.menuHLay = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.menuHLay.setContentsMargins(0, 0, 0, 0)
        self.menuHLay.setObjectName("menuHLay")

        #Resize button
        self.resizeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resizeButton.sizePolicy().hasHeightForWidth())
        self.resizeButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.resizeButton.setFont(font)
        self.resizeButton.setStyleSheet("background-color: rgb(144, 238, 144)")
        self.resizeButton.setObjectName("resizeButton")
        self.menuHLay.addWidget(self.resizeButton)

        # Text button
        self.textButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textButton.sizePolicy().hasHeightForWidth())
        self.textButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textButton.setFont(font)
        self.textButton.setStyleSheet("background-color: rgb(255, 176, 119);")
        self.textButton.setObjectName("textButton")
        self.menuHLay.addWidget(self.textButton)

        # Saturation button
        self.saturatioButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saturatioButton.sizePolicy().hasHeightForWidth())
        self.saturatioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.saturatioButton.setFont(font)
        self.saturatioButton.setStyleSheet("background-color: rgb(255, 192, 203)")
        self.saturatioButton.setObjectName("saturatioButton")
        self.menuHLay.addWidget(self.saturatioButton)

        # Saturation slider
        self.sliderSat = QSlider(Qt.Horizontal, self.centralwidget)
        self.sliderSat.setGeometry(QtCore.QRect(160, 580, 450, 50))
        self.sliderSat.setTickPosition(QSlider.NoTicks)
        self.sliderSat.setValue(1)
        self.sliderSat.setRange(-20, 20)
        self.sliderSat.valueChanged.connect(self.Saturation)
        self.sliderSat.setObjectName("sliderSaturation")
        self.sliderSat.hide()

        # Contrast button
        self.contrasButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contrasButton.sizePolicy().hasHeightForWidth())
        self.contrasButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.contrasButton.setFont(font)
        self.contrasButton.setStyleSheet("background-color: rgb(204, 255, 255);")
        self.contrasButton.setObjectName("contrasButton")
        self.menuHLay.addWidget(self.contrasButton)

        # Contrast slider
        self.sliderCon = QSlider(Qt.Horizontal, self.centralwidget)
        self.sliderCon.setGeometry(QtCore.QRect(160, 580, 450, 50))
        self.sliderCon.setTickPosition(QSlider.NoTicks)
        self.sliderCon.setValue(1)
        self.sliderCon.setRange(-20, 20)
        self.sliderCon.valueChanged.connect(self.Contrast)
        self.sliderCon.setObjectName("sliderContrast")
        self.sliderCon.hide()

        # Brightness button
        self.brigthnessButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brigthnessButton.sizePolicy().hasHeightForWidth())
        self.brigthnessButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.brigthnessButton.setFont(font)
        self.brigthnessButton.setStyleSheet("background-color: rgb(188, 143, 143);")
        self.brigthnessButton.setObjectName("brigthnessButton")
        self.menuHLay.addWidget(self.brigthnessButton)

        # Brigtness slider
        self.sliderBri = QSlider(Qt.Horizontal, self.centralwidget)
        self.sliderBri.setGeometry(QtCore.QRect(160, 580, 450, 50))
        self.sliderBri.setTickPosition(QSlider.NoTicks)
        self.sliderBri.setRange(0, 20)
        self.sliderBri.setValue(10)
        self.sliderBri.valueChanged.connect(self.Brightness)
        self.sliderBri.setObjectName("sliderBrigthness")
        self.sliderBri.hide()

        # Filters button
        self.filtersButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filtersButton.sizePolicy().hasHeightForWidth())
        self.filtersButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.filtersButton.setFont(font)
        self.filtersButton.setStyleSheet("background-color: rgb(204, 204, 255);")
        self.filtersButton.setObjectName("filtersButton")
        self.menuHLay.addWidget(self.filtersButton)

        # Main graphics(photo) view
        self.mainGraphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.mainGraphicsView.setGeometry(QtCore.QRect(40, 80, 681, 481))
        self.mainGraphicsView.setObjectName("mainGraphicsView")
        self.mainGraphicsView.hide()

        # Select photo button
        self.selectPhotoButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectPhotoButton.setText('Choose Photo')
        font = QtGui.QFont()
        font.setWeight(QFont.Bold)
        self.selectPhotoButton.setFont(QFont('Helvetica [Cronyx]', 14))
        self.selectPhotoButton.setGeometry(QtCore.QRect(200, 120, 350, 440))
        self.selectPhotoButton.setStyleSheet("background-color: rgb(220, 220, 220); border-radius : 50; border : 2px solid black")
        self.selectPhotoButton.setObjectName("selectPhotoButton")

        # Buttons Clear and Save(vertical layout)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(730, 459, 111, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Clear button
        self.clearButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("background-color: rgb(255, 0, 0);border-radius : 20")
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout.addWidget(self.clearButton)

        # Save button
        self.saveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("background-color: rgb(0, 170, 255);border-radius : 20")
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)

        # Roll button
        self.rollButton = QtWidgets.QPushButton(self.centralwidget)
        self.rollButton.setGeometry(QtCore.QRect(740, 80, 91, 61))
        font = QtGui.QFont()
        font.setWeight(QFont.Bold)
        self.rollButton.setFont(QFont('Helvetica [Cronyx]', 10))
        font.setFamily("Liberation Sans")
        self.rollButton.setObjectName("rollButton")
        self.rollButton.setGeometry(732, 90, 100, 100)
        self.rollButton.setIcon(QIcon('Icons/rotate.png'))
        self.rollButton.setIconSize(QtCore.QSize(33, 33))
        self.rollButton.setStyleSheet("background-color: rgb(255,255,153); border-radius : 50; border : 2px solid black")
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu and status bars
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # Button connects
        self.selectPhotoButton.clicked.connect(self.selectPhoto)
        self.resizeButton.clicked.connect(self.openResizeWindow)
        self.textButton.clicked.connect(self.openTextWindow)
        self.rollButton.clicked.connect(self.rotatePhoto)
        self.filtersButton.clicked.connect(self.openFiltersWindow)
        self.saveButton.clicked.connect(self.saveImage)
        self.clearButton.clicked.connect(self.clearPhoto)
        self.saturatioButton.clicked.connect(self.saturationSlider)
        self.contrasButton.clicked.connect(self.contrastSlider)
        self.brigthnessButton.clicked.connect(self.brightnessSlider)

        # Button locking
        self.unlockButtons(False)

        # Creating editor engine object
        self.editor = EE.EditorEngine()

        # Filters List
        self.filters = ['Blur', 'Contour', 'Detail', 'Emboss', 'Sharpen']

        #Qdialog widgets
        self.editHeight = QtWidgets.QLineEdit('Height')
        self.editWidth = QtWidgets.QLineEdit('Width')
        self.filterList = QtWidgets.QListWidget()
        self.textEdit = QtWidgets.QLineEdit()
        self.editFontSize = QtWidgets.QLineEdit()
        self.checkFontColor = QtWidgets.QCheckBox()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Editor"))
        self.resizeButton.setText(_translate("MainWindow", "Resize"))
        self.textButton.setText(_translate("MainWindow", "Text"))
        self.saturatioButton.setText(_translate("MainWindow", "Saturation"))
        self.contrasButton.setText(_translate("MainWindow", "Contrast"))
        self.brigthnessButton.setText(_translate("MainWindow", "Brightness"))
        self.filtersButton.setText(_translate("MainWindow", "Filters"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.rollButton.setText(_translate("MainWindow", ""))



    def selectPhoto(self):
        file = QtWidgets.QFileDialog()
        self.editor.imagePath = file.getOpenFileName(filter="JPG (*.jpg)")[0]
        try:
            self.editor.readImage()

            image_profile = ImageQt(self.editor.image)
            image_profile = image_profile.scaled(400, 400, aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                            transformMode=QtCore.Qt.SmoothTransformation)
            scene = QtWidgets.QGraphicsScene()
            scene.addPixmap(QtGui.QPixmap.fromImage(image_profile))

            self.mainGraphicsView.setScene(scene)
            self.selectPhotoButton.hide()
            self.mainGraphicsView.show()
            self.unlockButtons(True)
        except Exception as e:
            print(e)


    def unlockButtons(self, unlock):
        self.resizeButton.setEnabled(bool(unlock))
        self.textButton.setEnabled(bool(unlock))
        self.saturatioButton.setEnabled(bool(unlock))
        self.contrasButton.setEnabled(bool(unlock))
        self.brigthnessButton.setEnabled(bool(unlock))
        self.filtersButton.setEnabled(bool(unlock))
        self.rollButton.setEnabled(bool(unlock))
        self.clearButton.setEnabled(bool(unlock))
        self.saveButton.setEnabled(bool(unlock))

    def updatePhoto(self):
        image_profile = ImageQt(self.editor.image)
        image_profile = image_profile.scaled(400, 400, aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                             transformMode=QtCore.Qt.SmoothTransformation)
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap.fromImage(image_profile))

        self.mainGraphicsView.setScene(scene)

    def saveImage(self):
        try:
            file = QtWidgets.QFileDialog()
            savePath = file.getSaveFileName(filter="JPG (*.jpg)")[0]
            self.editor.saveImage(savePath)
        except Exception as e:
            print(e)

    def hideSliders(self):
        self.sliderCon.hide()
        self.sliderSat.hide()
        self.sliderBri.hide()


    def clearPhoto(self):
        self.sliderSat.setValue(1)
        self.sliderBri.setValue(10)
        self.sliderCon.setValue(1)
        self.editor.image = self.editor.baseImage
        self.updatePhoto()


    def rotatePhoto(self):
        self.hideSliders()
        self.editor.rotateImage(90)
        self.updatePhoto()


    def openResizeWindow(self):
        self.hideSliders()
        dialog = QtWidgets.QDialog()
        dialog.setWindowFlags(Qt.WindowCloseButtonHint)
        dialog.setWindowIcon(QtGui.QIcon("Icons/resize.png"))
        dialog.setFixedSize(300, 200)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(10)
        dialog.setFont(font)
        layout = QtWidgets.QVBoxLayout()
        buttonApply = QtWidgets.QPushButton('Apply')
        buttonApply.setFont(font)
        buttonApply.clicked.connect(self.resizePhoto)
        buttonApply.clicked.connect(dialog.close)
        buttonApply.setStyleSheet("background-color: rgb(255,255,255)")
        width, height = self.editor.image.size
        self.editHeight = QtWidgets.QLineEdit(str(height))
        self.editWidth = QtWidgets.QLineEdit(str(width))
        labelHeight = QLabel('Height:')
        labelWidth = QLabel('Width:')
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(labelHeight)
        layout.addWidget(self.editHeight)
        layout.addWidget(labelWidth)
        layout.addWidget(self.editWidth)
        layout.addWidget(buttonApply)
        dialog.setModal(False)
        dialog.setLayout(layout)
        dialog.setWindowTitle('Resize')
        dialog.setStyleSheet("background-color: rgb(218, 247, 166 )")
        dialog.exec()
        dialog.show()


    def resizePhoto(self):
         newHeight = self.editHeight.text()
         newWidth = self.editWidth.text()
         try:
            newSize = (int(newWidth), int(newHeight))
            self.editor.resizeImage(newSize)
            self.updatePhoto()
         except Exception:
             self.Error()

    def Error(self):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle('Error')
        error.setWindowIcon(QtGui.QIcon("Icons/error.png"))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(10)
        error.setText('Wrong\n  type!')
        error.setFont(font)
        error.setStandardButtons(QtWidgets.QMessageBox.Ok)
        error.exec()
        self.openResizeWindow()

    def openTextWindow(self):
        self.hideSliders()
        dialog = QtWidgets.QDialog()
        dialog.setWindowIcon(QtGui.QIcon("Icons/font.png"))
        dialog.setWindowFlags(Qt.WindowCloseButtonHint)
        dialog.setFixedSize(300, 200)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(10)
        dialog.setFont(font)
        layout = QtWidgets.QVBoxLayout()
        buttonApply = QtWidgets.QPushButton('Apply')
        buttonApply.setFont(font)
        buttonApply.clicked.connect(self.placeText)
        buttonApply.clicked.connect(dialog.close)
        buttonApply.setStyleSheet("background-color: rgb(255,255,255)")
        self.textEdit = QtWidgets.QLineEdit()
        self.textEdit.setPlaceholderText('Text')
        self.editFontSize = QtWidgets.QLineEdit()
        self.editFontSize.setPlaceholderText('Font size, for ex."5"')
        self.checkFontColor = QtWidgets.QCheckBox()
        self.checkFontColor.setText('White Color?')
        layout.addWidget(self.textEdit)
        layout.addWidget(self.editFontSize)
        layout.addWidget(self.checkFontColor)
        layout.addWidget(buttonApply)
        dialog.setModal(False)
        dialog.setLayout(layout)
        dialog.setWindowTitle('Text')
        dialog.setStyleSheet("background-color: rgb(237, 187, 153 )")
        dialog.exec()
        dialog.show()


    def placeText(self):
        try:
            if self.checkFontColor.isChecked() is True:
                color = 'white'
            else:
                color = 'black'

            if self.editFontSize.text() == '':
                self.editor.placeText(self.textEdit.text(), color)
            else:
                sizeFont = int(self.editFontSize.text())
                self.editor.placeText(self.textEdit.text(),color,sizeFont)

            self.updatePhoto()
        except Exception as e:
            print(e)


    def openFiltersWindow(self):
        self.hideSliders()
        dialog = QtWidgets.QDialog()
        dialog.setWindowIcon(QtGui.QIcon("Icons/filters.png"))
        dialog.setWindowFlags(Qt.WindowCloseButtonHint)
        dialog.setFixedSize(300, 200)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(10)
        dialog.setFont(font)
        layout = QtWidgets.QVBoxLayout()
        self.filterList = QtWidgets.QListWidget()
        font.setPointSize(12)
        self.filterList.setFont(font)
        buttonApply = QtWidgets.QPushButton("Apply")
        buttonApply.setFont(font)
        buttonApply.setStyleSheet("background-color: rgb(255,255,255)")
        buttonApply.clicked.connect(self.putFilter)
        buttonApply.clicked.connect(dialog.close)
        self.filterList.addItems(self.filters)
        self.filterList.setCurrentItem(self.filterList.item(0))
        layout.addWidget(self.filterList)
        layout.addWidget(buttonApply)
        dialog.setModal(False)
        dialog.setLayout(layout)
        dialog.setWindowTitle('Filters')
        dialog.setStyleSheet("background-color: rgb(230, 230, 250)")
        dialog.exec()
        dialog.show()


    def putFilter(self):
        item = self.filterList.currentItem().text()
        # DEBUG
        # print(item)

        if item == 'Blur':
            self.editor.filterBlur()

        if item == 'Contour':
            self.editor.filterContour()

        if item == 'Detail':
            self.editor.filterDetail()

        if item == 'Emboss':
            self.editor.filterEmboss()

        if item == 'Sharpen':
            self.editor.filterSharpen()

        self.updatePhoto()

    def Saturation(self):
        size = float(self.sliderSat.value()) / 10 + 1
        self.editor.changeSaturation(size)
        self.updatePhoto()

    def Contrast(self):
        size = float(self.sliderCon.value()) / 10 + 1
        self.editor.changeContrast(size)
        self.updatePhoto()

    def Brightness(self):
        size = float(self.sliderBri.value()) / 10
        self.editor.changeBrightness(size)
        self.updatePhoto()

    def saturationSlider(self):
        self.sliderCon.hide()
        self.sliderBri.hide()
        self.editor.saveTempImage()
        self.sliderSat.setValue(1)
        self.sliderSat.show()


    def contrastSlider(self):
        self.sliderSat.hide()
        self.sliderBri.hide()
        self.editor.saveTempImage()
        self.sliderCon.setValue(1)
        self.sliderCon.show()

    def brightnessSlider(self):
        self.sliderSat.hide()
        self.sliderCon.hide()
        self.editor.saveTempImage()
        self.sliderBri.setValue(10)
        self.sliderBri.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
