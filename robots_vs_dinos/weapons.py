class Weapon:
    def __init__(self, attack_power):
        self.name = ["Plasma Cannon", "Disintegrator", "Gatling Laser"]
        self.attack_power = [25, 30, 35]


    def get_random_weapon(self):
        return self.name