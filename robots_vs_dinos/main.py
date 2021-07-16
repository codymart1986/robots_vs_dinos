from robots import Robot
from dino import Dino
from Fleet import Fleet
from herd import Herd
from battlefield import Battlefield
import random

#Robots Created
robo1 = Robot("C-3PO")
robo2 = Robot("Wall-E")
robo3 = Robot("Cl4pTp")

#Dino's Created
dino1 = Dino("Rex")
dino2 = Dino("Steg")
dino3 = Dino("PaRappa the Raptor")

#Adding Robots to a fleet
fleet = Fleet()
fleet.add_robo(robo1)
fleet.add_robo(robo2)
fleet.add_robo(robo3)

#Adding Dino's to a herd
herd = Herd()
herd.add_dino(dino1)
herd.add_dino(dino2)
herd.add_dino(dino3)

#Create a BattleField
battle = Battlefield(fleet,herd)
print(battle.robos.robo_fleet[0].name)

battle.attack(battle.robos.robo_fleet[0], battle.dinos.dino_herd[0])
# battle.attack(battle.robos.robo_fleet[1], battle.dinos.dino_herd[1])
