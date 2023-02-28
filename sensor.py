import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, linkName):
        #self.sensor = SENSOR
        self.linkName = linkName
        self.values = numpy.zeros(c.RANGE)
    
        
        
    def Get_Value(self, t): 
        
        self.values[t] = (pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName))
        print(self.values)
        
        

    
        

        

    
        

        