import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import time
import pybullet_data


def simulate():
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    planeId = p.loadURDF("plane.urdf")
    robotId = p.loadURDF("body.urdf")
    p.setGravity(0,0,-9.8)
    p.loadSDF("world.sdf")
    backLegSensorValues = numpy.zeros(100)
    pyrosim.Prepare_To_Simulate(robotId) 
    
    for i in range(100):
        #print(i)
        backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        time.sleep(1/60)
        p.stepSimulation()
        
    
    p.disconnect()
    print(backLegSensorValues)
    numpy.save('data/saveData.npy', backLegSensorValues)




simulate()

