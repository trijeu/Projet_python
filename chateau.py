class Chateau:
    def __init__(
        self,
        x,
        y,
        hp,
        max_hp,
        attack,
        attack_type,
        reload_time,
        range
    ):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
        self.attack, attack
        self.attack_type = attack_type
        self.reload_time = reload_time
        self.range = range

        self.is_alive = True
        self.cooldown = 0.0
        self.targets = []    

    def take_damage(self, damage, attack_type):
        pass

    def update(self, dt):
        pass

    def est_detruit(self):
        pass