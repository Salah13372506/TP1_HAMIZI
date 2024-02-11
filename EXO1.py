# Classe Algebre
class Algebre(object):
    def __init__(self):
        pass

    # Méthode pour calculer la somme des entiers de 1 à n
    def calculEntier(self,n):
        res = 0
        for i in range(0,n+1):
            res += i
        return res
    
    # Méthode pour calculer la factorielle de n
    def factorielle(self,n):
        res = 1
        for i in range(1,n):
            res *= i
        return res