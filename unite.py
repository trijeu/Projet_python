#classe abstraite

class Unite:
    def __init__(self, vie: int, degat: int, type_degat: str, reload: float, melee_armor: int, peircing_armor: int, portee: int, speed: float, LoS: int, taille: float):
        self.vie = vie
        self.degat = degat
        self.type_degat = type_degat
        self.reload = reload
        self.melee_armor = melee_armor
        self.peircing_armor = peircing_armor
        self.portee = portee
        self.speed = speed
        self.LoS = LoS
        self.taille = taille




    def attaquer(self, cible: Unite, type_attaque: str, bonus: int):
        if type_attaque == "melee":
            degat = self.degat - cible.melee_armor + bonus
        elif type_attaque == "peircing":
            degat = self.degat - cible.peircing_armor + bonus

        cible.vie -= degat
    
