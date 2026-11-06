#classe abstraite

class Unite:
    def __init__(self, x: float, y: float, vie: int, degat: int, type_degat: str, reload: float, melee_armor: int, piercing_armor: int, portee: int, speed: float, taille: float):
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
        self.alive = True



    def attaquer(self, attaque, type_attaque, bonus = 0):
        if type_attaque == "melee":
            armure = self.melee_armor
        elif type_attaque == "piercing":
            armure = self.piercing_armor
        else: 
            raise ValueError("Type d'attaque invalide")

        damage = max(1, attaque - armure + bonus)
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            self.alive = False


    def deplacer(self ,nouveau_x,nouveau_y):
        self.x=nouveau_x
        self.y=nouveau_y
    
