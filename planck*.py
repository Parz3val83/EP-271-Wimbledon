#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENTER YOUR NAMES HERE.

The planck module contains a function that evaluates the
Planck radiance relation and a function that evaluates the
derivative of the radiance relation.
"""

# COMPLETE THE REMAINING ARGUMENTS THAT ARE NEEDED IN THE DEF-LINE.  ALSO,
# ADD COMMENT LINES FOR THE ARGUMENTS THAT YOU ADD.

def radiance(freq,temp,hcon=6.626e-34,kbolt=1.3807e-23,clight=2.998e8):
    """
    The radiance function evaluates Planck's radiance relation
    for power per unit area, per unit frequency, per unit solid
    angle, given the frequency and temperature.  The default
    values of the physical constants are in SI units and may
    be changed for other systems of units.

    Arguments:
    freq : real number
        frequency (1/s for SI) at which to evaluate the radiance
    temp : real number
        temperature (K for SI) at which to evaluate the radiance
    hcon : real number, optional
        Planck's constant. The default is 6.626e-34 (J-s).
    kbolt : real number, optional
        Boltzman constant. The default is 1.307e-23
    clight ; real number optional
        Speed of light. The default is 2.998e8

    Returns:
    value of the radiance (real number)
    """

    from math import exp
    from sys import exit
    
    # COMPLETE THE INPUT TESTS AND THE MATHEMATICAL OPERATIONS NEEDED
    # TO EVALUATE THE RADIANCE FORMULA WITH THE GIVEN INPUT.
    if (freq<0 or temp<0):
        exit('Please provide a positive value for temperature and frequency')
  
    elif freq==0:
        radianceval=0
    
    else:
        radianceval=(2*hcon*freq**3)/(clight**2*(exp(hcon*freq/(kbolt*temp))-1)) 
   
    return radianceval


# PREPARE THE DRADDNU FUNCTION.
def draddnu(freq,temp,hcon=6.626e-34,kbolt=1.3807e-23,clight=2.998e8):
    """
    The draddnu function evaluates the derivative of Plank's radiance relation 
    given frequency and temperature. The default values of the physical constants
    are in SI units and may be changed for other system units.
    ----------
    freq : real number
        frequency (1/s for SI) at which to evaluate draddnu
    temp : real number
        temperature (K in SI) at wich to evaluate draddnu
    hcon : real number, optional
        Planck's constant. The default is 6.626e-34.
    kbolt : real number, optional
        DESCRIPTION. The default is 1.3807e-23.
    clight : real number, optional
        speed of light. The default is 2.998e8.

    Returns
    -------
    The derivative of the radiance (real number) 

    """
    
    from math import exp
    from sys import exit
    
    if (freq<0 or temp<0):
        exit('Please provide a positive value for temperature and frequency')
    
    elif freq==0:
        draddnuval=0
   
    else:
        d1=(6*hcon*freq**2)/(clight**2*(exp((hcon*freq)/(kbolt*temp))-1))
        d2=(2*hcon**2*freq**3*exp((hcon*freq)/(kbolt*temp)))
        d3=(kbolt*temp*clight**2*((exp((hcon*freq)/(kbolt*temp))-1)**2))
        draddnuval= d1-(d2/d3)
    
    return draddnuval
    
    

    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    