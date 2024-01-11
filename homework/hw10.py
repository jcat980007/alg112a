import numpy as np
from scipy.optimize import root_scalar

def polynomial(x):
    """
    定義多項式方程
    """
    return x**5 + 1

# 使用root_scalar函數找到方程的根
result = root_scalar(polynomial, method='brentq', bracket=[-2, 2])

if result.converged:
    root = result.root
    print(f"The root is: {root}")
else:
    print("Unable to find a root.")