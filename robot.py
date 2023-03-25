import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy
import random
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os


class ROBOT:
    def __init__(self,solutionID):
        brainFile= "brain"+solutionID+".nndf"
        self.robot = ROBOT
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId) 
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK(brainFile)
        removeCommand = "rm "+ brainFile
        os.system(removeCommand)
    
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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                if jointName == 'Torso_BackLeg':
                    jointName = b'Torso_BackLeg'
                elif jointName == 'Torso_FrontLeg':
                    jointName = b'Torso_FrontLeg'
                self.motors[jointName].Set_Value(desiredAngle,self.robotId,t)
                # print(neuronName)
                # print(jointName)
                # print(desiredAngle)
                

        #for jointName in self.motors:
            #print(jointName)
            #self.motors[jointName].Set_Value(t,self.robotId)
            #self.motors[jointName].Save_Values()
    
    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        print("position values (x,y,z): ",positionOfLinkZero)
        print("position value of x: ",xCoordinateOfLinkZero)
        f = open("fitness.txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()


    def Think(self):
        self.nn.Update()
        self.nn.Print()


   

        