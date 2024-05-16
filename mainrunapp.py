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
        self.Pokemon_Button.clicked.connect(lambda: self.chgt_pokemon(pokemon_adv, joueur))
        self.Attack_Button.clicked.connect(lambda: self.attack(pokemon_adv, joueur, "attaque_norm"))
        self.Spe_Attack_Button.clicked.connect(lambda: self.attack(pokemon_adv, joueur, "attaque_spe"))
        self.Flee_Button.clicked.connect(self.flee)
    
    def chgt_pokemon(self, pokemon_adv, joueur):
        dlg = Choix(self)
        dlg.exec()
        
        hp_p1 = self.pokemon_adv.choix_attaque()(pokemon_actuel)
        
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
        
    def attack(self, pokemon_adv, joueur, attaque):
        if attaque == "attaque_norm":
            atq = pokemon_actuel.attaque_norm
        else:
            atq = pokemon_actuel.attaque_spe
        
        #Quel Pokémon agit en premier
        v1 = pokemon_actuel.speed
        v2 = pokemon_adv.speed
        if v1 > v2 :
            #Le Pokémon du joueur attaque en premier
            hp_p2 = atq(pokemon_adv)
        
            if hp_p2 <= 0: #Combat gagné
                print("You caught " + pokemon_adv.nom + " !")
                liste_entites.remove_pokemon(pokemon_adv.position)
                self.close()
                joueur.soigner_equipe()
            else:
                #Le Pokémon adverse attaque en deuxième
                hp_p1 = pokemon_adv.choix_attaque()(pokemon_actuel)
                
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
            hp_p1 = pokemon_adv.choix_attaque()(pokemon_actuel)
            
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
                hp_p2 = atq(pokemon_adv)

                # Vérifier si le Pokémon adverse est KO
                if hp_p2 <= 0:
                    # Combat gagné
                    print("You caught " + pokemon_adv.nom + " !")
                    liste_entites.remove_pokemon(pokemon_adv.position)
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
        self.ui.setupUi(self,"Team" )

def run_app():
    app = QApplication(sys.argv)
    mainWin = Combat()
    #mainWin = Overworld()
    #mainWin.setupUI()
    mainWin.show()
    app.exec_()
    
    
run_app()