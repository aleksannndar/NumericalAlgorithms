import numpy as np
from scipy.special import binom

#Centered Difference Quotient
def firstDerivativeAprox(func, x0, h):
    return (func(x0 + h) - func(x0 - h)) / (2.0 * h)

def derivativeAprox(func, x0, h, order):
    if(order <= 0):
        raise Exception("Order of derivative has to be higher than 0")
    sum = 0
    for k in range(0, order+1):
        sum+= (-1.0)**(k + order)*binom(order, k)*func(x0+k*h)
    
    return sum / (h**order)
