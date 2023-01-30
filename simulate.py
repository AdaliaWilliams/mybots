import pybullet as p
import time
import pybullet_data

def simulate():
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    planeId = p.loadURDF("plane.urdf")
    p.setGravity(0,0,-9.8)
    p.loadSDF("world.sdf")
    for i in range(1000):
        print(i)
        time.sleep(1/60)
        p.stepSimulation()
        
    p.disconnect()

simulate()
