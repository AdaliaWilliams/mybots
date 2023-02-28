import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy
import random
import constants as c

class ROBOT:
    def __init__(self):
        self.robot = ROBOT
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId) 
        self.Prepare_To_Sense()
       #self.Prepare_To_Act()
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:  
            self.sensors[linkName] = SENSOR(linkName)

    #def Prepare_To_Act(self):
        #self.amplitude = c.AMP
        #self.frequency = c.FREQUENCY
        #self.offset = c.PHASE
        #self.motors = {}
        #for jointName in pyrosim.pyrosim.jointNamesToIndices:  
            #self.motors[jointName] = MOTOR(jointName)

    
    def SENSE(self, t):
        for i in range(len(self.sensors)):
            print(i)
            print(self.sensors.get(i))
        

        for linkName in self.sensors:
            #self.sensors[i].Get_Value(t)
            #self.sensors.get(i).Get_Value(t)
            #i.Get_Value(t)
            print(self.sensors.get(linkName)) 
            print(linkName) 
            #SENSOR(linkName).Get_Value(t)
            #SENSOR(i).Get_Value(t, i)
            #self.sensors.get(i).getValue(t)

   # def Act(self,t):
   #     for i in self.motors:
    #        MOTOR.Set_Value(t, self.robot)
         