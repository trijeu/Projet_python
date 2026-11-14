from UniteParthes import UniteArchers
from UniteRomaine import Legionnaire

class Arbirtre:
    def __init__(self,taille_carte = 120):
        self.taille_carte = taille_carte
        self.tour = 0

    def deplacer_unite(self, unite , dx , dy):
        nx = unite.x +dx
        ny = unite.y +dy
        if 0 <= nx < self.taille_carte and 0 <= ny < self.taille_carte:
            unite.x = nx
            unite.y = ny
            return True
        return False

    def partie_terminee(self):
        if not self.unites_Parthe:
            return "Romains"
        if not self.unites_romaines:
            return ("Parthes")
        return None