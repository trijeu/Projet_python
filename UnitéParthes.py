from unite import Unite


'''class UniteParthe(Unite):
    def __init__(self, x: float, y: float, vie: int, degat: int, type_degat: str, reload: float,
                 melee_armor: int, piercing_armor: int, portee: int, speed: float, taille: float):
        super().__init__(x, y, vie, degat, type_degat, reload, melee_armor, piercing_armor, portee, speed, taille)
'''#Nouvelle version de l'init selon les nouveaux paramètres de Unite

class UniteCataphract(Unite):
    def __init__(self,uid: int, x: float, y: float):
        super().__init__(
            uid=uid,
            team = "parthe",
            x=x, 
            y=y,
            hp=150,
            attack=14,
            type_attack="melee",
            reload_time=1.7,
            melee_armor=5,
            piercing_armor=5,
            range=0,
            speed=1.35,
            radius=0.5
        )
        self.trample_damage_zone = 0.5

    def trample_attack(self, cibles_alentour: list):
        for cible in cibles_alentour:
            self.attaquer(cible, type_attaque="melee")

'''
class UniteCastle(Unite):
    def __init__(self,uid: int, x: float = 0.0, y: float = 0.0):
        super().__init__(
            uid=uid,
            team = "parthe",
            x=x,
            y=y,
            hp=1000,
            attack=15,
            type_attack="piercing",
            reload_time=2.0,
            melee_armor=0,
            piercing_armor=13,
            range=11,
            speed=0,
            radius=0
        )
        self.volley_count = 5  # Tir de salve (5 flèches)

    def attaquer_salve(self, cible: Unite):
        for _ in range(self.volley_count):
            self.attaquer(cible, type_attaque="piercing")
'''#Le chateau sera dans une classe à part, il est unique et un objectif

class UniteArchers(Unite):
    def __init__(self,uid: int, x: float, y: float):
        super().__init__(
            uid=uid,
            team = "parthe",
            x=x,
            y=y,
            hp=80,
            attack=12,
            type_attack="piercing",
            reload_time=1.8,
            melee_armor=5,
            piercing_armor=6,
            range=8,
            speed=1.44,
            radius=0.5
        )
