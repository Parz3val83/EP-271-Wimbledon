'''This is the python scrypt for Homework 4 Problem 1
    Our goal for this Prolem is to approximate the temperatures
    of a differential equation d^2T/dx^2+Q(x)=0 by incrementing
    a specified N intput over a range L

    '''
# import modules
import math
import numpy as np
import matplotlib.pyplot as plt

# user input for T values and step size
nseg = int(input("Enter N step size: "))
t_0 = float(input("Enter T initial: "))
t_L = float(input("Enter T final: "))
lseg = float(input("Enter the total range L: "))
QK = float(input("Enter the Uniform Magnitude of Q/k: "))

# initialize matrix
dones = np.ones(nseg + 1)
minone = -np.ones(nseg)
mymat = np.diag(2 * dones, 0) + np.diag(minone, -1) + np.diag(minone, 1)

rhs = np.ones((nseg + 1, 1))

confirmation = np.ones(nseg + 1)

xvals = np.ones(nseg + 1)
deltaX = lseg / nseg

for i in range(0, nseg + 1):
    rhs[i, 0] = QK * deltaX**2
    xvals[i] = i * deltaX

rhs[0] = t_0
rhs[nseg] = t_L

mymat[0, 0] = 1
mymat[0, 1] = 0
mymat[nseg, nseg] = 1
mymat[nseg, nseg - 1] = 0

soln = np.linalg.solve(mymat, rhs)

print("mymat: ", mymat)

print("rhs: ", rhs)

print("soln: ",soln)

#Please note that the rhs array needed to be transposed for the resmag calculations to work.
rhs[:]=rhs-np.dot(mymat,soln)
resmag=np.sqrt(np.dot(rhs.T,rhs))

print("resmag: ", resmag)

for j in range(0, nseg):
    confirmation[i] = t_0 + (t_L - t_0)*(xvals[i]/lseg) + 0.5*QK*xvals[i]*(lseg-xvals[i])

print("confirmation: ", confirmation)

plt.plot(soln, xvals)
plt.xlabel("Length (m)")
plt.ylabel("Temp (K)")
plt.show()
