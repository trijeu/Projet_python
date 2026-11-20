import random

from Battlefield import Battlefield


class SimpleIA:
    def __init__(self, mon_equipe):
         self.mon_equipe = mon_equipe

    def jouer_tour(self , arbitre):
        mes_unites = [ u for u in arbitre.battlefield.get_units_by_team(self.mon_equipe) if u.is_alive]
        if not mes_unites:
            return
        directions = [(0,1) , (0 ,-1) , (1,0) , (0,-1) , (1,1) ]
        dx , dy = random.choice(directions)
        for unite in mes_unites:
            arbitre.deplacer_unite(unite , dx , dy)