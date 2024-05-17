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
import pokedex as poke
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5 import QtTest
from PyQt5.QtCore import Qt


####### Initialisation du joueur #######

joueur = Joueur([5,5])

####### Programme principal #######

class Overworld(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setEnabled(True)
    
    def keyPressEvent(self,event):
        
        if event.key()==Qt.Key_P:
            poke.run_app()
            self.close()
        
        if event.key()==Qt.Key_Up:
            if (joueur.position[1]<=5 and joueur.position[1]>0) or (joueur.position[1]>=36 and joueur.position[1]<=39):
                self.trainer.move("up")
                joueur.position[1]-=1

            elif joueur.position[1]>5 and joueur.position[1]<36:
                self.carte.move("up")
                joueur.position[1]-=1
            if matrice_collision[joueur.position[0]][joueur.position[1]]!=[]:
                print(matrice_collision[joueur.position[0]][joueur.position[1]][0].nom)
                combat_win=Combat()
                combat_win.show()


        if event.key()==Qt.Key_Down:
            if (joueur.position[1]<=4 and joueur.position[1]>=0) or (joueur.position[1]>=35 and joueur.position[1]<39):
                self.trainer.move("down")
                joueur.position[1]+=1
            elif joueur.position[1]<35 and joueur.position[1]>4:
                self.carte.move("down")
                joueur.position[1]+=1
            if matrice_collision[joueur.position[0]][joueur.position[1]]!=[]:
                print(matrice_collision[joueur.position[0]][joueur.position[1]][0].nom)
                combat_win=Combat()
                combat_win.show()            
                
                
                
        if event.key()==Qt.Key_Left:
            if (joueur.position[0]<=5 and joueur.position[0]>0) or (joueur.position[0]>=36 and joueur.position[0]<=39):
                self.trainer.move("left")
                joueur.position[0]-=1
            elif joueur.position[0]>5 and joueur.position[0]<36:
                self.carte.move("left")
                joueur.position[0]-=1
            if matrice_collision[joueur.position[0]][joueur.position[1]]!=[]:
                print(matrice_collision[joueur.position[0]][joueur.position[1]][0].nom)
                combat_win=Combat()
                combat_win.show()

        if event.key()==Qt.Key_Right:
            if (joueur.position[0]<=4 and joueur.position[0]>=0) or (joueur.position[0]>=35 and joueur.position[0]<39):
                self.trainer.move("right")
                joueur.position[0]+=1
            elif joueur.position[0]<35 and joueur.position[0]>4:
                self.carte.move("right")
                joueur.position[0]+=1
            if matrice_collision[joueur.position[0]][joueur.position[1]]!=[]:
                print(matrice_collision[joueur.position[0]][joueur.position[1]][0].nom)
                combat_win=Combat()
                combat_win.show()

    
    def setupUI(self):
        self.resize(500,500)
        self.setWindowTitle("Pookemon")
        self.carte=Carte(self)
        self.trainer=Sprite(self)
            

class Combat(QMainWindow, Ui_Dialog):
    
    def __init__(self, parent = None):
        
        super(Combat, self).__init__(parent)
        #Récupération des stats initiales des PKMN
        self.pokemon_actuel = joueur.team[0]
        self.HP_init_act = self.pokemon_actuel.HP
        self.pokemon_adv = matrice_collision[joueur.position[0]][joueur.position[1]][0]     
        self.HP_init_adv = self.pokemon_adv.HP
        
        self.setupUi(self.pokemon_actuel, self.pokemon_adv, self)
        self.Pokemon_Button.clicked.connect(lambda: self.chgt_pokemon(joueur))
        self.Attack_Button.clicked.connect(lambda: self.attack(joueur, "normal attack"))
        self.Spe_Attack_Button.clicked.connect(lambda: self.attack(joueur, "special attack"))
        self.Flee_Button.clicked.connect(self.flee)
    
    def chgt_pokemon(self, joueurs):
        dlg = Choix(self)
        dlg.exec()
        
        #Mettre à jour le Pokémon actuel
        self.pokemon_actuel = joueur.team[0]
        self.HP_init_act = self.pokemon_actuel.HP

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
            self.zone_a_edit.setText(f"{self.pokemon_actuel.nom} uses a "+attaque)
            hp_p2 = atq(self.pokemon_adv)
            
            #La fonction attaque renvoyant les HP du pokémon attaqués selon ses HP initiaux, on vient modifier les HP initiaux avec la nouvelle valeur
            if hp_p2 < 0:
                self.pokemon_adv.HP = 0
            else:
                self.pokemon_adv.HP = hp_p2
                
            self.HP_adv.setText(f"HP {self.pokemon_adv.HP}/{self.HP_init_adv}")
            QtTest.QTest.qWait(1000)
            
            if hp_p2 <= 0: #Combat gagné
                self.zone_a_edit.setText("You caught " + self.pokemon_adv.nom + " !")
                QtTest.QTest.qWait(1000)
                liste_entites.remove_pokemon(self.pokemon_adv.position)
                matrice_collision[joueur.position[0]][joueur.position[1]].pop(0)
                joueur.team.append(self.pokemon_adv)
                self.close()
                joueur.soigner_equipe()
            else:
                #Le Pokémon adverse attaque en deuxième
                adv_atk = self.pokemon_adv.choix_attaque()
                if adv_atk == "attaque_norm":
                    self.zone_a_edit.setText((f"{self.pokemon_adv.nom} uses a normal attack"))
                    hp_p1 = self.pokemon_adv.attaque_norm(self.pokemon_actuel)
                    self.pokemon_actuel.HP = hp_p1
                else:
                    self.zone_a_edit.setText((f"{self.pokemon_adv.nom} uses a special attack"))
                    hp_p1 = self.pokemon_adv.attaque_spe(self.pokemon_actuel)
                    self.pokemon_actuel.HP = hp_p1
                    
                if hp_p1 < 0:
                    self.pokemon_actuel.HP = 0
                    
                self.HP_pokemon_team.setText(f"HP {self.pokemon_actuel.HP}/{self.HP_init_act}")
                QtTest.QTest.qWait(1000)
                
                if hp_p1 <= 0:
                    #Pokémon actuel KO
                    self.zone_a_edit.setText(f"{self.pokemon_actuel.nom} est KO !")
                    QtTest.QTest.qWait(1000)
                    if joueur.a_un_pokemon_non_ko():
                        #Obligé de changer de Pokémon
                        self.chgt_pokemon(joueur)
                    else:
                        #Combat perdu
                        QtTest.QTest.qWait(1000)
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
      
            if hp_p1 < 0:
                self.pokemon_actuel.HP = 0  
                
            self.HP_pokemon_team.setText(f"HP {self.pokemon_actuel.HP}/{self.HP_init_act}")  
            QtTest.QTest.qWait(1000)
            
            if hp_p1 <= 0:
                #Pokémon actuel KO
                self.zone_a_edit.setText(f"{self.pokemon_actuel.nom} is KO !")
                QtTest.QTest.qWait(1000)
                if joueur.a_un_pokemon_non_ko():
                    #Obligé de changer de Pokémon
                    self.chgt_pokemon(joueur)
                else:
                    #Combat perdu
                    self.zone_a_edit.setText("Out of usable Pokémon !")
                    QtTest.QTest.qWait(1000)
                    self.close()
                    joueur.soigner_equipe()
            else:
                #Le Pokémon du joueur attaque en deuxième
                self.zone_a_edit.setText((f"{self.pokemon_actuel.nom} uses a "+attaque))
                hp_p2 = atq(self.pokemon_adv)
                
                self.pokemon_adv.HP = hp_p2
                
                if hp_p2 < 0:
                    self.pokemon_adv.HP = 0
                else:
                    self.pokemon_adv.HP = hp_p2   
                    
                self.HP_adv.setText(f"HP {self.pokemon_adv.HP}/{self.HP_init_adv}")
                QtTest.QTest.qWait(1000)
                
                #Vérifier si le Pokémon adverse est KO
                if hp_p2 <= 0:
                    self.zone_a_edit.setText("You caught " + self.pokemon_adv.nom + " !")
                    QtTest.QTest.qWait(1000)
                    liste_entites.remove_pokemon(self.pokemon_adv.position)
                    matrice_collision[joueur.position[0]][joueur.position[1]].pop(0)
                    joueur.team.append(self.pokemon_adv)
                    self.close()
                    joueur.soigner_equipe()
    def flee(self):
        self.zone_a_edit.setText("Ran away safely !")
        QtTest.QTest.qWait(1000)
        joueur.soigner_equipe()
        self.close()
        
       
        
        
class Choix(QDialog):

        
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Switch to which Pokémon ?")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.label_current_pokemon = QLabel(f"Current Pokémon: {joueur.team[0].nom}")
        self.layout.addWidget(self.label_current_pokemon)
        self.pokemon_buttons = []
        
        for i, pokemon in enumerate(joueur.team):
            if pokemon.HP == 0 :
                #Bouton désactivé si Pokémon KO
                button = QPushButton(f"{pokemon.nom} (KO)")
                button.setEnabled(False)
            else:
                #Bouton activé sinon
                button = QPushButton(pokemon.nom)
                button.clicked.connect(lambda _, index=i: self.switch_pokemon(index))

            self.pokemon_buttons.append(button)
            self.layout.addWidget(button)

    def switch_pokemon(self, index):
        nouveau_pkmn = joueur.team[index]
        joueur.team[index] = joueur.team[0]
        joueur.team[0] = nouveau_pkmn
        self.label_current_pokemon.setText(f"Current Pokémon: {joueur.team[0].nom}")

        #Mise à jour des infos du Pokémon affiché
        self.parent().update_pokemon(self,nouveau_pkmn)
        self.close()

def run_app():
    app = QApplication(sys.argv)
    mainWin = Overworld()
    mainWin.setupUI()
    mainWin.show()
    app.exec_()
    