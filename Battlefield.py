from unite import Unite
import UniteParthes
import UniteRomaine

class Battlefield :
    def __init__(self) :
        self.largeur= 120
        self.hauteur= 120
        self.unites = []
        self.obstacles= []
        self.castle = None
        self.id_counter = 1


    def ajouter_unite(self,unite: Unite,type: str, team: str, x: int, y: int) :
        if team == "romain" :
            if type == "legionnaire" :
                unite = UniteRomaine.Legionnaire(uid=self.id_counter, x=x, y=y)
                self.id_counter += 1
            elif type == "trebuchet" :
                unite = UniteRomaine.Trebuchet(uid=self.id_counter, x=x, y=y)
                self.id_counter += 1
            else :
                raise ValueError("Type d'unité romaine inconnu")
        elif team == "parthes" :
            if type == "archer" :
                unite = UniteParthes.UniteArchers(uid=self.id_counter, x=x, y=y)
                self.id_counter += 1
            elif type == "cataphract" :
                unite = UniteParthes.UniteCataphract(uid=self.id_counter, x=x, y=y)
                self.id_counter += 1
            else :
                raise ValueError("Type d'unité parthe inconnu")
        else :
            raise ValueError("Équipe inconnue")

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

