class Battlefield:
    def __init__(self, robos, dinos):
        #insert fleet and herd
        self.robos = robos
        self.dinos = dinos
        self.robos_turn = False

        #display_welcome
    def display_welcome():
        print('Welcome to the Thunder Dome')

    #battle
    def battle(self):
        #for robots in self.robos:
        for dino in self.dinos:
            if(dino.health > 0):
                print()

    #Attack 
    def attack(self, robo, dino):
        if(self.robos_turn):
            dino.health -= robo.weapon.attack_power
            self.robos_turn = False
        if(self.robos_turn == False):
            robo.health -= dino.attack_power
            self.robos_turn = True

        print('Dino HP: ' + str(dino.health))
        print('Robo HP: ' + str(robo.health))


    #dino_turn
    def robos_turn(self):
        if(self.robos_turn == False):
            return True
    
    #robo_turn
    def robos_turn(self):
        if(self.robos_turn):
            return True


    #display winners