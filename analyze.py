import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)
backLegSensorValues = numpy.load('data/backLegSensorValues.npy', mmap_mode='r')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy', mmap_mode='r')
print(backLegSensorValues)
print(frontLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg', linewidth = 5)
matplotlib.pyplot.plot(frontLegSensorValues, label = 'Front Leg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()