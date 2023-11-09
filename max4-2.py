import math
import numpy as np
import matplotlib.pyplot as plt

nseg = int(input("Enter the number of segments: "))
h = float(input("Enter the floating point timestep limiting value: "))

deltaX = 2/nseg
deltaT = h*deltaX

xVals = np.ones(nseg)
fVals = np.ones(nseg)

for j in range(0, nseg-1):
    xVals[j] = -1 + j * deltaX
    fVals[j] = 1 + math.cos(math.pi * xVals[j])

offd=0.5*h*np.ones(nseg-1)
mat=np.diag(offd,-1)-np.diag(offd,1)

print(mat)
