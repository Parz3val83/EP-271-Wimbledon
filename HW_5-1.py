import math
import planck
import numpy as np

vCenter = 3
t = 1

#while v < 0: v = float(input('please input a value for v: '))

#planck.radiance(vCenter, t)

#defining step tables

numRows = 5
deltaV = 1
#linTable = vCenter*np.ones((numRows,2))
#cubeTable = vCenter*np.ones((numRows,4))
Table = vCenter*np.ones((numRows,2))

rows = Table.shape[0]
cols = Table.shape[1]
colCenter = (Table.shape[1]+1) * 0.5

for row in range(0, rows):
    for col in range(0, cols):
        if col < colCenter:
            Table[row, col] -= deltaV * 0.5 + deltaV * (Table.shape[1]*0.5 - col) - deltaV
        else:
            Table[row, col] += deltaV * 0.5 + deltaV * (col - Table.shape[1] * 0.5)
    deltaV *= 1/2




#print(linTable)
#print(cubeTable)
print(Table)

#in the delta_v matrix 3 is the "middle" and then our data range stretches in both directions by a constant proportional to the delta_v
