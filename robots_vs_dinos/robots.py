from weapons import Weapon


import random

class Robot:
    def __init__(self, name):
        weap = Weapon(11)
        self.name = name
        self.health = 100
        self.weapon = random.choice(weap.get_random_weapon())

    def attack_dino(self, enemy_dino):
        self.dino.health -= self.weapon.attack_power
