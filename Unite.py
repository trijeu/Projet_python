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

    def distance(self, cible: "Unite") -> float:  # Retourne la distance entre self et cible
        return ((self.x - cible.x) ** 2 + (self.y - cible.y) ** 2) ** 0.5


    def est_a_portee(self, cible, attack_type=None) -> bool:
        type_attaque = attack_type or self.attack_type
        distance = self.distance(cible)

        if type_attaque == "piercing" and self.range > 0:
            return self.range > 0 and distance <= self.range + cible.radius
        
        if type_attaque == "melee":
            portee = self.radius + cible.radius + 0.15  # On ajoute une petite marge au corps à corps
            return distance <= portee
        return False


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
        if not self.est_a_portee(cible, attack_type):
            return False

        cible.take_damage(self.attack, attack_type, bonus)
        self.cooldown = self.reload_time
        return True


    def update(self, dt) -> tuple: #retourne les coordonées demandées par self
        if self.cooldown > 0:
            self.cooldown = max(0, self.cooldown - dt)
        if not self.is_alive and self.destination is None:
            return None
        
        cible_x, cible_y = self.destination
        dx, dy = self.calculer_pas(cible_x, cible_y, dt)
        return dx, dy


    """def deplacer(self, dt):#Méthode interne, utiliser update() ,deplace self en fct de dt, speed et sa destination
        if not self.is_alive or self.destination is None:
            return
        
        target_x, target_y = self.destination
        dx = target_x - self.x
        dy = target_y - self.y
        distance = hypot(dx, dy) #distance entre self et sa destination

        if distance <= 0.05: #Aproximation 
            self.x = target_x
            self.y = target_y
            self.destination = None
            return

        etape = min(self.speed * dt, distance) #distance parcourue max à ce tour
        self.x += (dx / distance) * etape
        self.y += (dy / distance) * etape

        if etape >= distance:
            self.x = target_x
            self.y = target_y
            self.destination = None""" # Utiliser les méthodes ci - dessous


    #Nouvelles méthodes
    def distance_point(self, x: float, y: float) -> float:#Distance entre le centre de self et le point (x, y)
        return hypot(x - self.x, y - self.y)


    def distance_bord(self, cible) -> float:#Distance bord a bord (0 = les deux cercles se touchent)
        return self.distance(cible) - self.radius - cible.radius


    def calculer_pas(self, cible_x: float, cible_y: float, dt: float):#Deplacement (dx, dy) voulu pendant dt, sans collisions
        distance = self.distance_point(cible_x, cible_y)
        pas = self.speed * dt
        if distance == 0 or pas <= 0:
            return 0.0, 0.0
        if distance <= pas:#on arrive pile sur la cible sans la depasser
            return cible_x - self.x, cible_y - self.y
        facteur = pas / distance
        return (cible_x - self.x) * facteur, (cible_y - self.y) * facteur


    """def deplacer(self, dt) -> bool:#Methode interne, utiliser update(). Avance vers self.destination
        cible_x, cible_y = self.destination

        dx, dy = self.calculer_pas(cible_x, cible_y, dt)
        self.x += dx
        self.y += dy

        if self.distance_point(cible_x, cible_y) < 0.05:
            self.x, self.y = cible_x, cible_y
            self.destination = None""" #Responsibilite donnee a Battlefield
    