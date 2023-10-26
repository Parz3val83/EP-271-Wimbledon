#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Myles Jarrett, Cameron Patterson, Maxwell Stoughton.

This Python program uses the bisection method to find the maximum
value of Planck's blackbody radiance for a given temperature.

It usees the planck module for evaluating values of radiance
and its derivative with respect to frequency.'
"""

import planck
from math import fabs

# Start by asking the user to provide the temperature and the
# frequencies used to start the bisection method.  Check if the
# radiance derivatives at the starting frquencies have opposite
# signs, and if they don't, have the user reenter frequencies.
temperature=float(input('Enter temperature in units of K: '))
freqstring=input('Enter the two frequencies in 1/s separated by a space: ')
tolerance=float(input('Enter tolerance for calculation: '))
frequencies=[float(freqstring.split()[0]),float(freqstring.split()[1])]
drads=[planck.draddnu(frequencies[0],temperature),planck.draddnu(frequencies[1],temperature)]

i=0                 #iteration count
# COMPLETE THE REQUIRED ENTRIES FOR INPUT.

if drads[0]*drads[1]>0:
    print('Starting frequencies must contain a maximum value on there given interval')
    freqstringnew=input('Please re-enter frequencies in 1/s separated by a space: ')
    frequencies=[float(freqstringnew.split()[0]),float(freqstringnew.split()[1])]
# Here is the loop to correct if needed.  Note that the product of the
# two derivatives is less than 0 if they have opposite signs.
# COMPLETE THE EXECUTABLE LINES NEEDED TO CORRECT FREQUENCIES.
# Now start the search.  Perform this in a while loop to check whether the
# specified tolerance has been met.
# ENTER ALL OF THE NECESSARY LINES TO PERFORM THE SEARCH.
while fabs(frequencies[0]-frequencies[1])>tolerance:
    i+=1
    midpoint=fabs((frequencies[0]-frequencies[1]))/2
    dradmid=planck.draddnu(midpoint,temperature)
    if drads[0]*dradmid>0:
        frequencies[0]=midpoint
        drads[0]=dradmid
    else:
        frequencies[1]=midpoint
        drads[1]=dradmid
# Print the frequency and radiance where radiance is maximized.  Also,
# print the number of iteration steps required.
# PROVIDE LINES TO OUTPUT THE RESULTS OF THE SEARCH.

    
print('Maximum B(v) attained at frequency: ',midpoint)
print('Maximum value of B(v): ',dradmid)
print('result was found after',i,'interations')









