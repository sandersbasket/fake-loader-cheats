from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json

with open('config.json', 'r') as fp:
    cfg = json.loads(fp.read())




class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setWindowIcon(QtGui.QIcon('ico.ico'))
        Form.resize(400, 210)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 381, 191))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 361, 151))
        self.groupBox.setObjectName("groupBox")
        if cfg['injectsettings_1'] != "":
            self.checkBox = QtWidgets.QCheckBox(self.groupBox)
            self.checkBox.setGeometry(QtCore.QRect(10, 10, 101, 41))
            self.checkBox.setObjectName("checkBox")
        if cfg['injectsettings_2'] != "":
            self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
            self.checkBox_2.setGeometry(QtCore.QRect(10, 40, 91, 31))
            self.checkBox_2.setObjectName("checkBox_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(230, 10, 120, 80))
        self.groupBox_5.setObjectName("groupBox_5")
        self.keySequenceEdit = QtWidgets.QKeySequenceEdit(self.groupBox_5)
        self.keySequenceEdit.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.keySequenceEdit.setObjectName("keySequenceEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        if cfg['injectsettings_3'] != "":
            self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
            self.radioButton_3.setGeometry(QtCore.QRect(10, 70, 82, 17))
            self.radioButton_3.setObjectName("radioButton_3")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(220, 123, 141, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 120, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.pbar)
        self.pushButton_2.clicked.connect(self.save)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 9, 361, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        if cfg['functionsettings_1'] != "":
            self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
            self.checkBox_3.setGeometry(QtCore.QRect(10, 20, 81, 21))
            self.checkBox_3.setObjectName("checkBox_3")
        if cfg['functionsettings_2'] != "":
            self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
            self.checkBox_4.setGeometry(QtCore.QRect(10, 36, 70, 31))
            self.checkBox_4.setObjectName("checkBox_4")
        if cfg['functionsettings_3'] != "":
            self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
            self.checkBox_5.setGeometry(QtCore.QRect(10, 60, 71, 21))
            self.checkBox_5.setObjectName("checkBox_5")
        if cfg['functionsettings_4'] != "":
            self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_2)
            self.checkBox_6.setGeometry(QtCore.QRect(10, 80, 71, 21))
            self.checkBox_6.setObjectName("checkBox_6")
        if cfg['functionsettings_6'] != "":
            self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_2)
            self.checkBox_7.setGeometry(QtCore.QRect(260, 110, 70, 21))
            self.checkBox_7.setObjectName("checkBox_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(240, 10, 111, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_8.setGeometry(QtCore.QRect(9, 16, 81, 21))
        self.checkBox_8.setObjectName("checkBox_8")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(110, 10, 120, 80))
        self.groupBox_4.setObjectName("groupBox_4")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_4)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 50, 101, 21))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(0, 100)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setFocusPolicy(Qt.NoFocus)
        self.horizontalSlider.valueChanged.connect(self.sliders)
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(60, 40, 47, 13))
        self.label.setObjectName("label")
        if cfg['functionsettings_5'] != "":
            self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_2)
            self.checkBox_10.setGeometry(QtCore.QRect(130, 110, 91, 21))
            self.checkBox_10.setObjectName("checkBox_10")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 110, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(9, 9, 361, 151))
        self.groupBox_6.setObjectName("groupBox_6")
        if cfg['radarhacksettings_1'] != "":
            self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_6)
            self.checkBox_11.setGeometry(QtCore.QRect(10, 20, 70, 17))
            self.checkBox_11.setObjectName("checkBox_11")
        if cfg['radarhacksettings_2'] != "":
            self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox_6)
            self.checkBox_12.setGeometry(QtCore.QRect(10, 40, 70, 17))
            self.checkBox_12.setObjectName("checkBox_12")
        if cfg['radarhacksettings_3'] != "":
            self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox_6)
            self.checkBox_13.setGeometry(QtCore.QRect(10, 60, 70, 17))
            self.checkBox_13.setObjectName("checkBox_13")
        if cfg['radarhacksettings_4'] != "":
            self.checkBox_14 = QtWidgets.QCheckBox(self.groupBox_6)
            self.checkBox_14.setGeometry(QtCore.QRect(10, 80, 70, 17))
            self.checkBox_14.setObjectName("checkBox_14")
        if cfg['radarhacksettings_5'] != "":
            self.checkBox_15 = QtWidgets.QCheckBox(self.groupBox_6)
            self.checkBox_15.setGeometry(QtCore.QRect(110, 20, 81, 17))
            self.checkBox_15.setObjectName("checkBox_15")
        if cfg['radarhacksettings_6'] != "":
            self.checkBox_16 = QtWidgets.QCheckBox(self.groupBox_6)
            self.checkBox_16.setGeometry(QtCore.QRect(110, 40, 70, 17))
            self.checkBox_16.setObjectName("checkBox_16")
        if cfg['radarhacksettings_7'] != "":
            self.checkBox_17 = QtWidgets.QCheckBox(self.groupBox_6)
            self.checkBox_17.setGeometry(QtCore.QRect(110, 60, 81, 17))
            self.checkBox_17.setObjectName("checkBox_17")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_4.setGeometry(QtCore.QRect(254, 120, 91, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.save)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def sliders(self, value):
        self.label.setText(str(value))
    def save(self):
        QMessageBox.about(self, cfg['title'], cfg['MessageSave'])
    def pbar(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 1
            self.progressBar.setValue(self.completed)
        QMessageBox.about(self, cfg['title'], cfg['MessageInject'])

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", cfg['title']))
        self.tabWidget.setToolTip(_translate("Form", "<html><head/><body><p>Function</p><p><br/></p></body></html>"))
        self.tabWidget.setWhatsThis(_translate("Form", "<html><head/><body><p>not</p><p><br/></p></body></html>"))
        self.groupBox.setTitle(_translate("Form", cfg['GroupBox_1']))
        if cfg['injectsettings_1'] != "":
            self.checkBox.setText(_translate("Form", cfg['injectsettings_1']))
        if cfg['injectsettings_2'] != "":
            self.checkBox_2.setText(_translate("Form", cfg['injectsettings_2']))
        self.groupBox_5.setTitle(_translate("Form", "Open Menu "))
        self.label_2.setText(_translate("Form", "Set bind:"))
        if cfg['injectsettings_3'] != "":
            self.radioButton_3.setText(_translate("Form", cfg['injectsettings_3']))
        self.pushButton_2.setText(_translate("Form", "SAVE SETTINGS"))
        self.pushButton_3.setText(_translate("Form", "INJECT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", cfg['tabname_1']))
        self.groupBox_2.setTitle(_translate("Form", cfg['GroupBox_2']))
        if cfg['functionsettings_1'] != "":
            self.checkBox_3.setText(_translate("Form", cfg['functionsettings_1']))
        if cfg['functionsettings_2'] != "":
            self.checkBox_4.setText(_translate("Form", cfg['functionsettings_2']))
        if cfg['functionsettings_3'] != "":
            self.checkBox_5.setText(_translate("Form", cfg['functionsettings_3']))
        if cfg['functionsettings_4'] != "":
            self.checkBox_6.setText(_translate("Form", cfg['functionsettings_4']))
        if cfg['functionsettings_6'] != "":
            self.checkBox_7.setText(_translate("Form", cfg['functionsettings_6']))
        self.groupBox_3.setTitle(_translate("Form", cfg['GroupboxFunction_2']))
        self.checkBox_8.setText(_translate("Form", "Enable"))
        self.radioButton.setText(_translate("Form", "Object aim"))
        self.radioButton_2.setText(_translate("Form", "Mouse aim"))
        self.groupBox_4.setTitle(_translate("Form", cfg['GroupboxFunction_1']))
        self.checkBox_9.setText(_translate("Form", "Enable"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        if cfg['functionsettings_5'] != "":
            self.checkBox_10.setText(_translate("Form", cfg['functionsettings_5']))
        self.pushButton.setText(_translate("Form", "SAVE SETTINGS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", cfg['tabname_2']))
        self.groupBox_6.setTitle(_translate("Form", cfg['GroupBox_3']))
        if cfg['radarhacksettings_1'] != "":
            self.checkBox_11.setText(_translate("Form", cfg['radarhacksettings_1']))
        if cfg['radarhacksettings_2'] != "":
            self.checkBox_12.setText(_translate("Form", cfg['radarhacksettings_2']))
        if cfg['radarhacksettings_3'] != "":
            self.checkBox_13.setText(_translate("Form", cfg['radarhacksettings_3']))
        if cfg['radarhacksettings_4'] != "":
            self.checkBox_14.setText(_translate("Form", cfg['radarhacksettings_4']))
        if cfg['radarhacksettings_5'] != "":
            self.checkBox_15.setText(_translate("Form", cfg['radarhacksettings_5']))
        if cfg['radarhacksettings_6'] != "":
            self.checkBox_16.setText(_translate("Form", cfg['radarhacksettings_6']))
        if cfg['radarhacksettings_7'] != "":
            self.checkBox_17.setText(_translate("Form", cfg['radarhacksettings_7']))
        self.pushButton_4.setText(_translate("Form", "SAVE SETTINGS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", cfg['tabname_3']))

class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


# colors 
def colors():
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

app = QtWidgets.QApplication(sys.argv)
if cfg['style'] == 'Windows':
    app.setStyle("Windows")
    colors()
elif cfg['style'] == 'Fusion':
    app.setStyle("Fusion")
    colors()

    

window = MainWindow()
window.show()
app.exec() 