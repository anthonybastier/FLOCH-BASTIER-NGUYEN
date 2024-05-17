# -*- coding: utf-8 -*-
"""
@authors: Anais, Anthony, Thomas
"""
####### Imports #######
import csv
import pandas as pd
import random as rd
import copy
import numpy as np

####### Définition de la classe Pokémon #######

class Pokemon():
    
    def __init__(self, id, nom, type, type2, HP, attack, defense, sp_atk, sp_def, speed, position, legendary = False, rencontre=False):
        """
        Initialise un Pokémon avec toutes ses caractéristiques, dont la 
        position et s'il a été rencontré ou non.

        Parameters
        ----------
        id : int
            Identifiant du Pokémon, de 1 à 151.
        nom : str
            Nom du Pokémon
        type : str
            Premier type du Pokémon.
        type2 : str
            Second type du Pokémon, s'il en possède un.
        HP : float
            Points de vie du Pokémon.
        attack : int
            Points d'attaque du Pokémon.
        defense : int
            Points de défense du Pokémon.
        sp_atk : int
            Points d'attaque spéciale du Pokémon.
        sp_def : int
            Points de défense spéciale du Pokémon.
        speed : int
            Vitesse du Pokémon.
        position : tuple
            Position x,y des Pokémons. Elle ne changera pas au cours du jeu.
        legendary : bool, optional
            Indique si le Pokémon est légendaire ou non. Par défaut à False.
        rencontre : bool, optional
            Indique si le Pokémon a déjà été capturé. Par défault à False.

        """
        self.id = id
        self.nom = nom
        self.type = type
        self.type2 = type2
        self.HP = int(HP)
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.position = position
        self.rencontre = rencontre
        self.legendary = legendary
         
    def attaque_norm(self, pokemon):
        """
        Attaque de type normale commune à tous les Pokémons.Vérifie les 
        Pokémons pour lesquels les dégats sont attenués, en fonction de leurs 
        type principal et secondaire, à l'aide des facteurs k et l.
        ----------
        pokemon : str
            Pokémon adversaire lors d'un combat.

        Returns
        -------
        int
            Le nombre d'HP restant au pokemon ayant subi les dégâts, 
            calculé avec ses statistiques et ses HP max.
        """
        
        degats = self.attack
        k = 1 #facteur multiplicatif pour le type 1
        l = 1 #facteur multiplicatif pour le type 2
        if pokemon.type == "Steel" or pokemon.type == "Rock" :
            k = 0.5
        elif pokemon.type == "Ghost" :
            k = 0
        if pokemon.type2 == "Steel" or pokemon.type2 == "Rock" :
            l = 0.5
        elif pokemon.type2 == "Ghost" :
            l = 0
        degats_attenues = pokemon.defense - k*l * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : 
            return pokemon.HP + degats_attenues
        
        
    def attaque_spe(self, pokemon):
        """
        Attaque spéciale propre au type du Pokémon. Regarde dans le tableau csv
        des types Pokémons les correspondances entre le type de l'attaque et 
        les types des Pokémons attaqués.
        ----------
        pokemon : str
            Pokémon adversaire lors d'un combat.

        Returns
        -------
        int
            Le nombre d'HP restant au Pokémon ayant subi les dégâts, 
            calculé avec ses statistiques et ses HP max.
        """
        
        degats = self.sp_atk
        k = 1 #facteur multiplicatif pour le type 1
        l = 1 #facteur multiplicatif pour le type 2
        types = pd.read_csv(r"data\types.csv", index_col=0)
        k = types.loc[self.type, pokemon.type] #Trouve le facteur correspondant aux types dans le tableau des affinités
        if pokemon.type2 != "":
            l = types.loc[self.type, pokemon.type2] #De même avec le second type
        degats_attenues = pokemon.sp_def - k*l * degats
        if degats_attenues > 0 :
            return pokemon.HP - degats_attenues
        else : 
            return pokemon.HP + degats_attenues
        
    
    def choix_attaque(self):
        """
        Renvoie un choix aléatoire d'attaque ; utilisé par les Pokémons 
        adverses sur le Pokémon du joueur.

        Returns
        -------
        function
            Attaque aléatoire parmi attaque normale et attaque spéciale.

        """
        attaques = [self.attaque_norm, self.attaque_spe]
        return rd.choice(attaques)
    

####### Définition des listes de Pokémons #######
    
class Generation1:
    
    def __init__(self, nomfichier):
        """
        Permet d'obtenir la liste de tous les Pokemons de la première génération
        en les définissant comme tels avec leurs valeurs attribuées. La position 
        des Pokémons est initialisée à (0,0).
        
        Parameters
        ----------
        nomfichier : str
            Fichier contenant la liste de tous les Pokémons de la 1ère génération.

        """
        self.liste = []
        with open(nomfichier, encoding='utf-8', mode ='r') as file: #utf-8 permet de différencier Nidoran mâle et femelle
            csvFile = csv.reader(file)
            next(csvFile)
            
            for row in csvFile: #faire correspondre les colonnes du csv aux caractéristiques de la classe pour chaque pokemon
                a, b, c, d, e, f, g, h, i, j, k = (int(row[0]), str(row[1]), str(row[2]),str(row[3]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), row[12])
                creature = Pokemon(a, b, c, d, e, f, g, h, i, j, (0,0), k)
                self.liste.append(creature)
    
    def __getitem__(self, ind):
        """
        Surcharge de méthode ; permet de récupérer le i-ème pokémon de la 
        1ère génération.

        Parameters
        ----------
        ind : int
            Identifiant du Pokémon de 1 à 151.

        Returns
        -------
        Pokemon
            Pokémon correspondant de type "Pokemon"

        """
        return self.liste[ind]
    
    def __str__(self):
        """
        Surcharge de méthode ; permet d'afficher la liste des 151 Pokémons de 
        la 1ère génération.

        Returns
        -------
        txt : str
            Chaine de caractères contenant l'ensemble des Pokémons.

        """
        txt = ""
        for i in range(151) : 
            txt += str(self.liste[i].nom) + "\n"
        return txt
        
             
liste_pokemon = Generation1(r"data\pokemon_first_gen.csv")

class Entites:
    
    def __init__(self, nomfichier, liste_pokemon):
        """
        Permet d'obtenir la liste des Pokemons positionnés sur la carte. Utilise
        la liste des Pokémons de la première génération pour obtenir leurs 
        attributs puis ajoute la position.

        Parameters
        ----------
        nomfichier : str
            Nom du fichier contenant les noms des Pokémons ainsi que leur position.
        liste_pokemon : Generation1
            Liste des 151 Pokémons avec leurs attributs.

        """
        self.liste = []
        with open(nomfichier, encoding='utf-8', mode ='r') as file:
            csvFile = csv.reader(file)
            next(csvFile)
            
            for row in csvFile:
                nom, position_string = row[0], row[1]  # Extraire le nom et la position
                pos = tuple(map(float, position_string.replace("[", "").replace("]", "").split(", ")))
                
                #Copie des caractéristiques du Pokémon, pour ensuite ajouter sa position
                creature = copy.copy(next((pokemon for pokemon in liste_pokemon if pokemon.nom == nom), None))
                creature.position = pos
                self.liste.append(creature)
                
    def __getitem__(self, ind):
        """
        Surcharge de méthode ; permet de récupérer le i-ème pokémon de la 
        liste des Pokémons présents sur la carte.

        Parameters
        ----------
        ind : int
            Identifiant du Pokémon de 0 à 997.

        Returns
        -------
        Pokemon
            Pokémon correspondant de type "Pokemon"

        """
        return self.liste[ind]
    
    def remove_pokemon(self, pos):
        """
        Supprime un Pokémon de la liste des entités à partir de sa position 
        sur la carte.

        Parameters
        ----------
        position : (tuple)
            La position du Pokémon à supprimer.

        """

        for i in range(len(self.liste)-1):
            if self.liste[i].position == pos:
                self.liste.pop(i)         
    
    def __str__(self):
        """
        Surcharge de méthode ; permet d'afficher la liste des Pokémons présents
        sur la carte.

        Returns
        -------
        txt : str
            Chaine de caractères contenant l'ensemble des Pokémons.

        """
        txt = ""
        for i in range(998) : 
            txt += str(self.liste[i].nom) + "\n"
        return txt

liste_entites = Entites(r"data\pokemon_coordinates.csv",liste_pokemon)


####### Construction de la matrice de collision #######
"""
On construit la matrice de collision du jeu par projection des positions des 
Pokémons sur une grille 40x40.
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