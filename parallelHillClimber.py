from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents= {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION()
        #print(self.parents)

    def Evolve(self):
        for i in range(c.populationSize):
            self.parents[i].Evaluate("GUI")
        #for currentGeneration in range(c.numberOfGenerations):
           # self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()


    def Spawn(self):
        self.child = copy.deepcopy(self.parents)

    def Mutate(self):
        self.child.Mutate()
        print("parents weight:")
        print(self.parent.weights)
        print("child weight:")
        print(self.child.weights)
        

    def Select(self):
        if self.parents.fitness < self.child.fitness:
            self.parents.fitness = self.child.fitness

    def Print(self):
        print("parent fitness: ", self.parents.fitness, " child fitness: ", self.child.fitness)

    def Show_Best(self):
        pass
        #self.parent.Evaluate("GUI")