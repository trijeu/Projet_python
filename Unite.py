# classe abstraite

from math import hypot


class Unite:
    def __init__(
        self,
        uid,
        team,
        x,
        y,
        hp,
        max_hp,
        attack,
        attack_type,
        reload_time,
        melee_armor,
        piercing_armor,
        range,
        speed,
        radius
    ):
        self.uid = uid
        self.team = team
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.attack_type = attack_type
        self.reload_time = reload_time
        self.melee_armor = melee_armor
        self.piercing_armor = piercing_armor
        self.range = range
        self.speed = speed
        self.radius = radius

        # Etat de l'unité
        self.is_alive = True
        self.cooldown = 0.0
        self.target = None
        self.destination = None  # destination tuple (x, y) vers laquelle l'unité se déplace

    def distance(self, cible) -> float:  # Retourne la distance entre self et cible
        return ((self.x - cible.x) ** 2 + (self.y - cible.y) ** 2) ** 0.5


    def est_a_portee(self, cible) -> bool:
        type_attaque = self.attack_type
        distance = self.distance(cible)

        if type_attaque == "piercing" and self.range > 0:
            return distance <= self.range + cible.radius
        if type_attaque == "melee":

            portee = self.radius + cible.radius + 0.25  # On ajoute une petite marge au corps à corps
            return distance <= portee


    def take_damage(self, attack, attack_type, bonus = 0):  # Méthode interne, utiliser attaquer() pour infliger des dégâts à une cible
        if attack_type == "melee":
            armure = self.melee_armor
        elif attack_type == "piercing":
            armure = self.piercing_armor
        else:
            raise ValueError("Type d'attaque invalide")

        damage = max(1, attack - armure + bonus)
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            self.is_alive = False


    def attaquer(self, cible: "Unite", type_attaque: str = None, bonus: int = 0) -> bool:  # Renvoie un bool si l'attaque réussit
        if not self.is_alive:
            return False
        if not cible.is_alive:
            return False
        if self.cooldown > 0:
            return False

        attack_type = type_attaque or self.attack_type
        if not self.est_a_portee(cible):
            return False

        cible.take_damage(self.attack, attack_type, bonus)
        self.cooldown = self.reload_time
        return True


    def deplacer(self, dt, battlefield=None) -> bool: # Methode interne, utiliser update(). Avance vers self.destination. Renvoie True a l'arrivee
        if not self.is_alive or self.destination is None:
            return False
        cible_x, cible_y = self.destination

        if battlefield is not None:#collisions + bords de carte + falaises
            battlefield.deplacer_unite(self, cible_x, cible_y, dt)
        else: #mouvement libre, sans collisions
            dx, dy = self.calculer_pas(cible_x, cible_y, dt)
            self.x += dx
            self.y += dy

        if self.distance_point(cible_x, cible_y) < 1e-6:
            self.x, self.y = cible_x, cible_y
            self.destination = None
            return True
        return False


    def update(self, dt):
        if self.cooldown > 0:
            self.cooldown = max(0, self.cooldown - dt)