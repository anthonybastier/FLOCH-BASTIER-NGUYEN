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
        #Récupération des stats initiales des PKMN
        self.pokemon_actuel = joueur.team[0]
        self.HP_init_act = self.pokemon_actuel.HP
        self.pokemon_adv = liste_pokemon[index]     
        self.HP_init_adv = self.pokemon_adv.HP
        
        self.setupUi(self)
        self.Pokemon_Button.clicked.connect(lambda: self.chgt_pokemon(self.pokemon_adv, joueur))
        self.Attack_Button.clicked.connect(lambda: self.attack(joueur, "normal attack"))
        self.Spe_Attack_Button.clicked.connect(lambda: self.attack(joueur, "special attack"))
        self.Flee_Button.clicked.connect(self.flee)
    
    def chgt_pokemon(self, joueurs):
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
        #Type de l'attaque
        if attaque == "normal attack":
            atq = self.pokemon_actuel.attaque_norm
        else:
            atq = self.pokemon_actuel.attaque_spe
        
        #Quel Pokémon agit en premier
        v1 = self.pokemon_actuel.speed
        v2 = self.pokemon_adv.speed    
        if v1 > v2 :
            #Le Pokémon du joueur attaque en premier
            self.zone_a_edit.setText((f"{self.pokemon_actuel.nom} uses a "+attaque))
            hp_p2 = atq(self.pokemon_adv)
            
            #La fonction attaque renvoyant les HP du pokémon attaqués selon ses HP initiaux, on vient modifier les HP initiaux avec la nouvelle valeur
            self.pokemon_adv.HP = hp_p2
            self.HP_adv.setText(f"HP {self.pokemon_adv.HP}/{self.HP_init_adv}")
        
            if hp_p2 <= 0: #Combat gagné
                self.zone_a_edit.setText("You caught " + self.pokemon_adv.nom + " !")
                print("You caught " + self.pokemon_adv.nom + " !")
                liste_entites.remove_pokemon(self.pokemon_adv.position)
                #self.close()
                joueur.soigner_equipe()
            else:
                #Le Pokémon adverse attaque en deuxième
                adv_atk = self.pokemon_adv.choix_attaque()
                if adv_atk == "attaque_norm":
                    print(str(adv_atk))
                    self.zone_a_edit.setText((f"{self.pokemon_adv.nom} uses a normal attack"))
                    hp_p1 = self.pokemon_adv.attaque_norm(self.pokemon_actuel)
                    self.pokemon_actuel.HP = hp_p1
                else:
                    self.zone_a_edit.setText((f"{self.pokemon_adv.nom} uses a special attack"))
                    hp_p1 = self.pokemon_adv.attaque_spe(self.pokemon_actuel)
                    self.pokemon_actuel.HP = hp_p1
                    
                self.HP_pokemon_team.setText(f"HP {self.pokemon_actuel.HP}/{self.HP_init_act}")
                
                if hp_p1 <= 0:
                    #Pokémon actuel KO
                    if joueur.a_un_pokemon_non_ko():
                        #Obligé de changer de Pokémon
                        dlg = Choix()
                        dlg.exec()
                    else:
                        #Combat perdu
                        print("Out of usable Pokemon !")
                        self.close()
                        joueur.soigner_equipe()
        else:
            #Le Pokémon adverse attaque en premier
            adv_atk = self.pokemon_adv.choix_attaque()
            if adv_atk == "attaque_norm":
                self.zone_a_edit.setText(f"{self.pokemon_adv.nom} uses a normal attack")
                hp_p1 = self.pokemon_adv.attaque_norm(self.pokemon_actuel)
                self.pokemon_actuel.HP = hp_p1
            else:
                self.zone_a_edit.setText(f"{self.pokemon_adv.nom} uses a special attack")
                hp_p1 = self.pokemon_adv.attaque_spe(self.pokemon_actuel)
                self.pokemon_actuel.HP = hp_p1
            self.HP_pokemon_team.setText(f"HP {self.pokemon_actuel.HP}/{self.HP_init_act}")

            
            if hp_p1 <= 0:
                #Pokémon actuel KO
                if joueur.a_un_pokemon_non_ko():
                    #Obligé de changer de Pokémon
                    self.chgt_pokemon(joueur)
                else:
                    #Combat perdu
                    print("Out of usable Pokemon !")
                    self.close()
                    joueur.soigner_equipe()
            else:
                # Le Pokémon du joueur attaque en deuxième
                self.zone_a_edit.setText((f"{self.pokemon_actuel.nom} uses a "+attaque))
                hp_p2 = atq(self.pokemon_adv)
                
                self.pokemon_adv.HP = hp_p2
                self.HP_adv.setText(f"HP {self.pokemon_adv.HP}/{self.HP_init_adv}")
                
                # Vérifier si le Pokémon adverse est KO
                if hp_p2 <= 0:
                    self.zone_a_edit.setText("You caught " + self.pokemon_adv.nom + " !")
                    print("You caught " + self.pokemon_adv.nom + " !")
                    liste_entites.remove_pokemon(self.pokemon_adv.position)
                    #self.close()
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

def run_app():
    app = QApplication(sys.argv)
    mainWin = Combat()
    #mainWin = Overworld()
    #mainWin.setupUI()
    mainWin.show()
    app.exec_()
    
    
run_app()