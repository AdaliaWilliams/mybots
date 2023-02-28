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
        
        if(self.jointName==b'Torso_BackLeg'):
            self.motorValues = c.AMP * numpy.sin(c.FREQUENCYB*i + c.PHASE)
        else:
            self.motorValues = c.AMP * numpy.sin(c.FREQUENCY*i + c.PHASE)
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,  
            controlMode = p.POSITION_CONTROL,
            targetPosition= self.motorValues,
            maxForce = c.MAXFORCE)
        
    def Save_Values(self):
        nums = c.TWO* numpy.pi*(numpy.arange(c.RANGE) / c.RANGE)
        targetAngles1= numpy.sin(c.FREQUENCY * nums+c.PHASE)*(c.AMP)
        #print(targetAngles1)
        targetAngles= targetAngles1/100
        targetAngles = targetAngles*(numpy.pi/4)
        targetAngles= numpy.sin(targetAngles)
        numpy.save('data/targetAnglesBackLeg.npy', targetAngles)


