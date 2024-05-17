# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:45:01 2024

@author: Thomas Thanh NGUYEN ANH TUAN

"""
import numpy as np
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtTest
from joueur import *
from pokemons import *



        

class Carte():
    def __init__(self,mainWindow):
        """
        on initialise la carte avec PyQt dans la fenetre en entree

        Parameters
        ----------
        mainWindow : la fenêtre PyQt dans laquelle la carte s affiche

        Returns
        -------
        None.

        """
        self.carte=QtWidgets.QLabel(mainWindow)
        self.carte.setGeometry(QtCore.QRect(0,0,2000,2000))
        self.carte.setText("")
        self.carte.setScaledContents(True)
        self.carte.setObjectName("carte")
        self.carte.setPixmap(QtGui.QPixmap("./data/pokemap.jpg"))
        self.mainWindow=mainWindow
    
    def move(self,direction):
        """
        déplace la map sous l avatar du joueur et anime l avatar

        Parameters
        ----------
        direction : TYPE str
            chaîne de caractere recuperee dans mainrunapp.py avec une methode Key Pressed Event

        Returns
        -------
        None.

        """
        
        pos=self.carte.geometry()
        

        if direction == "up":
            
            pos.translate(0,20)
            self.carte.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_back_walk1.png"))
            QtTest.QTest.qWait(50)
            
            pos.translate(0,20)
            self.carte.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_back_walk2.png"))
            QtTest.QTest.qWait(50)        
            
            pos.translate(0,10)
            self.carte.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_back.png"))


        if direction == "down":

            pos.translate(0,-20)
            self.carte.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_front_walk1.png"))
            QtTest.QTest.qWait(50)

            pos.translate(0,-20)
            self.carte.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_front_walk2.png"))
            QtTest.QTest.qWait(50)
            
            pos.translate(0,-10)
            self.carte.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_front.png"))

            
        if direction == "left":
            
            pos.translate(20,0)
            self.carte.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_left_walk1.png"))
            QtTest.QTest.qWait(50)

            pos.translate(20,0)
            self.carte.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_left_walk2.png"))
            QtTest.QTest.qWait(50)

            pos.translate(10,0)
            self.carte.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_left.png"))            
            

        if direction == "right":

            pos.translate(-20,0)
            self.carte.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_right_walk1.png"))
            QtTest.QTest.qWait(50)

            pos.translate(-20,0)
            self.carte.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_right_walk2.png"))
            QtTest.QTest.qWait(50)

            pos.translate(-10,0)
            self.carte.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_right.png"))





class Sprite():
    def __init__(self,mainWindow):
        """
        initialise l avatar du joueur au centre de la fenetre de jeu

        Parameters
        ----------
        mainWindow 
            fenetre dans laquelle on initialise l avatar

        Returns
        -------
        None.

        """
        self.sprite=QtWidgets.QLabel(mainWindow)
        self.sprite.setGeometry(250,250,50,50)
        self.sprite.setText("")
        self.sprite.setScaledContents(True)
        self.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_front.png"))
        self.sprite.setObjectName('player')
        self.mainWindow=mainWindow
    
    
    def move(self,direction):
        """
        deplace l avatar sur une carte fixe et anime l avatar pour le deplacement

        Parameters
        ----------
        direction : TYPE str
            chaine de caractere recuperee dans mainrunapp.py avec une methode Key Pressed Event

        Returns
        -------
        None.

        """
        pos=self.sprite.geometry()
        

        if direction == "up":
            
            pos.translate(0,-20)
            self.sprite.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_back_walk1.png"))
            QtTest.QTest.qWait(50)
            
            pos.translate(0,-20)
            self.sprite.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_back_walk2.png"))
            QtTest.QTest.qWait(50)        
            
            pos.translate(0,-10)
            self.sprite.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_back.png"))


        if direction == "down":

            pos.translate(0,20)
            self.sprite.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_front_walk1.png"))
            QtTest.QTest.qWait(50)

            pos.translate(0,20)
            self.sprite.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_front_walk2.png"))
            QtTest.QTest.qWait(50)
            
            pos.translate(0,10)
            self.sprite.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_front.png"))

            
        if direction == "left":
            
            pos.translate(-20,0)
            self.sprite.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_left_walk1.png"))
            QtTest.QTest.qWait(50)

            pos.translate(-20,0)
            self.sprite.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_left_walk2.png"))
            QtTest.QTest.qWait(50)

            pos.translate(-10,0)
            self.sprite.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_left.png"))            
            

        if direction == "right":

            pos.translate(20,0)
            self.sprite.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_right_walk1.png"))
            QtTest.QTest.qWait(50)

            pos.translate(20,0)
            self.sprite.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_right_walk2.png"))
            QtTest.QTest.qWait(50)

            pos.translate(10,0)
            self.sprite.setGeometry(pos)
            self.mainWindow.trainer.sprite.setPixmap(QtGui.QPixmap("./data/trainer/trainer_right.png"))
        
    

    
    
       

