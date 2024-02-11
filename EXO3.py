import EXO2


class Triangle(object):
    def __init__(self,vect1,vect2,vect3):
        self.c1 = vect1
        self.c2 = vect2
        self.c3 = vect3
    
    def tournerTriangle(self,alpha):
        self.c1 = EXO2.tourner(alpha)
        self.c2 = EXO2.tourner(alpha)
        self.c3 = EXO2.tourner(alpha)   
    
    def afficherTriangle(self):
        print(f"{self.c1.x},{self.c1.y},{self.c1.z}")
        print(f"{self.c2.x},{self.c2.y},{self.c2.z}")
        print(f"{self.c3.x},{self.c3.y},{self.c3.z}")
    
    def deplacer(self,vect):
        self.c1 = self.c1.additionner(vect)
        self.c2 = self.c2.additionner(vect)
        self.c3 = self.c3.additionner(vect)


def main():
    v1 = EXO2.Vecteur(1,0,0)
    v2 = EXO2.Vecteur(0,1,0)
    v3 = EXO2.Vecteur(0,0,1)

    vd = EXO2.Vecteur(1,0,0)

    t = Triangle(v1,v2,v3)

    t.afficherTriangle()

    t.deplacer(vd)

    print("\n")

    t.afficherTriangle()

if __name__ == "__main__":
    main()