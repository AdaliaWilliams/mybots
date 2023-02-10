import numpy
import matplotlib.pyplot

targetAngles = numpy.zeros(100)
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)
backLegSensorValues = numpy.load('data/backLegSensorValues.npy', mmap_mode='r')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy', mmap_mode='r')
targetAngles =  numpy.load('data/targetAngles.npy', mmap_mode='r')
#print(backLegSensorValues)
#print(frontLegSensorValues)
print(targetAngles)
matplotlib.pyplot.plot(targetAngles, numpy.sin(targetAngles))
#matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg', linewidth = 5)
#matplotlib.pyplot.plot(frontLegSensorValues, label = 'Front Leg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()