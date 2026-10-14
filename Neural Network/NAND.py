import numpy as np

def unitStep(v):
    if v>=0:
        return 1
    else:
        return 0

def perceptronModel(x,w,b):
    v=np.dot(w,x)+b
    y=unitStep(v)
    return y

def NAND_logicFunction(x):
    w=np.array([-1,-1])
    b=1.5
    return perceptronModel(x,w,b)

test1=np.array([0,0])
test2=np.array([0,1])
test3=np.array([1,0])
test4=np.array([1,1])

print("NAND ({}, {})= {}".format(0, 0, NAND_logicFunction(test1)))
print("NAND ({}, {})= {}".format(0, 1, NAND_logicFunction(test2)))
print("NAND ({}, {})= {}".format(1, 0, NAND_logicFunction(test3)))
print("NAND ({}, {})= {}".format(1, 1, NAND_logicFunction(test4)))