#classe abstraite

class Unite:
    """ def __init__(self, x: float, y: float, vie: int, degat: int, type_degat: str, reload: float, melee_armor: int, piercing_armor: int, portee: int, speed: float, taille: float):
        self.vie = vie
        self.degat = degat
        self.type_degat = type_degat
        self.reload = reload
        self.melee_armor = melee_armor
        self.piercing_armor = piercing_armor
        self.portee = portee
        self.speed = speed
        self.taille = taille
        self.x = x
        self.y = y
        self.cooldown = 0.0
        self.alive = True """#Nouvelle version de l'init selon les nouveaux paramètres de Unite


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

        #Etat de l'unité
        self.is_alive = True
        self.cooldown = 0.0
        self.target = None
        self.destination = None #destination tuple (x, y) vers laquelle l'unité se déplace


    def distance(self,cible) -> float:#Retourne la distance entre self et cible
        return ((self.x - cible.x) ** 2 + (self.y - cible.y) ** 2) ** 0.5


    def est_a_portee(self, cible) -> bool:
        type_attaque = self.attack_type
        distance = self.distance(cible)

        if type_attaque == "piercing" and self.range > 0:
            return distance <= self.range + cible.radius
        if type_attaque == "melee":
            portee = self.radius + cible.radius + 0.25 #On ajoute une petite marge au corps à corps
            return distance <= portee


    def take_damage(self, attack, attack_type, bonus = 0):#Méthode interne, utiliser attaquer() pour infliger des dégâts à une cible
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


    def attaquer(self, cible: "Unite", type_attaque: str = None, bonus: int = 0) -> bool:#Renvoie un bool si l'attaque réussit
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


    def deplacer(self, dt):#Méthode interne, euiliser update() ,deplace self en fct de dt, speed et sa destination
        if not self.is_alive:
            return
        if self.destination is None:
            return

        target_x = self.destination[0]
        target_y = self.destination[1]
        dx = target_x - self.x
        dy = target_y - self.y
        distance = (dx**2 + dy**2)**0.5

        if distance == 0:
            return

        etape = min(self.speed * dt, distance)
        self.x += (dx / distance) * etape
        self.y += (dy / distance) * etape
    
    def update(self, dt):#met a jour l'unite en fct de dt
        if self.cooldown > 0:
            self.cooldown = max(0, self.cooldown - dt)
        self.deplacer(dt)

    