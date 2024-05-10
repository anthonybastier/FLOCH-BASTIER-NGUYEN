# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:23:44 2024

@author: anais
"""

import csv
import pandas as pd

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
        """
        Attaque  de type normale commune à tous les pokemon.
        ----------
        pokemon : string
            Pokemon adversaire lors d'un combat.

        Returns
        -------
        int
            Le nombre d'HP restant au pokemon ayant subi les dégâts.
        """
        
        degats = self.attack
        k = 1 #facteur multiplicatif
        if pokemon.type == "Steel" or pokemon.type == "Rock" :
            k = 0.5
        elif pokemon.type == "Ghost" :
            k = 0
        degats_attenues = pokemon.defense - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
        
        
    def attaque_spe(self, pokemon):
        """
        Attaque spéciale propre au type du pokemon.
        ----------
        pokemon : string
            Pokemon adversaire lors d'un combat.

        Returns
        -------
        int
            Le nombre d'HP restant au pokemon ayant subi les dégâts.
        """
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        types = pd.read_csv("data\types.csv", index_col=0)
        k = types.loc[self.type, pokemon.type] #Trouve le facteur k correspondant aux types

        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
    
    
######################################################################################################    
    
class Generation1:
    
    "Permet d'obtenir la liste de tous les pokemon en les définissant comme tels avec leurs valeurs attribuées"
    
    def __init__(self, nomfichier):
        self.liste = []
        with open(nomfichier, encoding='utf-8', mode ='r') as file: #utf-8 permet de différencier Nidoran mâle et femelle
            csvFile = csv.reader(file)
            next(csvFile)
            
            for row in csvFile: #faire correspondre les colonnes du csv aux caractéristiques de la classe pour chaque pokemon
                a, b, c, d, e, f, g, h, i, j = (int(row[0]), str(row[1]), str(row[2]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), bool(row[12]))
                creature = Pokemon(a, b, c, d, e, f, g, h, i, j)
                self.liste.append(creature)
    
    def __getitem__(self, ind):
        return self.liste[ind]
    
    def __str__(self):
        txt = ""
        for i in range(151) : 
            txt += str(self.liste[i].nom) + "\n"
        return txt
        
             
liste_pokemon = Generation1(r"data\pokemon_first_gen.csv")
