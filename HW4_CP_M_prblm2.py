""" Problem #2
    In this problem matricies are again used to represent a differntial equation
    The User will imput the bounds and step size
    then the program with out put a plot and a matrix representation
    
    Cameron Patterson and Max
"""
import math
import numpy as np
import matplotlib.pyplot as plt



#step 1: find N segmests and domain
nseg = int(input("Enter the number of segments: "))
h = float(input("Enter the floating point timestep limiting value: "))

deltaX = 2/nseg
deltaT = h*deltaX

#step 2: input x values for j
xVals = np.ones(nseg)
fVals = np.ones(nseg)
farr = np.ones(nseg)

#step 3: initialize array 
for j in range(0, nseg-1):
    xVals[j] = -1 + j * deltaX
    fVals[j] = 1 + math.cos(math.pi * xVals[j])
    farr[j] = 1 + math.cos(math.pi * xVals[j])

#step 4: format correct array
offd=0.5*h*np.ones(nseg-1)
mat=np.diag(offd,-1)-np.diag(offd,1)

mat[0,nseg-1] = h/2
mat[nseg-1,0] = -h/2

#step 5: compute dot product of f_j and matrix
fpre=farr+0.5*np.dot(mat,farr)
farr += np.dot(farr, fpre)

#step 6: print and plot relationship
print('\n'+'*Spatial Differential Operaltion matrix representation*'+'\n' + str(mat)+'\n')
print("*Dot product of half of differntial matirx(mat) and existing matrix(f_j)*"+"\n", str(farr))

plt.plot(farr, xVals)
plt.xlabel("X Axes")
plt.ylabel("f_j values")
plt.show()