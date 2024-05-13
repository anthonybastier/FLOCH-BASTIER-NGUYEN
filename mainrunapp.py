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
        self.Button_Pokemon.clicked.connect(self.Chgt_pokemon)
        self.Button_attack.clicked.connect(self.attack_norm)
        self.Button_attack_spe.clicked.connect(self.attack_spe)
        self.Button_flee.clicked.connect(self.flee)
        
    def Chgt_pokemon(self):
        dlg = Choix(self)
        dlg.exec()
        
    def attack_norm(self, pokemon):
        pass
    
    def attack_spe(self,pokemon):
        pass
    
    def flee(self):
        pass
        
        
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