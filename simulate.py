import pybullet as p
import random
import pyrosim.pyrosim as pyrosim
import numpy
import time
import pybullet_data

amplitudeBackLeg = -1*5*numpy.pi
frequencyBackLeg = 15
phaseOffsetBackLeg = numpy.pi/2
amplitudeFrontLeg = 5*numpy.pi
frequencyFrontLeg = 12
phaseOffsetFrontLeg = -1*numpy.pi/2

def simulate():
    
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    planeId = p.loadURDF("plane.urdf")
    robotId = p.loadURDF("body.urdf")
    p.setGravity(0,0,-9.8)
    p.loadSDF("world.sdf")
    backLegSensorValues = numpy.zeros(1000)
    frontLegSensorValues = numpy.zeros(1000)
    

    nums = 2* numpy.pi*(numpy.arange(1000) / 1000)
    targetAnglesBackLeg = numpy.sin(frequencyBackLeg * nums+phaseOffsetBackLeg)*(amplitudeBackLeg)
    targetAnglesFrontLeg = numpy.sin(frequencyFrontLeg* nums+phaseOffsetFrontLeg)*(amplitudeFrontLeg)
    #print(targetAnglesBackLeg)

    #print(targetAngles)
    #targetAngles= targetAngles/100
    #targetAngles = targetAngles*(numpy.pi/4)
    #targetAngles= numpy.sin(targetAngles)

    #numpy.save('data/targetAnglesBackLeg.npy', targetAnglesBackLeg)
    #numpy.save('data/targetAnglesFrontLeg.npy', targetAnglesFrontLeg)
    

    pyrosim.Prepare_To_Simulate(robotId) 
    
    #exit()
    for i in range(1000):
        #print(i)
        backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        time.sleep(1/60)
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = b'Torso_BackLeg',
            controlMode = p.POSITION_CONTROL,
            targetPosition= amplitudeBackLeg* numpy.sin(frequencyBackLeg*i +phaseOffsetBackLeg),
            #targetPosition = random.uniform(((-1)*(numpy.pi)/2),((numpy.pi)/2)),
            maxForce = 50)
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = b'Torso_FrontLeg',  
            controlMode = p.POSITION_CONTROL,
            targetPosition=amplitudeFrontLeg * numpy.sin(frequencyFrontLeg*i+ phaseOffsetFrontLeg) ,
            #targetPosition = random.uniform(((-1)*(numpy.pi)/2),((numpy.pi)/2)),
            maxForce = 50)
        p.stepSimulation()
        
    
    p.disconnect()
    #print(backLegSensorValues)
    numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
    numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)





simulate()

