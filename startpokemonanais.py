# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:23:44 2024

@author: anais
"""

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
        
    @abstractmethod
    def attaque_spe(self, pokemon):
        #pokemon1.attaque_spe(pokemon2)
        pass
    
######################################################################################################
################################################TYPES#################################################
######################################################################################################

"""Définitions des types et leurs attaques spéciales associées, avec leurs forces et faiblesses associées"""
 
class Steel(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Fairy" or pokemon.type == "Rock" or pokemon.type == "Ice" :
            k = 2 
        elif pokemon.type == "Steel" or pokemon.type == "Water" or pokemon.type == "Fire" or pokemon.type == "Electric" :
            k = 0.5
            
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP

 
class Fighting(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Steel" or pokemon.type == "Rock" or pokemon.type == "Ice" or pokemon.type == "Normal" :
            k = 2 
        elif pokemon.type == "Psychic" or pokemon.type == "Bug" or pokemon.type == "Fairy" or pokemon.type == "Poison" or pokemon.type == "Flying" :
            k = 0.5
            
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
  
    
class Dragon(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Dragon" :
            k = 2 
        elif pokemon.type == "Steel" :
            k = 0.5
        elif pokemon.type == "Fairy":
            k = 0
            
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
    
    
class Water(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Fire" or pokemon.type == "Rock" or pokemon.type == "Ground" :
            k = 2 
        elif pokemon.type == "Dragon" or pokemon.type == "Water" or pokemon.type == "Plant" :
            k = 0.5
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
    
    
class Electric(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Water" or pokemon.type == "Flying" :
            k = 2 
        elif pokemon.type == "Dragon" or pokemon.type == "Electric" or pokemon.type == "Plant" :
            k = 0.5
        elif pokemon.type == "Ground":
            k = 0
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
    
    
class Fire(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Plant" or pokemon.type == "Steel" or pokemon.type == "Ice" or pokemon.type == "Bug" :
            k = 2 
        elif pokemon.type == "Water" or pokemon.type == "Dragon" or pokemon.type == "Fire" or pokemon.type == "Rock" :
            k = 0.5
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
    
    
class Fairy(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Fighting" or pokemon.type == "Dragon":
            k = 2 
        elif pokemon.type == "Steel" or pokemon.type == "Fire" or pokemon.type == "Poison" :
            k = 0.5
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
   
    
class Ice(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Plant" or pokemon.type == "Dragon" or pokemon.type == "Ground" or pokemon.type == "Flying" :
            k = 2 
        elif pokemon.type == "Water" or pokemon.type == "Steel" or pokemon.type == "Fire" or pokemon.type == "Ice" :
            k = 0.5
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
    
    
class Bug(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Plant" or pokemon.type == "Psychic" :
            k = 2 
        elif pokemon.type == "Fighting" or pokemon.type == "Steel" or pokemon.type == "Fire" or pokemon.type == "Fairy" or pokemon.type == "Poison" or pokemon.type == "Ghost" or pokemon.type == "Flying":
            k = 0.5
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
  
    
class Normal(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Ghost" :
            k = 0 
        elif pokemon.type == "Rock" or pokemon.type == "Steel" :
            k = 0.5
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP


class Plant(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Water" or pokemon.type == "Rock" or pokemon.type == "Ground" :
            k = 2 
        elif pokemon.type == "Steel" or pokemon.type == "Dragon" or pokemon.type == "Fire" or pokemon.type == "Bug" or pokemon.type == "Plant" or pokemon.type == "Poison" or pokemon.type == "Flying" :
            k = 0.5
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
    
    
class Poison(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Fairy" or pokemon.type == "Plant" :
            k = 2 
        elif pokemon.type == "Poison" or pokemon.type == "Rock" or pokemon.type == "Ground" or pokemon.type == "Ghost" :
            k = 0.5
        elif pokemon.type == "Steel" :
            k = 0
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
        
 
class Psychic(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Fighting" or pokemon.type == "Poison" :
            k = 2 
        elif pokemon.type == "Psychic" or pokemon.type == "Steel" :
            k = 0.5
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
    
    
class Rock(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Fire" or pokemon.type == "Ice" or pokemon.type == "Bug" or pokemon.type == "Flying" :
            k = 2 
        elif pokemon.type == "Steel" or pokemon.type == "Fighting" or pokemon.type == "Ground" :
            k = 0.5
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
    
    
class Ground(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Fire" or pokemon.type == "Steel" or pokemon.type == "Electric" or pokemon.type == "Poison" or pokemon.type == "Rock":
            k = 2 
        elif pokemon.type == "Bug" or pokemon.type == "Plant" :
            k = 0.5
        elif pokemon.type == "Flying" :
            k = 0
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP


class Ghost(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Psychic" or pokemon.type == "Ghost" :
            k = 2 
        elif pokemon.type == "Normal" :
            k = 0
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP
    
    
class Flying(Pokemon):
    
    
    def __init__(self, id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False):
        super().__init__(id, nom, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False)
        
    def attaque_spe(self, pokemon):
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif
        if pokemon.type == "Fighting" or pokemon.type == "Bug" or pokemon.type == "Plant" :
            k = 2 
        elif pokemon.type == "Steel" or pokemon.type == "Electric" or pokemon.type == "Rock" :
            k = 0.5
        
        degats_attenues = pokemon.sp_def - k * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : return pokemon.HP


    
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
    
    def __getitem__(self, ind):
        return self.liste[ind]
    
    def __str__(self):
        txt = ""
        for i in range(151) : 
            txt += str(self.liste[i].nom) + "\n"
        return txt
        
             
liste_pokemon = Generation1(r"data\pokemon_first_gen.csv")
