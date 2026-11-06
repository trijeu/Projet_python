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




    def attaquer(self, cible: "Unite", type_attaque: str = None, bonus: int = 0):

        if type_attaque is None:
            type_attaque = self.type_degat

        if type_attaque == "melee":
            armure = cible.melee_armor

        elif type_attaque=="piercing" :
            armure = cible.piercing_armor

        else:
            raise ValueError(f"Type d'attaque inconnu : {type_attaque}")

        degats = max(1, self.degat + bonus - armure)

        cible.vie = max(0, cible.vie - degats)

        return degats


    def deplacer(self ,nouveau_x,nouveau_y):
        self.x=nouveau_x
        self.y=nouveau_y
    
