# -*- coding: utf-8 -*-
"""
@authors: Anais, Anthony, Thomas
"""
####### Imports #######
from ig_combat import *
from joueur import *
from pokemons import *
from map_tomata import *
from ig_combat import *
import pokedex as poke
import sys
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5 import QtTest
from PyQt5.QtCore import Qt


####### Initialisation du joueur #######

joueur = Joueur() #Initialise le joueur à la position [5,5] et avec les starters

####### Construction de la matrice de collision #######
"""
On construit la matrice de collision du jeu par projection des positions des 
Pokémons sur une grille 40x40.
Une liste vide correspond à une absence de pokemon sauvage et donc de collision.
Une liste non vide contient tous les pokemons qui se retrouvent avec la même position dans notre grille de jeu 40x40.

"""
matrice_collision=[[[]for i in range(40)]for j in range(40)] 
liste_pos=[]
for i in liste_entites:
    liste_pos.append(i.position)
liste_pos=np.array(liste_pos).transpose()
minx,maxx=min(liste_pos[0]),max(liste_pos[0])
miny,maxy=min(liste_pos[1]),max(liste_pos[1])

for i in  liste_entites:
    matrice_collision[int((i.position[0]-minx)*39/(maxx-minx))][int((i.position[1]-miny)*39/(maxy-miny))].append(i)

####### Programme principal #######

class Overworld(QMainWindow):
    def __init__(self):
        """
        Initialise l'objet Overworld qui sert de support à l'affichage de la phase de jeu hors combat.
        
        """
        QMainWindow.__init__(self)
        self.setEnabled(True)
    
    def keyPressEvent(self,event):
        """
        Gère les inputs lors de la phase overworld notamment P pour ouvrir le
        Pokédex (memoire des Pokémons attrapés) et les flèches directionnelles 
        pour le déplacement du joueur ou de la carte selon les effets de bord.
        Le déplacement peut aussi induire la rencontre avec des Pokémons 
        sauvages avec la matrice de collision construite dans pokemons.py
        
        Parameters
        ----------
        event 
            Evènement d'appui de touche lorsque la fenêtre Overworld est ouverte.

        """
        
        #Ouverture du Pokédex
        if event.key()==Qt.Key_P:
            poke.run_app()
            
        #Déplacements du joueur
        if event.key()==Qt.Key_Up:
            if (joueur.position[1]<=5 and joueur.position[1]>0) or (joueur.position[1]>=36 and joueur.position[1]<=39):
                self.trainer.move("up")
                joueur.position[1]-=1

            elif joueur.position[1]>5 and joueur.position[1]<36:
                self.carte.move("up")
                joueur.position[1]-=1
            if matrice_collision[joueur.position[0]][joueur.position[1]]!=[]:
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
                combat_win=Combat()
                combat_win.show()

    
    def setupUI(self):
        """
        Définit la taille de la fenêtre de jeu. Regroupe tous les objets à
        afficher lors de la phase de jeu Overworld (hors combat) la carte et
        le sprite du joueur.

        """
        self.resize(500,500)
        self.setWindowTitle("Pookemon")
        self.carte=Carte(self)
        self.trainer=Sprite(self)
            

class Combat(QMainWindow, Ui_Dialog):
    
    def __init__(self, parent = None):
        """
        Initialise un combat Pokémon. Fait apparaître l'interface graphique du 
        choix, le Pokémon actuel du joueur et le Pokémon adverse avec leurs HP
        respectifs. Le joueur peut choisir entre une attaque normale, une 
        attaque spéciale, la fuite et le changement de Pokémon.
        """
        super(Combat, self).__init__(parent)
        
        #Récupération des stats initiales des Pokémons
        self.pokemon_actuel = joueur.team[0]
        self.HP_init_act = self.pokemon_actuel.HP
        self.pokemon_adv = matrice_collision[joueur.position[0]][joueur.position[1]][0]     
        self.HP_init_adv = self.pokemon_adv.HP
        
        #Récupération des inputs
        self.setupUi(self.pokemon_actuel, self.pokemon_adv, self)
        self.Pokemon_Button.clicked.connect(lambda: self.chgt_pokemon(joueur))
        self.Attack_Button.clicked.connect(lambda: self.attack(joueur, "normal attack"))
        self.Spe_Attack_Button.clicked.connect(lambda: self.attack(joueur, "special attack"))
        self.Flee_Button.clicked.connect(self.flee)
    
    def chgt_pokemon(self, joueur):
        """
        Permet au joueur de changer de Pokémon. Cette fonction est appelée si 
        le Pokémon actuel est KO ou si le joueur a utilisé le bouton dédié.
        Cette fonction fait appel à la classe Choix, qui permet d'afficher les
        Pokémons de l'équipe. Quand un Pokémon est KO, on l'enlève de la 
        liste des Pokémons de la carte et de la matrice des collisions, puis on
        l'ajoute à l'équipe et on le marque comme rencontré pour le Pokédex.

        Parameters
        ----------
        joueur : Joueur
            Le joueur initialisé plus tôt. Permet d'accéder à son équipe.
        """
        dlg = Choix(self)
        dlg.exec()
        
        #Mettre à jour le Pokémon actuel
        self.pokemon_actuel = joueur.team[0]
        self.HP_init_act = self.pokemon_actuel.HP

    def attack(self, joueur, attaque):
        """
        Lance les attaques, à la fois sur le Pokémon actuel et sur l'adversaire.
        Compare d'abord les vitesses des Pokémons, pour savoir qui agit en 
        premier.

        Parameters
        ----------
        joueur : Joueur
            Le joueur.
        attaque : str
            Permet de spécifier s'il s'agit d'une attaque spéciale ou normale.
            
        """
        #Type de l'attaque
        if attaque == "normal attack":
            atq = self.pokemon_actuel.attaque_norm
        else:
            atq = self.pokemon_actuel.attaque_spe
        
        #Quel Pokémon agit en premier ?
        v1 = self.pokemon_actuel.speed
        v2 = self.pokemon_adv.speed 
        if v1 > v2 :
            
            #Le Pokémon du joueur attaque en premier
            self.zone_a_edit.setText(f"{self.pokemon_actuel.nom} uses a "+attaque)
            hp_p2 = atq(self.pokemon_adv)
            
            #Pas de HP négatifs
            if hp_p2 < 0:
                self.pokemon_adv.HP = 0
            else:
                self.pokemon_adv.HP = hp_p2
            
            #Affichage des HP
            self.HP_adv.setText(f"HP {self.pokemon_adv.HP}/{self.HP_init_adv}")
            QtTest.QTest.qWait(1000)
            
            #Combat gagné ?
            if hp_p2 <= 0: 
                #Pokémon adverse KO
                self.zone_a_edit.setText("You caught " + self.pokemon_adv.nom + " !")
                QtTest.QTest.qWait(1000)
                liste_entites.remove_pokemon(self.pokemon_adv.position)
                matrice_collision[joueur.position[0]][joueur.position[1]].pop(0)
                joueur.team.append(self.pokemon_adv)
                liste_pokemon[self.pokemon_adv.id -1].rencontre = True
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
                    liste_pokemon[self.pokemon_adv.id -1].rencontre = True
                    self.close()
                    joueur.soigner_equipe()
                    
    def flee(self):
        """
        Permet de fuir du combat
        
        """
        self.zone_a_edit.setText("Ran away safely !")
        QtTest.QTest.qWait(1000)
        joueur.soigner_equipe()
        self.close()
        
       
        
        
class Choix(QDialog):

        
    def __init__(self, parent=None):
        """
        Permet d'initialiser la fenêtre de choix des Pokémons, en affichant les
        Pokémons de l'équipe et s'ils sont KO ou non.

        """
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
        """
        Permet de changer de Pokémon.

        Parameters
        ----------
        index : int
            Identifiant du Pokémon à supprimer de l'équipe.

        """
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
    