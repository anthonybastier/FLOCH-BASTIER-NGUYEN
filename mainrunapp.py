# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:31:30 2024

@author: anais
"""

from testbutton import *
from joueur import *
from pokemons import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog



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
    mainWin = Combat()
    mainWin.show()
    app.exec_()
    
    
run_app()