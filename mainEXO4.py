from EXO2 import*
from EXO3 import*
from EXO4 import*


def main():
    col = Couleur(100,255,155)
    centre = Vecteur(0.5,0.5,0.5)

    v1 = Vecteur(1,0,0)
    v2 = Vecteur(0,1,0)
    v3 = Vecteur(0,0,1)

    v4 = Vecteur(2,0,0)
    v5 = Vecteur(0,2,0)
    v6 = Vecteur(0,0,2)

    v7 = Vecteur(3,0,0)
    v8 = Vecteur(0,3,0)
    v9 = Vecteur(0,0,3)

    t1 = Triangle(v1,v2,v3)
    t2 = Triangle(v4,v5,v6)
    t3 = Triangle(v7,v8,v9)

    vd = Vecteur(1,0,0)

    obj = Objet3D([t1,t2],centre,col)

    obj.afficher()

    obj.ajouterTriangle(t3)

    obj.afficher()

    obj.move(vd)

    obj.afficher()


if __name__ == "__main__":
    main()
