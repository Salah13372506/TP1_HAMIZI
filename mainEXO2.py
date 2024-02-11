from EXO2 import *
from math import sqrt


def main():
    v1 = Vecteur(1, 2, 3)
    v2 = Vecteur(4, 5, 6)

    # Test de la méthode vectNul
    v_nul = v1.vectNul()
    print("Vecteur nul:", end=" ")
    v_nul.afficher()

    # Test de la méthode additioner
    somme = v1.additionner(v2)
    print("Somme des vecteurs:")
    somme.afficher()

    # Test de la méthode calculerNorme
    norme_v1 = v1.calculerNorme()
    print("Norme du vecteur v1:", norme_v1)

    # Test de la méthode calculerProduitScalaire
    produit_scalaire = v1.calculerProduitScalaire(v2)
    print("Produit scalaire de v1 et v2:", produit_scalaire)

    # Test de la méthode tourner
    v_rotated = v1.tourner(math.pi/2)
    print("Vecteur v1 après rotation de pi/2:")
    v_rotated.afficher()

    
if __name__ == "__main__":
    main()