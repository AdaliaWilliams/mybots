import math

import pybullet

import pyrosim.pyrosim as pyrosim

import pyrosim.constants as c

class NEURON: 

    def __init__(self,line):

        self.Determine_Name(line)

        self.Determine_Type(line)

        self.Search_For_Link_Name(line)

        self.Search_For_Joint_Name(line)

        self.Set_Value(0.0)

    def Add_To_Value( self, value ):

        self.Set_Value( self.Get_Value() + value )

    def Get_Joint_Name(self):

        return self.jointName

    def Get_Link_Name(self):

        return self.linkName

    def Get_Name(self):

        return self.name

    def Get_Value(self):

        return self.value

    def Is_Sensor_Neuron(self):

        return self.type == c.SENSOR_NEURON

    def Is_Hidden_Neuron(self):

        return self.type == c.HIDDEN_NEURON

    def Is_Motor_Neuron(self):

        return self.type == c.MOTOR_NEURON

    def Print(self):

        # self.Print_Name()

        # self.Print_Type()

        self.Print_Value()

        # print("")

    def Set_Value(self,value):

        self.value = value
    
    def Update_Sensor_Neuron(self):

        self.Set_Value(pyrosim.Get_Touch_Sensor_Value_For_Link(self.Get_Link_Name()))

    def Allow_Presynaptic_Neuron_To_Influence_Me(self, weight, value):
        print("weight= ", weight)
        print("value = ", value)
        influence = weight*value
        self.Add_To_Value(influence)
    
    def Update_Hidden_Or_Motor_Neuron(self, neurons, synapses):
        self.Set_Value(0)
        
        print("inital value =" ,self.Get_Value())
        
        for key in synapses.keys():
        
            if self.Get_Name() == synapses[key].Get_Target_Neuron_Name():
                self.Allow_Presynaptic_Neuron_To_Influence_Me(synapses[key].Get_Weight(), neurons[key[0]].Get_Value())
        
        # self.value = 0.0
        # #neurons = 0.0
        # #print(neurons)
        # print(self.value)
        # for key in synapses.keys():
        #     print(synapses[key].Get_Target_Neuron_Name())

        # for synapse in synapses:
        
        #     #get the second element in the tuple
        #     element = synapse[1]
        #     #print(element)
        #     #print(self.Get_Name())
        #     if (element == self.Get_Name()):
        #         #print the names of the pre and postsynapic neurons 
        #         self.Allow_Presynaptic_Neuron_To_Influence_Me(synapses[synapse].Get_Weight(), neurons[self.Get_Name()].Get_Value())
        #         #print(synapse[0])
        #         #print(synapse[1])
        print("final value =" , self.Get_Value())
        
        
        
        
    
# -------------------------- Private methods -------------------------

    def Determine_Name(self,line):

        if "name" in line:

            splitLine = line.split('"')

            self.name = splitLine[1]

    def Determine_Type(self,line):

        if "sensor" in line:

            self.type = c.SENSOR_NEURON

        elif "motor" in line:

            self.type = c.MOTOR_NEURON

        else:

            self.type = c.HIDDEN_NEURON

    def Print_Name(self):

       print(self.name)

    def Print_Type(self):

       print(self.type)

    def Print_Value(self):

       print(self.value , " " , end="" )

    def Search_For_Joint_Name(self,line):

        if "jointName" in line:

            splitLine = line.split('"')

            self.jointName = splitLine[5]

    def Search_For_Link_Name(self,line):

        if "linkName" in line:

            splitLine = line.split('"')

            self.linkName = splitLine[5]

    def Threshold(self):

        self.value = math.tanh(self.value)

    
