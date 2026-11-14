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
        self.destination = None #destination tuple (x, y) vers laquelle l'unité se déplace


    def take_damage(self, attack, attack_type, bonus = 0):#Self prend des dégats en paramètres
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

    """def attaquer(self, cible: "Unite", attack_type: str = None, bonus: int = 0):#self attaque une cible
        if attack_type is None:
            attack_type = self.attack_type

        if attack_type == "melee":
            armure = cible.melee_armor

        elif attack_type=="piercing" :
            armure = cible.piercing_armor

        else:
            raise ValueError(f"Type d'attaque inconnu : {attack_type}")

        degats = max(1, self.attack + bonus - armure)
        cible.hp = max(0, cible.hp - degats)"""#Voir take_damage pour moins de paramètres


    def deplacer(self, dt):#Deplace self en fct de dt, speed et sa destination
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
    
    def update_cooldown(self, dt):#met a jour le cooldown d'attaque de self en fct de dt
        if self.cooldown > 0:
            self.cooldown = max(0, self.cooldown - dt)

    