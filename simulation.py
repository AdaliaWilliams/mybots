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
    def __init__(self, directOrGUI, solutionID):
        if directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
        elif directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        self.world= WORLD()
        self.robot = ROBOT(solutionID)
        
        
    def Run(self):
        for t in range(c.RANGE):
            #print(t)
        
            time.sleep(c.SLEEP)
            p.stepSimulation() 
            self.robot.SENSE(t)
            self.robot.Think()
            self.robot.Act(t)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
            
    
    def __del__(self):
        p.disconnect()

   