# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:28:31 2024

@author: Anthony Bastier
"""

#Import des Pokemons
from pokemons import liste_pokemon

#Import des modules 
import random as rd

class Joueur:
    def __init__(self, position = (0,0), nb_pokemon = 1):
        """
        Initialise le joueur, avec au moins un pokémon choisi aléatoirement

        Parameters
        ----------
        position : tuple, optional
            Position de départ du personnage. Par défaut à (0,0).
        nb_pokemon : int
            Nombre de pokemons possédés au départ du jeu. Par défaut à 1.

        Returns
        -------
        None.

        """
        
        self.position = position
        self.team = [] #Liste des pokemons de départ
        
        for i in range(nb_pokemon):
            index = rd.randint(0,150) #Parmi les 151 pokemons
            self.team.append(liste_pokemon[index])
    
    def a_un_pokemon_non_ko(self):
        """
        Vérifie si au moins un Pokémon du joueur n'est pas KO.

        Returns
        -------
        bool
            True si au moins un Pokémon est non KO, False sinon.
        """

        for pokemon in self.team:
            if pokemon.HP != 0:
                return True
        return False

