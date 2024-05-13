# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:43:58 2024

@author: anais
"""
####### Imports #######

from PyQt5 import QtCore, QtGui, QtWidgets
from joueur import *
from pokemons import *

####### Définition des protagonistes #######

joueur = Joueur((0,0),6) #joueur en 0,0 avec 6 pokemon dans sa team
pokemon_team = joueur.team[0]
pokemon_team_HP_init = pokemon_team.HP
index = rd.randint(0,150)
pokemon_adv = liste_pokemon[index] #pokemon_adv.nom renvoie son nom dcp
pokemon_adv_HP_init = pokemon_adv.HP

####### Interface Graphique de Combat #######

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1022, 1344)
        self.Fond_Combat_Dialogue = QtWidgets.QLabel(Dialog)
        self.Fond_Combat_Dialogue.setGeometry(QtCore.QRect(0, 0, 1022, 642))
        self.Fond_Combat_Dialogue.setText("")
        self.Fond_Combat_Dialogue.setTextFormat(QtCore.Qt.RichText)
        self.Fond_Combat_Dialogue.setPixmap(QtGui.QPixmap("data/fond combat.jpg"))
        self.Fond_Combat_Dialogue.setScaledContents(True)
        self.Fond_Combat_Dialogue.setObjectName("Fond_Combat_Dialogue")
        self.Fond_Combat_Button = QtWidgets.QLabel(Dialog)
        self.Fond_Combat_Button.setGeometry(QtCore.QRect(0, 640, 1022, 702))
        self.Fond_Combat_Button.setText("")
        self.Fond_Combat_Button.setTextFormat(QtCore.Qt.RichText)
        self.Fond_Combat_Button.setPixmap(QtGui.QPixmap("data/buttons combat.jpg"))
        self.Fond_Combat_Button.setScaledContents(True)
        self.Fond_Combat_Button.setObjectName("Fond_Combat_Button")
        self.Attack_Button = QtWidgets.QPushButton(Dialog)
        self.Attack_Button.setGeometry(QtCore.QRect(110, 810, 361, 161))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.Attack_Button.setFont(font)
        self.Attack_Button.setObjectName("Attack_Button")
        self.Attack_Button.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.Spe_Attack_Button = QtWidgets.QPushButton(Dialog)
        self.Spe_Attack_Button.setGeometry(QtCore.QRect(570, 810, 361, 161))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.Spe_Attack_Button.setFont(font)
        self.Spe_Attack_Button.setObjectName("Spe_Attack_Button")
        self.Spe_Attack_Button.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.Flee_Button = QtWidgets.QPushButton(Dialog)
        self.Flee_Button.setGeometry(QtCore.QRect(110, 1040, 361, 161))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.Flee_Button.setFont(font)
        self.Flee_Button.setObjectName("Flee_Button")
        self.Flee_Button.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.Pokemon_Button = QtWidgets.QPushButton(Dialog)
        self.Pokemon_Button.setGeometry(QtCore.QRect(570, 1040, 361, 161))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.Pokemon_Button.setFont(font)
        self.Pokemon_Button.setObjectName("Pokemon_Button")
        self.Pokemon_Button.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.sprite_team = QtWidgets.QLabel(Dialog)
        self.sprite_team.setGeometry(QtCore.QRect(100, 290, 261, 241))
        self.sprite_team.setText("")
        self.sprite_team.setTextFormat(QtCore.Qt.RichText)
        self.sprite_team.setPixmap(QtGui.QPixmap(f"data/pokemon_sprite/{pokemon_team.nom}_d.png"))
        self.sprite_team.setScaledContents(True)
        self.sprite_team.setObjectName("sprite_team")
        self.sprite_adv = QtWidgets.QLabel(Dialog)
        self.sprite_adv.setGeometry(QtCore.QRect(630, 115, 261, 241))
        self.sprite_adv.setText("")
        self.sprite_adv.setTextFormat(QtCore.Qt.RichText)
        self.sprite_adv.setPixmap(QtGui.QPixmap(f"data/pokemon_sprite/{pokemon_adv.nom}_f.png"))
        self.sprite_adv.setScaledContents(True)
        self.sprite_adv.setObjectName("sprite_adv")
        self.Nom_pokemon_adv = QtWidgets.QLineEdit(Dialog)
        self.Nom_pokemon_adv.setGeometry(QtCore.QRect(20, 60, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.Nom_pokemon_adv.setFont(font)
        self.Nom_pokemon_adv.setObjectName("Nom_pokemon_adv")
        self.Nom_pokemon_adv.setStyleSheet("QLineEdit { background-color: transparent; border: 0px }")
        self.Nom_pokemon_team = QtWidgets.QLineEdit(Dialog)
        self.Nom_pokemon_team.setGeometry(QtCore.QRect(610, 390, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.Nom_pokemon_team.setFont(font)
        self.Nom_pokemon_team.setObjectName("Nom_pokemon_team")
        self.Nom_pokemon_team.setStyleSheet("QLineEdit { background-color: transparent; border: 0px }")
        self.HP_adv = QtWidgets.QLineEdit(Dialog)
        self.HP_adv.setGeometry(QtCore.QRect(230, 90, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.HP_adv.setFont(font)
        self.HP_adv.setObjectName("HP_adv")
        self.HP_adv.setStyleSheet("QLineEdit { background-color: transparent; border: 0px }")
        self.HP_pokemon_team = QtWidgets.QLineEdit(Dialog)
        self.HP_pokemon_team.setGeometry(QtCore.QRect(830, 410, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.HP_pokemon_team.setFont(font)
        self.HP_pokemon_team.setObjectName("HP_pokemon_team")
        self.HP_pokemon_team.setStyleSheet("QLineEdit { background-color: transparent; border: 0px }")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Attack_Button.setText(_translate("Dialog", "Attack"))
        self.Spe_Attack_Button.setText(_translate("Dialog", "Special Attack"))
        self.Flee_Button.setText(_translate("Dialog", "Flee"))
        self.Pokemon_Button.setText(_translate("Dialog", "Pokemon"))
        self.Nom_pokemon_adv.setText(_translate("Dialog", f"{pokemon_adv.nom}"))
        self.Nom_pokemon_team.setText(_translate("Dialog", f"{pokemon_team.nom}"))
        self.HP_adv.setText(_translate("Dialog", f"HP/{pokemon_adv_HP_init}"))
        self.HP_pokemon_team.setText(_translate("Dialog", f"HP/{pokemon_team_HP_init}"))
