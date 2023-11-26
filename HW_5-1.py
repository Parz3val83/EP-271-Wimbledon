import math
import planck
import fit_data
import numpy as np

#defining frequency table values
global vCenter, t, deltaV, numRows

#defining a function to generate a table of blackbody radiation values
def tableGen(numRows, numCols, deltaV, vCenter, t):
    Matrix = vCenter * np.ones((numRows, numCols))
    rows = Matrix.shape[0]
    cols = Matrix.shape[1]
    colCenter = (Matrix.shape[1] + 1) * 0.5
    for row in range(0, rows):
        for col in range(0, cols):
            if col < colCenter:
                Matrix[row, col] -= deltaV * 0.5 + deltaV * (Matrix.shape[1] * 0.5 - col) - deltaV
            else:
                Matrix[row, col] += deltaV * 0.5 + deltaV * (col - Matrix.shape[1] * 0.5)
        deltaV *= 1 / 2
    return Matrix

#defining step tables
V = 3
T = 1
deltaV = 0.5
NumRows = 4

linTable = tableGen(NumRows, 2, 0.5, V, T)
cubeTable = tableGen(NumRows, 4, 0.5, V, T)
quintTable = tableGen(NumRows, 6, 0.5, V, T)

#generating a matrix of solutions for the cubic table and the quintic table
cubeRads = np.ones((numRows, cubeTable[1], 2))
quintRads = np.ones((numRows, quintTable[1], 2))

for matrix in range(0, cubeRads[0]):
    for row in range(0, cubeTable[1]):
        cubRads[matrix, row, 0] = cubeTable[matrix, row]

#defining an array to store each approximations solutions
linApprox = np.ones(NumRows)
cubeApprox = np.ones(NumRows)
quintApprox = np.ones(NumRows)

#traversing each radiance matrix to generate the approximation solutions
for row in range(1, linTable.shape[0]):
    slope = (planck.radiance(linTable[row-1, 0], T) - planck.radiance(linTable[row, 1], T)) / (linTable[row-1, 0] - linTable[row, 0])
    b = planck.radiance(linTable[row, 0], T) - slope * (linTable[row, 0])
    linApprox[row] = slope * V + b

print(linApprox)
print(cubeTable)
print(quintTable)
