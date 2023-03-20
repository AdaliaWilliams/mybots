import numpy 

class SOLUTION:
    def __init__(self):
        #create a 3 row and 2 column matrix of random values called self.weights
        self.weights = numpy.random.rand(3,2)
        
        self.weights = (self.weights*2)-1
        
    
    def Evaluate(self):
        pass