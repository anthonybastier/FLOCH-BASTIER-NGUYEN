# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:31:30 2024

@author: anais
"""

from testbutton import *
from joueur import *
from pokemons import *
from map_tomata import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtCore import Qt

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
            
            
class Combat(QMainWindow, Ui_Form):
    
    def __init__(self, parent = None):
        super(Combat, self).__init__(parent)
        self.setupUi(self)
        self.Button_Pokemon.clicked.connect(self.chgt_pokemon)
        self.Button_attack.clicked.connect(self.attack_norm)
        self.Button_attack_spe.clicked.connect(self.attack_spe)
        self.Button_flee.clicked.connect(self.flee)
        
    def chgt_pokemon(self):
        dlg = Choix(self)
        dlg.exec()
        
    def attack_norm(self, pokemon_adv, joueur):
        pokemon_actuel = joueur.team[0]
        
        #Quel Pokémon agit en premier
        v1 = pokemon_actuel.speed
        v2 = pokemon_adv.speed
        if v1 > v2 :
            hp_p2 = pokemon_actuel.attaque_norm(pokemon_adv)
        
            if hp_p2 <= 0:
                #Combat gagné
                print("Vous attrapez " + pokemon_adv.nom)
                liste_entites.pop(pokemon_adv)
                self.close()
            else:
                hp_p1 = pokemon_adv.attaque_norm(pokemon_actuel)
                
                if hp_p1 <= 0:
                    if joueur.a_un_pokemon_non_ko():
                        self.chgt_pokemon()
                        
        
    
    def attack_spe(self,pokemon):
        pass
    
    def flee(self):
        print("Ran away safely !")
        self.close()
       
        
        
class Choix(QDialog):
    
    def __init__(self, parent = None):
        super(Choix, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        
def run_app():
    app = QApplication(sys.argv)
    mainWin = Overworld()
    mainWin.setupUI()
    mainWin.show()
    app.exec_()
    
    
run_app()