# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:45:01 2024

@author: Thomas Thanh NGUYEN ANH TUAN

"""
import numpy as np
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from joueur import *


class Carte():
    def __init__(self,mainWindow):
        self.carte=QtWidgets.QLabel(mainWindow)
        self.carte.setGeometry(QtCore.QRect(0,0,2000,500))
        self.carte.setText("")
        self.carte.setScaledContents(True)
        self.carte.setObjectName("carte")
        self.carte.setPixmap(QtGui.QPixmap("./data/pokemap.jpg"))
    
    def move(self,direction):
        pos=self.carte.geometry()
        
        if direction == "up":
            pos.translate(0,25)
            joueur.position[1]+=0.5

        if direction == "down":
            pos.translate(0,-25)
            joueur.position[1]-=0.5

        if direction == "left":
            pos.translate(-25,0)
            joueur.position[0]-=0.5

        if direction == "right":
            pos.translate(25,0)
            joueur.position[0]+=0.5

class Sprite():
    def __init__(self,mainWindow,spritePath):
        self.sprite=QtWidgets.QLabel(mainWindow)
        self.sprite.setGeometry(250,250,50,50)
        self.sprite.setText("")
        self.sprite.setScaledContents(True)
        self.sprite.setPixmap(QtGui.QPixmap(spritePath))
        self.sprite.setObjectName('player')
    
    
    
    
       

