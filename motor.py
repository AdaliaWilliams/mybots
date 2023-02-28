import numpy
import random
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        world = MOTOR
        self.jointName = jointName
        self.motorValues = []
        

    def Set_Value(self,i,robotId):
        pyrosim.Set_Motor_For_Joint(
             bodyIndex = robotId,
             jointName = self.jointName,  
             controlMode = p.POSITION_CONTROL,
             targetLocation= self.motorValues ,
             targetPosition = random.uniform(((-1)*(numpy.pi)/2),((numpy.pi)/2)),
             maxForce = c.MAXFORCE)

