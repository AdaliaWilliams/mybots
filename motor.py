import numpy
import random
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        #self.motor = MOTOR
        self.jointName = jointName
        self.motorValues = 0
        

    def Set_Value(self,i,robotId):
        
        self.motorValues = c.AMP * numpy.sin(c.FREQUENCY*i + c.PHASE)
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,  
            controlMode = p.POSITION_CONTROL,
            targetPosition= self.motorValues ,
            maxForce = c.MAXFORCE)

