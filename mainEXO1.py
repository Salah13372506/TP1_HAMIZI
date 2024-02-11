from EXO1 import *
import sys

def main():
    algebre = Algebre()
    
    if len(sys.argv) != 3:
        print("Usage: python programme.py <nombre_entier> <nombre_entier>")
        return
    
    n = int(sys.argv[1])

    somme = algebre.calculEntier(n)
    print(f"La somme des {n} premiers entiers est : {somme}")

    n = int(sys.argv[2])
    facto = algebre.factorielle(n)
    print(f"La factorielle de {n} est égale à {facto}")

if __name__ == "__main__":
    main()
