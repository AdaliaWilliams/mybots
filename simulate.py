#import pybullet as p
import random
import pyrosim.pyrosim as pyrosim
import numpy
import time
import pybullet_data
import constants as c
from simulation import SIMULATION


simulation = SIMULATION()
# amplitudeBackLeg = c.AMPB
# frequencyBackLeg = c.FREQUENCYB
# phaseOffsetBackLeg = c.PHASEB
# amplitudeFrontLeg = c.AMPF
# frequencyFrontLeg = c.FREQUENCYF
# phaseOffsetFrontLeg = c.PHASEF


# def simulate():
    
#     physicsClient = p.connect(p.GUI)
#     p.setAdditionalSearchPath(pybullet_data.getDataPath())
#     planeId = p.loadURDF("plane.urdf")
#     robotId = p.loadURDF("body.urdf")
#     p.setGravity(0,0,-c.GRAVITY)
#     p.loadSDF("world.sdf")
#     backLegSensorValues = numpy.zeros(c.RANGE)
#     frontLegSensorValues = numpy.zeros(c.RANGE)
    

#     nums = c.TWO* numpy.pi*(numpy.arange(c.RANGE) / c.RANGE)
#     targetAnglesBackLeg = numpy.sin(frequencyBackLeg * nums+phaseOffsetBackLeg)*(amplitudeBackLeg)
#     targetAnglesFrontLeg = numpy.sin(frequencyFrontLeg* nums+phaseOffsetFrontLeg)*(amplitudeFrontLeg)
#     #print(targetAnglesBackLeg)

#     #print(targetAngles)
#     #targetAngles= targetAngles/100
#     #targetAngles = targetAngles*(numpy.pi/4)
#     #targetAngles= numpy.sin(targetAngles)

#     #numpy.save('data/targetAnglesBackLeg.npy', targetAnglesBackLeg)
#     #numpy.save('data/targetAnglesFrontLeg.npy', targetAnglesFrontLeg)
    

#     
    
#     #exit()
#     for i in range(c.RANGE):
#         #print(i)
#         backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#         frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#         time.sleep(c.SLEEP)
#         pyrosim.Set_Motor_For_Joint(
#             bodyIndex = robotId,
#             jointName = b'Torso_BackLeg',
#             controlMode = p.POSITION_CONTROL,
#             targetPosition= amplitudeBackLeg* numpy.sin(frequencyBackLeg*i +phaseOffsetBackLeg),
#             #targetPosition = random.uniform(((-1)*(numpy.pi)/2),((numpy.pi)/2)),
#             maxForce = c.MAXFORCE)
#         pyrosim.Set_Motor_For_Joint(
#             bodyIndex = robotId,
#             jointName = b'Torso_FrontLeg',  
#             controlMode = p.POSITION_CONTROL,
#             targetPosition=amplitudeFrontLeg * numpy.sin(frequencyFrontLeg*i+ phaseOffsetFrontLeg) ,
#             #targetPosition = random.uniform(((-1)*(numpy.pi)/2),((numpy.pi)/2)),
#             maxForce = c.MAXFORCE)
#         p.stepSimulation()
        
    
#     p.disconnect()
#     #print(backLegSensorValues)
#     numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
#     numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)





# simulate()

