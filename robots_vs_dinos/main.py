from robots import Robot
from dino import Dino
from Fleet import Fleet
from herd import Herd

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

