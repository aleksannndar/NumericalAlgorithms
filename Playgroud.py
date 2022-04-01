import DifferentiationAlgorithms as da
import numpy as np

print(np.cos(1))
print(da.firstDerivativeApprox(np.sin, 1 ,0.001))