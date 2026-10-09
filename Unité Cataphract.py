class UniteParthe(Unite):
    def __init__(self, x: float, y: float, vie: int, degat: int, type_degat: str, reload: float,
                 melee_armor: int, piercing_armor: int, portee: int, speed: float, LoS: int, taille: float):
        super().__init__(x, y, vie, degat, type_degat, reload, melee_armor, piercing_armor, portee, speed, LoS, taille)


class UniteCastle(UniteParthe):
    def __init__(self, x: float = 0.0, y: float = 0.0):
        super().__init__(
            x=x, y=y,
            vie=1000,
            degat=15,
            type_degat="p",
            reload=2.0,
            melee_armor=0,
            piercing_armor=13,
            portee=11,
            speed=0.0,  # Immobile
            LoS=11,
            taille=0.0
        )
        self.volley_count = 5  # Tir de salve (5 flèches)


def attaquer_salve(self, cible: Unite):
    """Tir de salve infligeant 5 projectiles d'un coup."""
    for _ in range(self.volley_count):
        self.attaquer(cible, type_attaque="piercing")


class Archer(UniteParthes):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.vie = 80
        self.degat = 12
        self.type_degat = "peircing"
        self.reload = 1.8
        self.melee_armor = 5
        self.peircing_armor = 6
        self.portee = 8
        self.speed = 1.44
        self.LoS = 6
        self.taille = 0.5


class UniteCataphract(UniteParthe):
    def __init__(self, x: float, y: float):
        super().__init__(
            x=x, y=y,
            vie=150,
            degat=14,
            type_degat="m",
            reload=1.7,
            melee_armor=5,
            piercing_armor=5,
            portee=0,
            speed=1.35,
            LoS=4,
            taille=0.5
        )
        self.trample_damage_zone = 0.5


def trample_attack(self, cibles_alentour: list):
    """Attaque de zone infligeant des dégâts de piétinement."""
    for cible in cibles_alentour:
        self.attaquer(cible, type_attaque="melee")
