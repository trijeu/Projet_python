from unite import Unite

class Battlefield :
    def __init__(self) :
        self.largeur= 120
        self.hauteur= 120
        self.unites= []
        self.obstacles= []
        self.castle = None


    def ajouter_unite(self,unite: Unite) :
        self.unites.append(unite)


    def supprimer_unite(self, unite: Unite) :
        if unite in self.unites :
            self.unites.remove(unite)


    def get_alive_units(self):
        return [u for u in self.unites if u.is_alive]


    def get_units_by_team(self, team):
        return [u for u in self.unites if u.team == team and u.is_alive]

