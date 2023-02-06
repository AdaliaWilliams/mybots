import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import pybullet_data

def simulate():
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    planeId = p.loadURDF("plane.urdf")
    robotId = p.loadURDF("body.urdf")
    p.setGravity(0,0,-9.8)
    p.loadSDF("world.sdf")
    pyrosim.Prepare_To_Simulate(robotId)
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    
    for i in range(1000):
        #print(i)
        print(backLegTouch)
        time.sleep(1/60)
        p.stepSimulation()
        
    p.disconnect()




simulate()
