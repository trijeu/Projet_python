import random
import Battlefield
import Unite


class SimpleIA:
    def __init__(self, liste_unites, equipe: str):
        self.mon_equipe = []
        self.equipe_adverse = []
        self.liste_unites = liste_unites;
        self.mon_type = equipe

    def decide(self , observation):
        orders = []
        #analyse la situation et décide des actions à prendre pour chaque unité

        return orders
        
        
        """
        self.mon_equipe = arbitre.get_units_by_team(self.mon_equipe)
        self.equipe_adverse = arbitre.get_units_by_team(self.equipe_adverse)
        for unite in self.mon_equipe:
            for adversaire in self.equipe_adverse:
                if abs(unite.x - adversaire.x) <= 1 and abs(unite.y - adversaire.y) <= 1:
                    unite.attaquer(adversaire)
                    if not adversaire.is_alive:
                        arbitre.supprimer_unite(adversaire)
                    break
            unite.deplacer_unite(unite,dx,dy)"""