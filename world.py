import pybullet as p
import pybullet_data
import constants as c

class WORLD:
    def __init__(self):
        self.world = WORLD
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.planeId = p.loadURDF("plane.urdf")
        self.robotId = p.loadURDF("body.urdf")
        p.setGravity(0,0,-c.GRAVITY)
        p.loadSDF("world.sdf")