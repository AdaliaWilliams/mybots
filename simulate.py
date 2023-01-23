import pybullet as p
def simulate():
    physicsClient = p.connect(p.GUI)
    p.disconnect()

simulate()