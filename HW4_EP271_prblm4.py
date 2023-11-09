'''This is the python scrypt for Homework 4 Problem 1
    Our goal for this Prolem is to approximate the temperatures
    of a differential equation d^2T/dx^2+Q(x)=0 by incrementing
    a specified N intput over a range L

    '''
#answer questions here and dont forget the Sypder variable explorer part!

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

# initialize matricies
dones = np.ones(nseg + 1)
minone = -np.ones(nseg)
mymat = np.diag(2 * dones, 0) + np.diag(minone, -1) + np.diag(minone, 1)
rhs1 = np.ones((nseg + 1, 1))
rhs2 = np.ones((nseg + 1, 1))
confirmation = np.ones((nseg + 1, 1))
xvals = np.ones(nseg + 1)

# define change in x
deltaX = lseg / nseg

# define matricy values
for i in range(0, nseg + 1):
    rhs1[i, 0] = QK * deltaX**2
    rhs2[i, 0] = QK * math.exp(-(4*i/lseg - 2)**2)
    xvals[i] = i * deltaX

rhs1[0] = t_0
rhs1[nseg] = t_L

mymat[0, 0] = 1
mymat[0, 1] = 0
mymat[nseg, nseg] = 1
mymat[nseg, nseg - 1] = 0

# solving both cases
soln1 = np.linalg.solve(mymat, rhs1)
soln2 = np.linalg.solve(mymat, rhs2)

#Please note that the rhs array needed to be transposed for the resmag calculations to work.
rhs1[:]=rhs1-np.dot(mymat,soln1)
resmag=np.sqrt(np.dot(rhs1.T,rhs1))

#defining the confirmation matrix
for j in range(0, nseg):
    confirmation[j, 0] = t_0 + (t_L - t_0)*(xvals[j]/lseg) + 0.5*QK*xvals[j]*(lseg-xvals[j])

#print("confirmation: ", confirmation)

#plotting
plt.plot(soln1, xvals)
plt.xlabel("Length (m)")
plt.ylabel("Temp (K)")
plt.show()
plt.savefig("uniformQ_Temp.jpg")

plt.plot(soln2, xvals)
plt.xlabel("Length (m)")
plt.ylabel("Temp (K)")
plt.show()
plt.savefig("gaussianQ_temp.jpg")
