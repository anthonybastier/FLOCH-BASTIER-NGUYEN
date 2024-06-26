# -*- coding: utf-8 -*-
"""
@authors: Anais, Anthony, Thomas
"""
####### Imports #######
from PyQt5 import QtCore, QtGui, QtWidgets
from joueur import *
from pokemons import *

####### Interface graphique de combat #######

class Ui_Dialog(object):
    def setupUi(self, pokemon_team, pokemon_adv, Dialog):
        """
        Génère l'interface graphique du combat.

        Parameters
        ----------
        pokemon_team : Pokemon
            Pokémon actuel du joueur.
        pokemon_adv : Pokemon
            Pokémon adverse.
        Dialog : 
            Objet PyQt pour définir la taille de la fenêtre.

        """
        Dialog.setObjectName("Dialog")
        Dialog.resize(688, 888)
        pokemon_adv_HP_init = pokemon_adv.HP
        pokemon_team_HP_init = pokemon_team.HP
        self.Fond_Combat_Dialogue = QtWidgets.QLabel(Dialog)
        self.Fond_Combat_Dialogue.setGeometry(QtCore.QRect(0, 0, 691, 391))
        self.Fond_Combat_Dialogue.setText("")
        self.Fond_Combat_Dialogue.setTextFormat(QtCore.Qt.RichText)
        self.Fond_Combat_Dialogue.setPixmap(QtGui.QPixmap("data/fond combat.jpg"))
        self.Fond_Combat_Dialogue.setScaledContents(True)
        self.Fond_Combat_Dialogue.setObjectName("Fond_Combat_Dialogue")
        self.Fond_Combat_Button = QtWidgets.QLabel(Dialog)
        self.Fond_Combat_Button.setGeometry(QtCore.QRect(0, 390, 691, 551))
        self.Fond_Combat_Button.setText("")
        self.Fond_Combat_Button.setTextFormat(QtCore.Qt.RichText)
        self.Fond_Combat_Button.setPixmap(QtGui.QPixmap("data/buttons combat.jpg"))
        self.Fond_Combat_Button.setScaledContents(True)
        self.Fond_Combat_Button.setObjectName("Fond_Combat_Button")
        self.Attack_Button = QtWidgets.QPushButton(Dialog)
        self.Attack_Button.setGeometry(QtCore.QRect(80, 540, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.Attack_Button.setFont(font)
        self.Attack_Button.setObjectName("Attack_Button")
        self.Attack_Button.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.Spe_Attack_Button = QtWidgets.QPushButton(Dialog)
        self.Spe_Attack_Button.setGeometry(QtCore.QRect(390, 540, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.Spe_Attack_Button.setFont(font)
        self.Spe_Attack_Button.setObjectName("Spe_Attack_Button")
        self.Spe_Attack_Button.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.Flee_Button = QtWidgets.QPushButton(Dialog)
        self.Flee_Button.setGeometry(QtCore.QRect(80, 710, 231, 111))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.Flee_Button.setFont(font)
        self.Flee_Button.setObjectName("Flee_Button")
        self.Flee_Button.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.Pokemon_Button = QtWidgets.QPushButton(Dialog)
        self.Pokemon_Button.setGeometry(QtCore.QRect(390, 710, 231, 111))
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
        self.sprite_team.setGeometry(QtCore.QRect(70, 180, 131, 131))
        self.sprite_adv.setText("")
        self.sprite_adv.setTextFormat(QtCore.Qt.RichText)
        self.sprite_adv.setPixmap(QtGui.QPixmap(f"data/pokemon_sprite/{pokemon_adv.nom}_f.png"))
        self.sprite_adv.setScaledContents(True)
        self.sprite_adv.setObjectName("sprite_adv")
        self.sprite_adv.setGeometry(QtCore.QRect(460, 60, 121, 121))
        self.Nom_pokemon_adv = QtWidgets.QLineEdit(Dialog)
        self.Nom_pokemon_adv.setGeometry(QtCore.QRect(10, 40, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.Nom_pokemon_adv.setFont(font)
        self.Nom_pokemon_adv.setObjectName("Nom_pokemon_adv")
        self.Nom_pokemon_adv.setStyleSheet("QLineEdit { background-color: transparent; border: 0px }")
        self.Nom_pokemon_team = QtWidgets.QLineEdit(Dialog)
        self.Nom_pokemon_team.setGeometry(QtCore.QRect(410, 240, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.Nom_pokemon_team.setFont(font)
        self.Nom_pokemon_team.setObjectName("Nom_pokemon_team")
        self.Nom_pokemon_team.setStyleSheet("QLineEdit { background-color: transparent; border: 0px }")
        self.HP_adv = QtWidgets.QLineEdit(Dialog)
        self.HP_adv.setGeometry(QtCore.QRect(180, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.HP_adv.setFont(font)
        self.HP_adv.setObjectName("HP_adv")
        self.HP_adv.setStyleSheet("QLineEdit { background-color: transparent; border: 0px }")
        self.HP_pokemon_team = QtWidgets.QLineEdit(Dialog)
        self.HP_pokemon_team.setGeometry(QtCore.QRect(580, 240, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.HP_pokemon_team.setFont(font)
        self.HP_pokemon_team.setObjectName("HP_pokemon_team")
        self.HP_pokemon_team.setStyleSheet("QLineEdit { background-color: transparent; border: 0px }")
        self.zone_a_edit = QtWidgets.QLineEdit(Dialog)
        self.zone_a_edit.setGeometry(QtCore.QRect(40, 320, 601, 61))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.zone_a_edit.setFont(font)
        self.zone_a_edit.setObjectName("zone_a_edit")
        self.zone_a_edit.setStyleSheet("QLineEdit { background-color: transparent; border: 0px }")

        self.retranslateUi(pokemon_team, pokemon_adv,Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, pokemon_team, pokemon_adv, Dialog):
        """
        Initialise le dialogue du combat.

        Parameters
        ----------
        pokemon_team : Pokemon
            Pokémon actuel du joueur.
        pokemon_adv : Pokemon
            Pokémon adverse.
        Dialog :
            Objet PyQt.

        """
        pokemon_adv_HP_init = pokemon_adv.HP
        pokemon_team_HP_init = pokemon_team.HP
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Attack_Button.setText(_translate("Dialog", "Attack"))
        self.Spe_Attack_Button.setText(_translate("Dialog", "Special Attack"))
        self.Flee_Button.setText(_translate("Dialog", "Flee"))
        self.Pokemon_Button.setText(_translate("Dialog", "Pokemon"))
        self.Nom_pokemon_adv.setText(_translate("Dialog", f"{pokemon_adv.nom}"))
        self.Nom_pokemon_team.setText(_translate("Dialog", f"{pokemon_team.nom}"))
        self.HP_adv.setText(_translate("Dialog", f"HP {pokemon_adv.HP}/{pokemon_adv_HP_init}"))
        self.HP_pokemon_team.setText(_translate("Dialog", f"HP {pokemon_team.HP}/{pokemon_team_HP_init}"))
        self.zone_a_edit.setText(_translate("Dialog", f"A {pokemon_adv.nom} appears !"))

    def update_pokemon(self, Dialog, pokemon):
        """
        Fonction utilisée pour mettre à jour les données et le sprite du Pokémon
        actuel du joueur en cas de changement.

        Parameters
        ----------
        Dialog :
            Objet PyQt.
        pokemon : Pokemon
            Nouveau Pokémon choisi par le joueur.

        """
        self.Nom_pokemon_team.setText(f"{pokemon.nom}")
        self.HP_pokemon_team.setText(f"HP {pokemon.HP}/{pokemon.HP}")
        self.sprite_team.setPixmap(QtGui.QPixmap(f"data/pokemon_sprite/{pokemon.nom}_d.png"))