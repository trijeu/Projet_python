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
        self.alive = True """


    def __init__(
        self,
        uid,
        team,
        x,
        y,
        hp,
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
        self.destination = None


    def attaquer(self, attack, attack_type, bonus = 0):
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


    def deplacer(self ,target_x,target_y, dt):
        if not self.is_alive:
            return

        dx = target_x - self.x
        dy = target_y - self.y
        distance = (dx**2 + dy**2)**0.5

        if distance == 0:
            return

        etape = min(self.speed * dt, distance)
        self.x += (dx / distance) * etape
        self.y += (dy / distance) * etape
    
    def update_cooldown(self, dt):
        if self.cooldown > 0:
            self.cooldown = max(0, self.cooldown - dt)

    