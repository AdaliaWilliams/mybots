import numpy
import matplotlib.pyplot

targetAngles = numpy.zeros(1000)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
backLegSensorValues = numpy.load('data/backLegSensorValues.npy', mmap_mode='r')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy', mmap_mode='r')
targetAnglesBackLeg=  numpy.load('data/targetAnglesBackLeg.npy', mmap_mode='r')
targetAnglesFrontLeg=  numpy.load('data/targetAnglesFrontLeg.npy', mmap_mode='r')
#print(backLegSensorValues)
#print(frontLegSensorValues)
print(targetAngles)

matplotlib.pyplot.plot(targetAnglesBackLeg, label='sin data' , linewidth = 5)
matplotlib.pyplot.plot(targetAnglesFrontLeg, label='sin data' )


#matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg', linewidth = 5)
#matplotlib.pyplot.plot(frontLegSensorValues, label = 'Front Leg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()