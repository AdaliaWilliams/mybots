import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
x1= 0
y1=0
z1= 0.5
x2 = 1
y2 = 0
z2 = 1.5


for a in range(5):
    length = 1
    width = 1
    height =1
    for i in range(10):
        pyrosim.Send_Cube(name="Box", pos=[2,a,(i+.5)] , size=[length,width,height])
        length = length * (9/10)
        width= width * (9/10)
        height = height * (9/10)
    
for b in range(5):
    length = 1
    width = 1
    height =1
    for i in range(10):
        pyrosim.Send_Cube(name="Box", pos=[1,b,(i+.5)] , size=[length,width,height])
        length = length * (9/10)
        width= width * (9/10)
        height = height * (9/10)

for c in range(5):
    length = 1
    width = 1
    height =1
    for i in range(10):
        pyrosim.Send_Cube(name="Box", pos=[0,c,(i+.5)] , size=[length,width,height])
        length = length * (9/10)
        width= width * (9/10)
        height = height * (9/10)

for d in range(5):
    length = 1
    width = 1
    height =1
    for i in range(10):
        pyrosim.Send_Cube(name="Box", pos=[(-1),d,(i+.5)] , size=[length,width,height])
        length = length * (9/10)
        width= width * (9/10)
        height = height * (9/10)

for e in range(5):
    length = 1
    width = 1
    height =1
    for i in range(10):
        pyrosim.Send_Cube(name="Box", pos=[(-2),e,(i+.5)] , size=[length,width,height])
        length = length * (9/10)
        width= width * (9/10)
        height = height * (9/10)
     
pyrosim.End()