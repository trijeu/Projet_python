from Unite import Unite
from Battlefield import Battlefield

class Arbirtre:
    def __init__(self,battlefield:Battlefield):
        self.battlefield = battlefield
        self.tour = 0
    def deplacer_unite(self, unite , dx , dy):
        nx = unite.x +dx
        ny = unite.y +dy
        if 0 <= nx < self.battlefield.largeur and 0 <= ny < self.battlefield.hauteur:
            unite.x = nx
            unite.y = ny
            return True
        return False
    def partie_terminee(self):
        romains_vivants = [ u for u in self.battlefield.get_units_by_team("romain") if u.is_alive]
        parthes_vivants = [ u for u in self.battlefield.get_units_by_team("parthe") if u.is_alive]
        if not parthes_vivants:
            return "Romains"
        if not romains_vivants:
            return "Parthes"
        return None