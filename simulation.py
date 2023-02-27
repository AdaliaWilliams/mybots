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
        
        
    def Run(self):
        for t in range(c.RANGE):
            print(t)
        
            time.sleep(c.SLEEP)
        # pyrosim.Set_Motor_For_Joint(
        #     bodyIndex = robotId,
        #     jointName = b'Torso_BackLeg',
        #     controlMode = p.POSITION_CONTROL,
        #     targetPosition= amplitudeBackLeg* numpy.sin(frequencyBackLeg*i +phaseOffsetBackLeg),
        #     #targetPosition = random.uniform(((-1)*(numpy.pi)/2),((numpy.pi)/2)),
        #     maxForce = c.MAXFORCE)
        # pyrosim.Set_Motor_For_Joint(
        #     bodyIndex = robotId,
        #     jointName = b'Torso_FrontLeg',  
        #     controlMode = p.POSITION_CONTROL,
        #     targetPosition=amplitudeFrontLeg * numpy.sin(frequencyFrontLeg*i+ phaseOffsetFrontLeg) ,
        #     #targetPosition = random.uniform(((-1)*(numpy.pi)/2),((numpy.pi)/2)),
        #     maxForce = c.MAXFORCE)
            p.stepSimulation() 
            self.robot.SENSE(t)
    
    def __del__(self):
        p.disconnect()
