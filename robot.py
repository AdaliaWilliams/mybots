import pybullet as p
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.robot = ROBOT
        self.sensors = SENSOR()
        self.motor = MOTOR()
        self.robotId = p.loadURDF("body.urdf")