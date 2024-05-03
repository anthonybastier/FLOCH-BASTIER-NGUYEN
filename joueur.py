# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:28:31 2024

@author: Anthony Bastier
"""

#Import des Pokemons
from startpokemon import liste_pokemon

#Import des modules 
import numpy as np

class joueur:
    def __init__(self, position = (0,0), champ_vision = 3, nb_pokemon = 1):
        """
        Initialise le joueur, avec 

        Parameters
        ----------
        position : tuple, optional
            Position de départ du personnage. Par défaut à (0,0).
        champ_vision : int
            Champ de vision du personnage, i.e distance à partir de laquelle on découvre les pokémons. Par défaut à 3.
        nb_pokemon : int
            Nombre de pokemons possédés au départ du jeu. Par défaut à 1.

        Returns
        -------
        None.

        """
        
        self.position = position
        self.champ_vision = champ_vision
        self.pokemons = [] #Liste des pokemons de départ
        
        for i in range(nb_pokemon):
            index = rd.randint(0,150) #Parmi les 151 pokemons
            self.pokemon.append(liste_pokemon[index])
            

    