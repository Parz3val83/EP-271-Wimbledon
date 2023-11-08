'''This is the pytho scrypt for Homework 4 Problem 1
    Our goal for this Prolem is to approximate the temperatures
    of a differential equation d^2T/dx^2+Q(x)=0 by incrementing 
    a specified N intput over a range L
    
    '''
#import modules
import math 
import numpy as np

#user input for T values and step size
nseg= input("Enter N step size: ")
t_0=input("Enter T initial: ")
t_L=input("Enter T final: ")
lseg=input("Enter the total range L: ")

#initialize matrix
dones=np.ones(nseg+1)
minone=-np.ones(nseg)
mymat=np.diag(2*dones,0)+np.diag(minone,-1)+np.diag(minone,1)


