# Pokémon: projet informatique

# Mode d'emploi du GIT FLOCH-BASTIER-NGUYEN

* Présentation
- Bienvenue dans Pookemon, le but de ce jeu est de remplir le Pokedex en attrapant les 151 Pokémons, cela se fait en parcourant le monde où sont cachés des pokemons sauvages et en les battant !

* Comment démarrer le jeu ?
- Ouvrez le fichier main.py 
- Lancer le jeu avec F5
- Votre avatar est situé dans le coin supérieur gauche de la carte (40x40) et vous commencez avec une équipe composée de 3 Pokémons Bulbasaur, Charmander et Squirtle

* Comment jouer dans le monde ?
- Se déplacer avec les flèches directionnelles du clavier (input par input, ne pas rester appuyé)
- Arriver sur une case contenant un Pokémon caché déclanche un combat
- Les cases peuvent ne pas contenir de Pokémon ou bien en contenir plusieurs, ce nombre est fixe donc il est possible de vider toutes les cases

* Déroulement d'un combat
- Cliquer sur "Flee" pour fuire le combat
- Pour changer de Pokemon, cliquer sur "Pokemon" pour accéder à l'équipe actuelle du joueur
- Pour attaquer, cliquer sur "Attack" ou "Special Attack"
- Lorsque le pokemon adverse tombe à 0HP, il est attrapé
- Si le pokemon de la team tombe à 0HP, le joueur est invité à choisir un autre pokemon
- Si tous les pokemon de l'équipe ont été vaincus, le joueur sort du combat et ses pokemons sont soignés

* Fonctionnement du Pokedex
- Appuyer sur la touche "P" pour accéder au pokedex et pour le fermer
Au début de la partie, le Pokedex ne sera composé que des 3 Pokémons de départ, le reste de la fenêtre est blanc. Au fur et à mesure que des Pokemon sont rencontrés, ils seront ajoutés au Pokedex.

* Informations importantes :
- Tous les pokemon attrapés deviennent jouables 
- A chaque fin de combat tous les pokemon de l'équipe sont soignés

* Versions :
Python 3.8.10
PyQt5 5.15.10



