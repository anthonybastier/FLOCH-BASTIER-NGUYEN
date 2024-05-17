# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:28:31 2024

@author: Anthony Bastier
"""

#Import des Pokemons
from pokemons import *

#Import des modules 
import random as rd
import copy

class Joueur:
    def __init__(self, position = [5,5]):
        """
        Initialise le joueur, avec les trois starters de la 1ere génération.

        Parameters
        ----------
        position : tuple, optional
            Position de départ du personnage. Par défaut à (0,0).
        Returns
        -------
        None.

        """
        
        self.position = position
        self.team = [copy.copy(liste_pokemon[0]),copy.copy(liste_pokemon[3]),copy.copy(liste_pokemon[6])]
        #Définition des pokémons de l'équipe comme attrapés
        self.team[0].rencontre = True
        self.team[1].rencontre = True
        self.team[2].rencontre = True
    
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

    def soigner_equipe(self):
        """
        Soigne tous les Pokémons du joueur.
        
        """

        for pokemon in self.team:
            # Récupérer le HP max du Pokémon
            HP_max = liste_pokemon[pokemon.id-1].HP
            # Soigner le Pokémon
            pokemon.HP = HP_max
