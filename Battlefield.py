from Unite import Unite

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


    def est_dans_limites(self, x, y) -> bool: # Vérifie si l'unité est dans les limites de la map
        bordure = self.largeur /2
        return (-bordure < x < bordure) and (-bordure < y < bordure)


    def position_libre(self, x, y): # Vérifie si l'emplacement visé par l'unité est libre (hitbox des autres)
        for i in self.unites:
            lim = i.radius  /2
            if i.x - lim < x < i.x + lim or i.y - lim < y < i.y + lim:
                return False
        return True
        
    