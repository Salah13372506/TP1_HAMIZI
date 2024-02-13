from random import randint

class De(object):
    def __init__(self):
        pass
    
    def lancer(self):
        # Génère un nombre aléatoire entre 1 et 6, pour simuler la lancé d'un dé
        return randint(1, 6)

class Joueur(object):
    def __init__(self, nom):
        self.nom = nom  

    def tout_lancer(self, des):
        res = []
        # Boucle qui retourne le résultat du lancer de tous les dés du joueur lors de chaque début de tour
        for i in range(len(des)):
            res.append(des[i].lancer())
        return res

    def lancer_des(self, des, ind):
        # Lance un dé spécifique du joueur et retourne le résultat
        return des[ind].lancer()

class Jeu(object):
    def __init__(self, joueurs, tour):
        self.joueurs = joueurs  # Liste des joueurs
        self.des = [De() for _ in range(3)]  # Liste des dés utilisés dans le jeu
        self.tour = tour        # Nombre de tours

    def lancer_tour(self):
        for i in range(self.tour):
            # Pour chaque tour
            for joueur in self.joueurs:
                print(f"{joueur.nom} lance les dés...")
                # Lancer tous les dés au début du tour
                res = joueur.tout_lancer(self.des)
                print("Résultats avant relance:", res)

                # Demander au joueur quels dés il souhaite relancer
                choix = input("Indiquez les dés à relancer (ex: '1 2', '0' pour ne rien relancer) : ")

                if choix.strip() == "0":
                    print("Vous ne relancez aucun dé.")
                else:
                    # Convertir l'entrée en une liste d'indices de dés à relancer
                    des_a_relancer = [int(i) - 1 for i in choix.split()]
                    for ind in des_a_relancer:
                        # Relancer chaque dé choisi par le joueur
                        res[ind] = joueur.lancer_des(self.des, ind)
                    print("Résultats après relance:", res)

                # Analyser les résultats et attribuer des points au joueur
                points = self.analyser_resultat(res)
                print(f"Points obtenus pour {joueur.nom}: {points}")
                print("\n")

    def analyser_resultat(self, res):
        # Analyse les résultats des dés et calcule les points obtenus
        points = 0
        if 4 in res and 2 in res and 1 in res:
            points += 10
        if res.count(1) == 2:
            points += res[res.index(1) - 1]  # Ajoute la valeur du troisième dé
        if len(set(res)) == 3 and max(res) - min(res) == 2:
            points += 2
        return points

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
