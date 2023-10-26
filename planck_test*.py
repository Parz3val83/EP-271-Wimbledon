#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:35:25 2023

@author: mylesjarrett
"""

import planck
nestedlist=[[1e14,4000],[5e14,4000],[5e14,2000]]


for i,newlist in enumerate(nestedlist):
    nestedlist[i].append(planck.radiance(newlist[0],newlist[1]))
    nestedlist[i].append(planck.draddnu(newlist[0],newlist[1]))    