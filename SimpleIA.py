import random


class SimpleIA:
    def __init__(self, mon_equipe , dictionnaires_unites):
         self.mon_equipe = mon_equipe
         self.mes_unites = dictionnaires_unites

    def jouer_tour(self , arbitre):
        for nom , unite in self.mes_unites.items():
            directions = [(0,1) , (0 ,-1) , (1,0) , (0,-1) , (1,1) ]
            dx , dy = random.choice(directions)
            arbitre.deplacer_unite(unite,dx,dy)