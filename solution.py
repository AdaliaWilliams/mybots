import numpy
import pyrosim.pyrosim as pyrosim
import os
import random

class SOLUTION:
    def __init__(self):
        self.weights =  numpy.random.rand(3,2)
        self.weights = (self.weights * 2 )- 1
    
    def Evaluate(self, DirectOrGui):
        
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        if DirectOrGui == "DIRECT":
            os.system("python3 simulate.py DIRECT  &")
        elif  DirectOrGui == "GUI":
            os.system("python3 simulate.py GUI &")
        f = open("fitness.txt", "r")
        self.fitness = float(f.readline())
        f.close()
       # print("fitness: ", self.fitness)

    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)

        self.weights[randomRow][randomColumn] = (random.random() * 2) -1
       

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")  
        pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5] , size=[1,1,1])
        pyrosim.End()
    
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,(1.5)] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [(0.5),0,(1.0)])
        pyrosim.Send_Cube(name="BackLeg", pos=[(.5),0,(-.5)] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [(-0.5),0,(1.0)])
        pyrosim.Send_Cube(name="FrontLeg", pos=[(-.5),0,(-.5)] , size=[1,1,1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        for currentRow in range(3):
        #print("i value:", i)
            if currentRow == 0:
                pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
            if currentRow == 1:
                pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
            if currentRow == 2:
                pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
            for currentColumn in range(2): 
                #print("j value:", j)
                if currentColumn == 0:
                    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
                if currentColumn == 1:
                    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
            
                targetName = currentColumn+3
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = targetName, weight =self.weights[currentRow][currentColumn] )
        pyrosim.End()
    