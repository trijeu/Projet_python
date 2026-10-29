from unite import Unite

class UniteRomaine(Unite):

    def __init__(
        self,
        x: float,
        y: float,
        vie: int,
        degat: int,
        type_degat: str,
        reload: float,
        melee_armor: int,
        peircing_armor: int,
        portee: int,
        speed: float,
        LoS: int,
        taille: float,
    ):
        super().__init__(
            x,
            y,
            vie,
            degat,
            type_degat,
            reload,
            melee_armor,
            peircing_armor,
            portee,
            speed,
            LoS,
            taille,
            "Romain",
        )
    

class Legionnaire(UniteRomaine):

    def __init__(self, x: float, y: float):
        super().__init__(
            x=x,
            y=y,
            vie=75,
            degat=18,
            type_degat="melee",
            reload=2.0,
            melee_armor=6,
            peircing_armor=6,
            portee=0,
            speed=1.06,
            LoS=7,
            taille=0.4,
        )
        self.mur_de_boucliers_actif = False

    def basculer_mur_de_boucliers(self, actif: bool):
        if actif and not self.mur_de_boucliers_actif:
            self.peircing_armor += 6
            self.mur_de_boucliers_actif = True
        elif not actif and self.mur_de_boucliers_actif:
            self.peircing_armor -= 6
            self.mur_de_boucliers_actif = False

class Trebuchet(UniteRomaine):

    def __init__(self, x: float, y: float):
        super().__init__(
            x=x,
            y=y,
            vie=150,
            degat=250,
            type_degat="peircing",
            reload=0.0,
            melee_armor=2,
            peircing_armor=8,
            portee=0,
            speed=0.8,
            LoS=19,
            taille=1.0,
        )
        self.temps_depaquetage = 11.0
        self.est_depaquete = False
        self.precision_chateau = 0.8
        self.precision_unites = 0.15  
