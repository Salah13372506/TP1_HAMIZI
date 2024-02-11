from EXO3 import *
from EXO2 import *


def main():
    v1 = Vecteur(1,0,0)
    v2 = Vecteur(0,1,0)
    v3 = Vecteur(0,0,1)

    vd = EXO2.Vecteur(1,0,0)

    t = Triangle(v1,v2,v3)

    t.afficherTriangle()

    t.deplacer(vd)

    print("\n")

    t.afficherTriangle()

if __name__ == "__main__":
    main()