# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1471, 1104)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1471, 1105))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("Downloads/boutons actions.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Button_attack = QtWidgets.QPushButton(Form)
        self.Button_attack.setEnabled(True)
        self.Button_attack.setGeometry(QtCore.QRect(160, 290, 501, 211))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.Button_attack.setFont(font)
        self.Button_attack.setMouseTracking(False)
        self.Button_attack.setTabletTracking(False)
        self.Button_attack.setAcceptDrops(False)
        self.Button_attack.setAutoFillBackground(False)
        self.Button_attack.setCheckable(False)
        self.Button_attack.setAutoRepeat(False)
        self.Button_attack.setAutoExclusive(False)
        self.Button_attack.setAutoDefault(False)
        self.Button_attack.setDefault(False)
        self.Button_attack.setObjectName("Button_attack")
        self.Button_attack.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.Button_attack_spe = QtWidgets.QPushButton(Form)
        self.Button_attack_spe.setEnabled(True)
        self.Button_attack_spe.setGeometry(QtCore.QRect(820, 290, 501, 211))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.Button_attack_spe.setFont(font)
        self.Button_attack_spe.setMouseTracking(False)
        self.Button_attack_spe.setTabletTracking(False)
        self.Button_attack_spe.setAcceptDrops(False)
        self.Button_attack_spe.setAutoFillBackground(False)
        self.Button_attack_spe.setCheckable(False)
        self.Button_attack_spe.setAutoRepeat(False)
        self.Button_attack_spe.setAutoExclusive(False)
        self.Button_attack_spe.setAutoDefault(False)
        self.Button_attack_spe.setDefault(False)
        self.Button_attack_spe.setObjectName("Button_attack_spe")
        self.Button_attack_spe.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.Button_flee = QtWidgets.QPushButton(Form)
        self.Button_flee.setEnabled(True)
        self.Button_flee.setGeometry(QtCore.QRect(160, 650, 501, 211))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.Button_flee.setFont(font)
        self.Button_flee.setMouseTracking(False)
        self.Button_flee.setTabletTracking(False)
        self.Button_flee.setAcceptDrops(False)
        self.Button_flee.setAutoFillBackground(False)
        self.Button_flee.setCheckable(False)
        self.Button_flee.setAutoRepeat(False)
        self.Button_flee.setAutoExclusive(False)
        self.Button_flee.setAutoDefault(False)
        self.Button_flee.setDefault(False)
        self.Button_flee.setObjectName("Button_flee")
        self.Button_flee.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.Button_Pokemon = QtWidgets.QPushButton(Form)
        self.Button_Pokemon.setEnabled(True)
        self.Button_Pokemon.setGeometry(QtCore.QRect(820, 650, 501, 211))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.Button_Pokemon.setFont(font)
        self.Button_Pokemon.setMouseTracking(False)
        self.Button_Pokemon.setTabletTracking(False)
        self.Button_Pokemon.setAcceptDrops(False)
        self.Button_Pokemon.setAutoFillBackground(False)
        self.Button_Pokemon.setCheckable(False)
        self.Button_Pokemon.setAutoRepeat(False)
        self.Button_Pokemon.setAutoExclusive(False)
        self.Button_Pokemon.setAutoDefault(False)
        self.Button_Pokemon.setDefault(False)
        self.Button_Pokemon.setObjectName("Button_Pokemon")
        self.Button_Pokemon.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Button_attack.setText(_translate("Form", "Attack"))
        self.Button_attack_spe.setText(_translate("Form", "Special Attack"))
        self.Button_flee.setText(_translate("Form", "Flee"))
        self.Button_Pokemon.setText(_translate("Form", "Pokemon"))
