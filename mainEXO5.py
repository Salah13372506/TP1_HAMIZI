from EXO5 import *


def main():
    # Création des joueurs
    j1 = Joueur("Joueur 1")
    j2 = Joueur("Joueur 2")

    nbTour = 3

    # Initialisation du jeu et lancement des tours
    jeu = Jeu([j1, j2], nbTour)
    jeu.lancer_tour()

if __name__ == "__main__":
    main()