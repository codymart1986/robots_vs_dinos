from weapons import Weapon


import random

class Robot:
    def __init__(self, name):
        self.name = ""
        self.health = 100
        self.weapon = Weapon(random.choices(self.weapon.name))

    def attack_dino(self, enemy_dino):
        self.dino.health -= self.weapon.attack_power
