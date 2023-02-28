import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy
import random
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self):
        self.robot = ROBOT
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId) 
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:  
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.amplitude = c.AMP
        self.frequency = c.FREQUENCY
        self.offset = c.PHASE
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:  
            self.motors[jointName] = MOTOR(jointName)

    
    def SENSE(self, t):

        for linkName in self.sensors:
            #print(self.sensors.get(linkName)) 
            #print(self.sensors[linkName])
            self.sensors[linkName].Get_Value(t)
            self.sensors[linkName].Save_Values()
            #print(linkName) 
            #SENSOR(linkName).Get_Value(t)
            #SENSOR(i).Get_Value(t, i)
            #self.sensors.get(i).getValue(t)

    def Act(self,t):
        for jointName in self.motors:
            #print(jointName)
            self.motors[jointName].Set_Value(t,self.robotId)
            self.motors[jointName].Save_Values()
    
    

    def Think(self):
        self.nn.Print()