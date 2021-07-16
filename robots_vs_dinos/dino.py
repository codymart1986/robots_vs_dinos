import random

class Dino:
    def __init__(self, name):
        self.name = ""
        self.attack_power = random.choice([25, 30, 35])
        self.health = 100

    def attack_robot(self, enemy_robot):
        self.robot.health -= self.attack_power
        #setting dino to attack robot and subtract the attack power from robots health
