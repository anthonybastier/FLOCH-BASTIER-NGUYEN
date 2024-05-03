# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:23:44 2024

@author: anais
"""
import matplotlib.pyplot as plt
import numpy as np
import csv
from abc import abstractmethod

######################################################################################################

class Pokemon():
    def __init__(self, id, nom, type, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        self.id = id
        self.nom = nom
        self.type = type
        self.HP = int(HP)
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.position = position
        self.legendary = legendary
         
    def attaque_norm(self, pokemon):
        #vérifier le type du pokemon adverse quand même exemple normal nul face à ghost
        pass
        
    @abstractmethod
    def attaque_spe(self, pokemon):
        #pokemon1.attaque_spe(pokemon2)
        pass
    
######################################################################################################
################################################TYPES#################################################
######################################################################################################
    
class Plante(Pokemon):
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        pass
        
######################################################################################################    
    
class Generation1:
    "Permet d'obtenir la liste de tous les pokemon en les définissant comme tels avec leurs valeurs attribuées"
    #liste_pokemon = Generation1(r"C:\Users\anais\projetPokemon\data\pokemon_first_gen.csv")
    def __init__(self, nomfichier):
        self.liste = []
        with open(nomfichier, encoding='utf-8', mode ='r') as file: #utf-8 permet de différencier Nidoran mâle et femelle
            csvFile = csv.reader(file)
            next(csvFile)
            for row in csvFile: #faire correspondre les colonnes du csv aux caractéristiques de la classe pour chaque pokemon
                a, b, c, d, e, f, g, h, i, j = (int(row[0]), str(row[1]), str(row[2]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), bool(row[12]))
                creature = Pokemon(a, b, c, d, e, f, g, h, i, j)
                self.liste.append(creature)
                
    def __str__(self):
        txt = ""
        for i in range(151) : 
            txt += str(self.liste[i].nom) + "\n"
        return txt
        
             
liste_pokemon = Generation1(r"C:\Users\anais\projetPokemon\data\pokemon_first_gen.csv")
