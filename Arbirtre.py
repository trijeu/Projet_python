import UniteRomaine
import UniteParthes

class Arbirtre:
    def __init__(self,battlefield):
        self.battlefield = battlefield
        self.taille_carte = battlefield.largeur
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
        romains_vivants = [ u for u in self.battlefield.get_units_by_team("romain") if u.is_alive]
        parthes_vivants = [ u for u in self.battlefield.get_units_by_team("parthes") if u.is_alive]
        if not parthes_vivants:
            return "Romains"
        if not romains_vivants:
            return "Parthes"
        return None