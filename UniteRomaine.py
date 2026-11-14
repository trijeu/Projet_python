from Unite import Unite

'''class UniteRomaine(Unite):

    def __init__(
        self,
        x: float,
        y: float,
        vie: int,
        degat: int,
        type_degat: str,
        reload: float,
        melee_armor: int,
        piercing_armor: int,
        portee: int,
        speed: float,
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
            piercing_armor,
            portee,
            speed,
            taille,
        )
    '''#Nouvelle version de l'init selon les nouveaux paramètres de Unite

class Legionnaire(Unite):

    def __init__(self, uid: int, x: float, y: float):
        super().__init__(
            uid=uid,
            team = "romain",
            x=x,
            y=y,
            hp=75,
            max_hp=75,
            attack=18,
            attack_type="melee",
            reload_time=2.0,
            melee_armor=6,
            piercing_armor=6,
            range=0,
            speed=1.06,
            radius=0.4,
        )
        self.mur_de_boucliers_actif = False

    def basculer_mur_de_boucliers(self, actif: bool):
        if actif and not self.mur_de_boucliers_actif:
            self.piercing_armor += 6
            self.mur_de_boucliers_actif = True
        elif not actif and self.mur_de_boucliers_actif:
            self.piercing_armor -= 6
            self.mur_de_boucliers_actif = False

class Trebuchet(Unite):

    def __init__(self, uid: int, x: float, y: float):
        super().__init__(
            uid=uid,
            team = "romain",
            x=x,
            y=y,
            hp=150,
            max_hp=150,
            attack=250,
            attack_type="piercing",
            reload_time=0.0,
            melee_armor=2,
            piercing_armor=8,
            range=0,
            speed=0.8,
            radius=1.0,
        )
        self.temps_depaquetage = 11.0
        self.temps_restant_depaquetage = 0.0
        self.est_depaquete = False
        self.precision_chateau = 0.8
        self.precision_unites = 0.15  

    def deplier(self):
        if not self.est_depaquete and self.temps_restant_depaquetage <= 0:
            self.destination = None
            self.temps_restant_depaquetage = self.temps_depaquetage


    def update(self, dt):
        self.update(dt)

        if self.temps_restant_depaquetage > 0:
            self.temps_restant_depaquetage = max(0, self.temps_restant_depaquetage - dt)

            if self.temps_restant_depaquetage == 0:
                self.est_depaquete = True
            return

        if not self.est_depaquete:
            self.deplacer(dt)


    def attaquer(self, cible, type_attaque=None, bonus=0):
        if not self.est_depaquete:
            return False

        return super().attaquer(cible, type_attaque, bonus)


    def replier(self):
        self.est_depaquete = False
        self.temps_restant_depaquetage = 0.0
        self.cooldown = 0.0