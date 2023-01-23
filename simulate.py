import pybullet as p
import time

def simulate():
    physicsClient = p.connect(p.GUI)
    p.loadSDF("box.sdf")
    for i in range(1000):
        print(i)
        time.sleep(1/60)
        p.stepSimulation()
        
    p.disconnect()

simulate()
