from Unite import Unite


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
            max_hp=150,
            attack=14,
            attack_type="melee",
            reload_time=1.7,
            melee_armor=5,
            piercing_armor=5,
            range=0,
            speed=1.35,
            radius=0.5
        )
        self.trample_damage_zone = 0.5

    def trample_attack(self, cibles_alentour: list):
        if not self.is_alive or self.cooldown > 0:
            return 0
        nb_touches = 0
        for cible in cibles_alentour:
            if not cible.is_alive:
                continue
            
            dist = self.distance(cible)
            portee = self.radius + cible.radius + self.trample_damage_zone

            if dist  <= portee:
                cible.take_damage(self.attack, "melee", bonus = 4)
                nb_touches += 1
            
        if nb_touches > 0:
            self.cooldown = self.reload_time
        return nb_touches    
        

class UniteArchers(Unite):
    def __init__(self,uid: int, x: float, y: float):
        super().__init__(
            uid=uid,
            team = "parthe",
            x=x,
            y=y,
            hp=80,
            max_hp=80,
            attack=12,
            attack_type="piercing",
            reload_time=1.8,
            melee_armor=5,
            piercing_armor=6,
            range=8,
            speed=1.44,
            radius=0.5
        )
