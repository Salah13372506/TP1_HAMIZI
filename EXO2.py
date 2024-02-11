from math import sqrt
import math

class Vecteur(object):
    # Initialisation avec les coordonnées x, y et z du vecteur
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Méthode pour créer un vecteur nul
    def vectNul(self):
        return Vecteur(0, 0, 0)

    # Méthode pour additionner deux vecteurs
    def additionner(self, vect):
        x = self.x + vect.x
        y = self.y + vect.y
        z = self.z + vect.z

        return Vecteur(x, y, z)
    
    # Méthode pour calculer la norme du vecteur
    def calculerNorme(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    # Méthode pour calculer le produit scalaire avec un autre vecteur
    def calculerProduitScalaire(self, vect):
        x = self.x * vect.x
        y = self.y * vect.y
        z = self.z * vect.z

        return (x + y + z)
    
    # Méthode pour effectuer une rotation du vecteur autour de l'axe z d'un angle alpha
    def tourner(self, alpha):
        # Calcul des coordonnées après la rotation
        x_rot = self.x * math.cos(alpha) - self.y * math.sin(alpha)
        y_rot = self.x * math.sin(alpha) + self.y * math.cos(alpha)
        
        # Retourner le vecteur après la rotation
        return Vecteur(x_rot, y_rot, self.z)   

    # Méthode pour afficher les coordonnées du vecteur
    def afficher(self):
        print(f"Coordonnées du vecteur: ({self.x}, {self.y}, {self.z})")
