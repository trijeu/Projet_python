from unite import Unite


class UniteParthe(Unite):
    def __init__(self, x: float, y: float, vie: int, degat: int, type_degat: str, reload: float,
                 melee_armor: int, piercing_armor: int, portee: int, speed: float, LoS: int, taille: float):
        super().__init__(x, y, vie, degat, type_degat, reload, melee_armor, piercing_armor, portee, speed, LoS, taille)


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

    for cible in cibles_alentour:
        self.attaquer(cible, type_attaque="melee")


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
            speed=0,
            LoS=11,
            taille=0
        )
        self.volley_count = 5  # Tir de salve (5 flèches)

    def attaquer_salve(self, cible: Unite):

    for _ in range(self.volley_count):
        self.attaquer(cible, type_attaque="piercing")


class UniteArchers(UniteParthe):
    def __init__(self, x: float, y: float):
        super().__init__(
            x=x, y=y,
            vie=80,
            degat=12,
            type_degat="p",
            reload=1.8,
            melee_armor=5,
            piercing_armor=6,
            portee=8,
            speed=1.44,
            LoS=6,
            taille=0.5
        )
