import numpy as np

def firstDerivativeAprox(func, x0, h):
    return (func(x0 + h) - func(x0 - h)) / (2.0 * h)