from EXO2 import *
from EXO3 import *

# Définition de la classe Couleur
class Couleur(object):
    # Initialisation avec les composantes rouge, vert et bleu de la couleur
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

# Définition de la classe Objet3D
class Objet3D(object):
    # Initialisation avec une liste de triangles, un centre et une couleur
    def __init__(self, triangles, center, color):
        self.triangles = triangles
        self.center = center
        self.color = color

    # Méthode pour afficher les coordonnées des points de chaque triangle
    def afficher(self):
        for triangle in self.triangles:
            for point in [triangle.c1, triangle.c2, triangle.c3]:
                print(f"{point.x},{point.y},{point.z}")

            print("\n")

    # Méthode pour ajouter un triangle à la liste de triangles
    def ajouterTriangle(self, triangle):
        self.triangles.append(triangle)

    # Méthode pour déplacer l'objet en fonction d'un vecteur passé en argument
    def move(self, vect):
        for triangle in self.triangles:
            triangle.deplacer(vect)