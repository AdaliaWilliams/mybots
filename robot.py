import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy
import constants as c

class ROBOT:
    def __init__(self):
        self.robot = ROBOT
        self.motor = MOTOR()
        self.robotId = p.loadURDF("body.urdf")
        
        
        pyrosim.Prepare_To_Simulate(self.robotId) 
        self.Prepare_To_Sense()
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:  
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:  
            self.sensors[linkName] = SENSOR(linkName)

    
    def SENSE(self, t):
        for i in self.sensors:
            #self.sensors[i].Get_Value(t)
            #self.sensors[i].GetValue(t)
            SENSOR(i).Get_Value(t)
            #self.sensors.get(i).getValue(t)
            #self.Get_Value(t)
         