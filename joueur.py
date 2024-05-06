# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:28:31 2024

@author: Anthony Bastier
"""

#Import des Pokemons
from startpokemonanais import liste_pokemon, Pokemon

#Import des modules 
import random as rd

class joueur:
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
            self.pokemon.append(liste_pokemon[index])
    
    def combat(self, pokemon_adv):
        """
        Un combat se joue au "tour par tour" : un pokémon effectue une action, 
        puis c'est au pokémon adverse d'effectuer une action et ainsi de suite.
        Les actions du pokémon adverse sont aléatoires.
        Le pokémon qui a la vitesse la plus élevée attaque en premier. 
        Les attaques infligent un nombre de dégâts déterminé 
        par les affinités de types et les statistiques attaque et défense 
        des pokémons.
        Lors de son tour, l'utilisateur choisit parmi plusieurs actions: 
            – attaquer,
            – changer de pokemon, 
            – fuir 
        Le combat s'arrête soit lorsque l'un des pokémon est KO, soit à la 
        suite d'une fuite du joueur.

        Parameters
        ----------
        pokemon : Pokemon
            Pokemon contre qui le joueur combat.

        Returns
        -------
        None.

        """
        pokemon_actuel = self.equipe[0]
        fuite = False
        while pokemon_adv.HP > 0 and pokemon_actuel.HP > 0 and not(fuite):
            
            #Action
            action = ""
            while(True):
                try:
                    action = input("What will you do ?")
                    assert(action in ["Fight","Switch Pokemon", "Flee"])
                    if len(self.equipe) == 1:
                        print("Unable to switch !")
                    break
                except (AssertionError):
                    print("Choose an action from : Fight, Switch Pokemon, Flee")
                    
            if action == "Flee":
                fuite = True
            
            if action == "Switch Pokemon":
                print ("Pokemon in your team :")
                print()
            

    