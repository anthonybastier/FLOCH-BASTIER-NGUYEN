# -*- coding: utf-8 -*-
"""
@authors: Anais, Anthony, Thomas
"""
####### Imports #######
from pokemons import *
import copy

####### Définition de la classe Joueur #######

class Joueur:
    def __init__(self, position = [5,5]):
        """
        Initialise le joueur, avec les trois starters de la 1ere génération.
        On les définit comme rencontrés, afin qu'ils apparaissent dans le 
        Pokédex comme tels.

        Parameters
        ----------
        position : tuple, optional
            Position de départ du personnage. Par défaut à [5,5].

        """
        
        self.position = position
        self.team = [copy.copy(liste_pokemon[0]),copy.copy(liste_pokemon[3]),copy.copy(liste_pokemon[6])]
        #Définition des pokémons de l'équipe comme attrapés
        liste_pokemon[0].rencontre = True
        liste_pokemon[3].rencontre = True
        liste_pokemon[6].rencontre = True
    
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
            #Récupère les HP max du Pokémon
            HP_max = liste_pokemon[pokemon.id-1].HP
            pokemon.HP = HP_max
