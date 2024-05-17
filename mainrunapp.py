# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:31:30 2024

@author: anais
"""
####### Imports #######

from ig_combat import *
from joueur import *
from pokemons import *
from map_tomata import *
from ig_combat import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

####### Définition des protagonistes #######

joueur = Joueur((0,0))
pokemon_team = joueur.team[0]
index = rd.randint(0,150)
pokemon_adv = liste_pokemon[index]

####### Programme principal #######

class Overworld(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setEnabled(True)
    
    def keyReleaseEvent(self,event):
        if event.key()==Qt.Key_Up:
            self.carte.move("up")
        if event.key()==Qt.Key_Down:
            self.carte.move("down")        
        if event.key()==Qt.Key_Left:
            self.carte.move("left")        
        if event.key()==Qt.Key_Right:
            self.carte.move("right")
    
    def setupUI(self):
        self.resize(500,500)
        self.setWindowTitle("Pookemon")
        self.carte=Carte(self)
            
            
class Combat(QMainWindow, Ui_Dialog):
    
    def __init__(self, parent = None):
        
        super(Combat, self).__init__(parent)
        self.pokemon_actuel = joueur.team[0]
        self.pokemon_adv = liste_pokemon[index]        
        self.setupUi(self)
        self.Pokemon_Button.clicked.connect(lambda: self.chgt_pokemon(self.pokemon_adv, joueur))
        self.Attack_Button.clicked.connect(lambda: self.attack(joueur, "attaque_norm"))
        self.Spe_Attack_Button.clicked.connect(lambda: self.attack(joueur, "attaque_spe"))
        self.Flee_Button.clicked.connect(self.flee)
    
    def chgt_pokemon(self, joueur):
        dlg = Choix(self)
        dlg.exec()
        
        hp_p1 = self.pokemon_adv.choix_attaque()(self.pokemon_actuel)
        
        if hp_p1 <= 0:
            #Pokémon actuel KO
            if joueur.a_un_pokemon_non_ko():
                #Obligé de changer de Pokémon
                dlg = Choix(self)
                dlg.exec()
            else:
                #Combat perdu
                print("Out of usable Pokemon !")
                self.close()
                joueur.soigner_equipe()
        
    def attack(self, joueur, attaque):
        if attaque == "attaque_norm":
            atq = self.pokemon_actuel.attaque_norm
        else:
            atq = self.pokemon_actuel.attaque_spe
        
        #Quel Pokémon agit en premier
        v1 = self.pokemon_actuel.speed
        v2 = self.pokemon_adv.speed
        if v1 > v2 :
            #Le Pokémon du joueur attaque en premier
            hp_p2 = atq(self.pokemon_adv)
        
            if hp_p2 <= 0: #Combat gagné
                print("You caught " + self.pokemon_adv.nom + " !")
                liste_entites.remove_pokemon(self.pokemon_adv.position)
                self.close()
                joueur.soigner_equipe()
            else:
                #Le Pokémon adverse attaque en deuxième
                hp_p1 = self.pokemon_adv.choix_attaque()(self.pokemon_actuel)
                
                if hp_p1 <= 0:
                    #Pokémon actuel KO
                    if joueur.a_un_pokemon_non_ko():
                        #Obligé de changer de Pokémon
                        dlg = Choix(self)
                        dlg.exec()
                    else:
                        #Combat perdu
                        print("Out of usable Pokemon !")
                        self.close()
                        joueur.soigner_equipe()
        else:
            #Le Pokémon adverse attaque en premier
            hp_p1 = self.pokemon_adv.choix_attaque()(self.pokemon_actuel)
            
            if hp_p1 <= 0:
                #Pokémon actuel KO
                if joueur.a_un_pokemon_non_ko():
                    #Obligé de changer de Pokémon
                    self.chgt_pokemon()
                else:
                    #Combat perdu
                    print("Out of usable Pokemon !")
                    self.close()
                    joueur.soigner_equipe()
            else:
                # Le Pokémon du joueur attaque en deuxième
                hp_p2 = atq(self.pokemon_adv)

                # Vérifier si le Pokémon adverse est KO
                if hp_p2 <= 0:
                    # Combat gagné
                    print("You caught " + self.pokemon_adv.nom + " !")
                    liste_entites.remove_pokemon(self.pokemon_adv.position)
                    self.close()
                    joueur.soigner_equipe()
        
    def flee(self):
        self.label.setText("Ran away safely !") 
        print("Ran away safely !")
        self.close()
       
        
        
class Choix(QDialog):
    def __init__(self, parent = None):
        super(Choix, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        # Window title
        self.setWindowTitle("Change Pokémon")

        # Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Label for displaying current Pokémon
        self.label_current_pokemon = QLabel(f"Current Pokémon: {joueur.team[0].nom}")
        self.layout.addWidget(self.label_current_pokemon)

        # Create buttons for each Pokémon in the team
        self.pokemon_buttons = []
        for i, pokemon in enumerate(joueur.team):
            if pokemon.HP ==0 :
                # Disable button if Pokémon is KO
                button = QPushButton(f"{pokemon.nom} (KO)")
                button.setEnabled(False)
            else:
                # Enable button for healthy Pokémon
                button = QPushButton(pokemon.nom)
                button.clicked.connect(lambda _, index=i: self.switch_pokemon(index))

            self.pokemon_buttons.append(button)
            self.layout.addWidget(button)

        # Cancel button
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close)
        self.layout.addWidget(self.cancel_button)

    def switch_pokemon(self, index):
        # Switch the current Pokémon with the selected one
        nouveau_pkmn = joueur.team[index]
        joueur.team[index] = joueur.team[0]
        joueur.team[0] = nouveau_pkmn
        self.label_current_pokemon.setText(f"Current Pokémon: {joueur.team[0].nom}")
        self.close()  # Close the dialog after switching

        # Update the combat window if necessary (assuming this is called from the Combat class)
        if self.parent():
            # Get a reference to the Combat window
            combat_window = self.parent()

            # Update the displayed Pokémon information in the combat window
            combat_window.update_pokemon_info()
    """
def run_app():
    app = QApplication(sys.argv)
    mainWin = Combat()
    #mainWin = Overworld()
    #mainWin.setupUI()
    mainWin.show()
    app.exec_()
    
    
run_app()