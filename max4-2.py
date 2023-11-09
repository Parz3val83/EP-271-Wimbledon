import math
import numpy as np
import matplotlib.pyplot as plt
nseg = int(input("Enter the number of segments: "))
h = float(input("Enter the floating point timestep limiting value: "))

deltaX = 2/nseg
deltaT = h*deltaX

xVals = np.ones(nseg)
farr = np.ones(nseg)

for j in range(0, nseg-1):
    xVals[j] = -1 + j * deltaX
    farr[j] = 1 + math.cos(math.pi * xVals[j])

offd=0.5*h*np.ones(nseg-1)
mat=np.diag(offd,-1)-np.diag(offd,1)

mat[0,nseg-1] = h/2
mat[nseg-1,0] = -h/2

fpre=farr+0.5*np.dot(mat,farr)
farr += np.dot(farr, fpre)

print(mat)
print("dot: ", farr)
plt.plot(farr, xVals)
plt.show()
