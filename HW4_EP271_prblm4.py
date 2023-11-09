'''This is the python scrypt for Homework 4 Problem 1
    Our goal for this Prolem is to approximate the temperatures
    of a differential equation d^2T/dx^2+Q(x)=0 by incrementing 
    a specified N intput over a range L
    
    '''
#import modules
import math 
import numpy as np

#user input for T values and step size
nseg= int(input("Enter N step size: "))
t_0= float(input("Enter T initial: "))
t_L= float(input("Enter T final: "))
lseg= float(input("Enter the total range L: "))

#initialize matrix
dones = np.ones (nseg+1)
minone = -np.ones(nseg)
mymat = np.diag(2*dones,0)+np.diag(minone,-1)+np.diag(minone,1)
temps = np.ones((nseg+1,1))
deltaT = (t_L - t_0)/nseg
deltaX = lseg/nseg

for i in range(0, nseg+1):
    temps[i, 0] = t_0 + i*deltaT

mymat[0,0] = 1
mymat[0,1] = 0
mymat[nseg, nseg] = 1
mymat[nseg,nseg-1] = 0

solns = np.linalg.solve(mymat, temps)

ratio = solns/(deltaX**2)

ratioMag = 0.0
for j in range(0, nseg + 1):
    ratioMag += ratio[j, 0]**2
    
ratioMag = ratioMag**0.5

print(temps)

print(mymat)

print(solns)

print(ratioMag)
