# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:53:20 2024

@author: anais
"""

#Import des Pokemons
from pokemons import liste_pokemon

pokedex = []

for i in range(151):
    pokedex.append(liste_pokemon[i].nom)
    
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(840, 781)
        self.p1 = QtWidgets.QLabel(Dialog)
        self.p1.setGeometry(QtCore.QRect(10, 0, 91, 101))
        self.p1.setText("")
        self.p1.setTextFormat(QtCore.Qt.RichText)
        self.p1.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Bulbasaur_F.png"))
        self.p1.setObjectName("p1")
        self.p2 = QtWidgets.QLabel(Dialog)
        self.p2.setGeometry(QtCore.QRect(100, 0, 91, 101))
        self.p2.setText("")
        self.p2.setTextFormat(QtCore.Qt.RichText)
        self.p2.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Ivysaur_F.png"))
        self.p2.setObjectName("p2")
        self.p3 = QtWidgets.QLabel(Dialog)
        self.p3.setGeometry(QtCore.QRect(190, 0, 91, 101))
        self.p3.setText("")
        self.p3.setTextFormat(QtCore.Qt.RichText)
        self.p3.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Venusaur_F.png"))
        self.p3.setObjectName("p3")
        self.p4 = QtWidgets.QLabel(Dialog)
        self.p4.setGeometry(QtCore.QRect(280, 0, 91, 101))
        self.p4.setText("")
        self.p4.setTextFormat(QtCore.Qt.RichText)
        self.p4.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Charmander_F.png"))
        self.p4.setObjectName("p4")
        self.p5 = QtWidgets.QLabel(Dialog)
        self.p5.setGeometry(QtCore.QRect(370, 0, 91, 101))
        self.p5.setText("")
        self.p5.setTextFormat(QtCore.Qt.RichText)
        self.p5.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Charmeleon_F.png"))
        self.p5.setObjectName("p5")
        self.p6 = QtWidgets.QLabel(Dialog)
        self.p6.setGeometry(QtCore.QRect(460, 0, 91, 101))
        self.p6.setText("")
        self.p6.setTextFormat(QtCore.Qt.RichText)
        self.p6.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Charizard_F.png"))
        self.p6.setObjectName("p6")
        self.p7 = QtWidgets.QLabel(Dialog)
        self.p7.setGeometry(QtCore.QRect(550, 0, 91, 101))
        self.p7.setText("")
        self.p7.setTextFormat(QtCore.Qt.RichText)
        self.p7.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Squirtle_F.png"))
        self.p7.setObjectName("p7")
        self.p8 = QtWidgets.QLabel(Dialog)
        self.p8.setGeometry(QtCore.QRect(640, 0, 91, 101))
        self.p8.setText("")
        self.p8.setTextFormat(QtCore.Qt.RichText)
        self.p8.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Wartortle_F.png"))
        self.p8.setObjectName("p8")
        self.p9 = QtWidgets.QLabel(Dialog)
        self.p9.setGeometry(QtCore.QRect(730, 0, 91, 101))
        self.p9.setText("")
        self.p9.setTextFormat(QtCore.Qt.RichText)
        self.p9.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Blastoise_F.png"))
        self.p9.setObjectName("p9")
        self.p10 = QtWidgets.QLabel(Dialog)
        self.p10.setGeometry(QtCore.QRect(10, 100, 91, 101))
        self.p10.setText("")
        self.p10.setTextFormat(QtCore.Qt.RichText)
        self.p10.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Caterpie_F.png"))
        self.p10.setObjectName("p10")
        self.p11 = QtWidgets.QLabel(Dialog)
        self.p11.setGeometry(QtCore.QRect(100, 100, 91, 101))
        self.p11.setText("")
        self.p11.setTextFormat(QtCore.Qt.RichText)
        self.p11.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Metapod_F.png"))
        self.p11.setObjectName("p11")
        self.p12 = QtWidgets.QLabel(Dialog)
        self.p12.setGeometry(QtCore.QRect(190, 100, 91, 101))
        self.p12.setText("")
        self.p12.setTextFormat(QtCore.Qt.RichText)
        self.p12.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Butterfree_F.png"))
        self.p12.setObjectName("p12")
        self.p13 = QtWidgets.QLabel(Dialog)
        self.p13.setGeometry(QtCore.QRect(280, 100, 91, 101))
        self.p13.setText("")
        self.p13.setTextFormat(QtCore.Qt.RichText)
        self.p13.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Weedle_F.png"))
        self.p13.setObjectName("p13")
        self.p14 = QtWidgets.QLabel(Dialog)
        self.p14.setGeometry(QtCore.QRect(370, 100, 91, 101))
        self.p14.setText("")
        self.p14.setTextFormat(QtCore.Qt.RichText)
        self.p14.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Kakuna_F.png"))
        self.p14.setObjectName("p14")
        self.p15 = QtWidgets.QLabel(Dialog)
        self.p15.setGeometry(QtCore.QRect(370, 100, 91, 101))
        self.p15.setText("")
        self.p15.setTextFormat(QtCore.Qt.RichText)
        self.p15.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Beedrill_F.png"))
        self.p15.setObjectName("p15")
        self.p16 = QtWidgets.QLabel(Dialog)
        self.p16.setGeometry(QtCore.QRect(460, 100, 91, 101))
        self.p16.setText("")
        self.p16.setTextFormat(QtCore.Qt.RichText)
        self.p16.setPixmap(QtGui.QPixmap("data/pokemon_sprite/Pidgey_F.png"))
        self.p16.setObjectName("p16")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        
        
class Window(QMainWindow, Ui_Dialog):
    
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.setupUi(self)


def run_app():
    app = QApplication(sys.argv)
    mainWin = Window()
    mainWin.show()
    app.exec_()
    
    
run_app()