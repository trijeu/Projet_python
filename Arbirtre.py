from classe_1 import Legionnaire
from UnitéParthes import UniteArchers
""" y a un soucis avec unites parthes il y a espace dans le non et ca rend difficile d importer"""

class Arbirtre:
    def __init__(self,taille_carte = 120):
        self.taille_carte = taille_carte
        self.unites_romaines = {"Legionnaire_1":Legionnaire(x=10,y =10)}
        self.unite_Parthe = {"Archer_1":UniteArchers(x=20,y=20)}

        def deplacer_unite(self, unite , dx , dy):
            nx = unite.x +dx
            ny = unite.y +dy
            if 0 <= nx < self.taille_carte and 0 <= ny < self.taille_carte:
                unite.x = nx
                unite.y = ny
                return True
            return False