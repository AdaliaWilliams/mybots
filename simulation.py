import pybullet as p
import random
import pyrosim.pyrosim as pyrosim
import numpy
import time
import pybullet_data
import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.world= WORLD()
        self.robot = ROBOT()
        self.physicsClient = p.connect(p.GUI)
        p.setGravity(0,0,-c.GRAVITY)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        pyrosim.Prepare_To_Simulate(self.robot.robotId) 
        