import DifferentiationAlgorithms as da
import numpy as np


print(np.cos(1))
print(da.derivativeAprox(np.sin, 1, 0.0001, 3))