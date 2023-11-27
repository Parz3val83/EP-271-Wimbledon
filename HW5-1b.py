import math
import planck
import fit_data
import numpy as np
import matplotlib.pyplot as plt

#defining frequency table values
global vCenter, t, deltaV, numRows

#defining a function to generate a table of blackbody radiation values
def tableGen(numRows, numCols, deltaV, vCenter, t):
    Matrix = vCenter * np.ones((numRows, numCols))
    rows = Matrix.shape[0]
    cols = Matrix.shape[1]
    colCenter = (Matrix.shape[1] + 1) * 0.5
    for row in range(0, rows):
        initial = vCenter-deltaV
        for col in range(0, cols):
            if col == 0:
                Matrix[row, col] = initial + 2*deltaV*col
        deltaV *= 1 / 2
    return Matrix

#defining a function to obtain an error value
def getError(approx, real):
    return abs((approx - real)/real)

#defining step tables
V = 3
T = 1
deltaV = 0.5
NumRows = 4

linTable = tableGen(NumRows, 2, 0.5, V, T)
cubeTable = tableGen(NumRows, 4, 0.5, V, T)
quintTable = tableGen(NumRows, 6, 0.5, V, T)

#defining an array to store each approximations solutions
linApprox = np.ones(NumRows)
cubeApprox = np.ones(NumRows)
quintApprox = np.ones(NumRows)

#defining data tables to store information for the final plot
linData = np.ones((NumRows, 2))
cubeData = np.ones((NumRows, 2))
quintData = np.ones((NumRows, 2))

#generating a matrix of solutions for the cubic table and the quintic table
cubeRads = np.ones((NumRows, cubeTable.shape[1], 2))
quintRads = np.ones((NumRows, quintTable.shape[1], 2))

for matrix in range(0, quintRads.shape[0]):
    for row in range(0, quintTable.shape[1]):
        quintRads[matrix, row, 0] = quintTable[matrix, row]
        quintRads[matrix, row, 1] = planck.radiance(quintTable[matrix, row], T)

for matrix in range(0, cubeRads.shape[0]):
    for row in range(0, cubeTable.shape[1]):
        cubeRads[matrix, row, 0] = cubeTable[matrix, row]
        cubeRads[matrix, row, 1] = planck.radiance(cubeTable[matrix, row], T)

#traversing the matricies of datapoints to generate a curve fit and calculating the approximation at V
for matrix in range(0, NumRows):
    coeffs = fit_data.poly_fit(quintRads[matrix], 5)
    quintApprox[matrix] = coeffs[0] + coeffs[1]*V + coeffs[2]*V**2 + coeffs[3]*V**3 + coeffs[4]*V**4 + coeffs[4]*V**5

for matrix in range(0, NumRows):
    coeffs = fit_data.poly_fit(cubeRads[matrix], 3)
    cubeApprox[matrix] = coeffs[0] + coeffs[1]*V + coeffs[2]*V**2 + coeffs[3]*V**3

#traversing each radiance matrix to generate the approximation solutions for the linear interpolation
for row in range(0, linTable.shape[0]):
    slope = (planck.radiance(linTable[row-1, 0], T) - planck.radiance(linTable[row, 1], T)) / (linTable[row-1, 0] - linTable[row, 0])
    b = planck.radiance(linTable[row, 0], T) - slope * (linTable[row, 0])
    linApprox[row] = slope * V + b

print(linApprox)
print(cubeApprox)
print(quintApprox)

#traversing the approximation arays to obtain error values for each
for index in range(0, NumRows):
    linApprox[index] = getError(linApprox[index], planck.radiance(V, T))
    cubeApprox[index] = getError(cubeApprox[index], planck.radiance(V, T))
    quintApprox[index] = getError(quintApprox[index], planck.radiance(V, T))
    linData[index] = [deltaV * 0.5**index, linApprox[index]]
    cubeData[index] = [deltaV * 0.5 ** index, cubeApprox[index]]
    quintData[index] = [deltaV * 0.5 ** index, quintApprox[index]]

print(linApprox)
print(cubeApprox)
print(quintApprox)

#plotting...
x1, y1 = zip(*linData)
x2, y2 = zip(*cubeData)
x3, y3 = zip(*quintData)

plt.loglog(x1, y1, color='r', label='linear approximation error')
plt.loglog(x2, y2, color='g', label='Cubic approximation error')
plt.loglog(x3, y3, color='b', label='Quintic approximation error')

#configuring the plot
plt.xlabel('Step size')
plt.ylabel('Error')
plt.title('Log-Log Plot of Error vs Step Size for First Interval Frequency Center')
plt.legend()

plt.show()
