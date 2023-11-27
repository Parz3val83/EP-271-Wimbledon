import math
import fit_data
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(r'gauss_data.txt')
xData = data[:, 0]
yData = data[:, 1]

print(fit_data.gauss_fit(np.loadtxt(r'gauss_data.txt'),True))
