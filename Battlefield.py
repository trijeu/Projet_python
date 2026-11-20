from Unite import Unite
from math import hypot

class Battlefield :
    def __init__(self) :
        self.largeur= 120
        self.hauteur= 120
        self.unites = []
        self.unites_romaines = []
        self.unites_parthes = []
        self.obstacles= []
        self.castle = None


    def ajouter_unite(self,unite: Unite) :
        self.unites.append(unite)


    def supprimer_unite(self, uid: int) :
        for u in self.unites :
            if u.uid == uid :
                self.unites.remove(u)
                break


    def get_alive_units(self):
        return [u for u in self.unites if u.is_alive]


    def get_units_by_team(self, team: str):
        return [u for u in self.unites if u.team == team and u.is_alive]

#méthode interne: utiliser position_libre()
    def est_dans_limites(self, x, y, radius = 0) -> bool: # Vérifie si l'unité est dans les limites de la map
        demi_hauteur = self.hauteur / 2
        demi_largeur = self.largeur / 2
        return (
                 -demi_largeur + radius <= x <= demi_largeur - radius
        and
        -demi_hauteur + radius <= y <= demi_hauteur - radius
    )


    def position_libre(self, unite, x, y) -> bool: # Vérifie si l'emplacement visé par l'unité est libre (hitbox des autres)
        if not self.est_dans_limites(x, y, unite.radius):
            return False

        for autre in self.unites:
            if autre is unite or not autre.is_alive:
                continue

            distance = hypot(autre.x - x, autre.y - y)

            if distance < unite.radius + autre.radius:
                return False
        return True


    def get_unite(self, uid):
        return next(
            (u for u in self.unites if u.uid == uid),
            None
        )
    