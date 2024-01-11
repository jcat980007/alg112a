import numpy as np

step = 0.01

# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k):
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step

# 梯度：計算函數 f 在點 p 上的梯度
def grad(f, p):
    gp = np.zeros_like(p, dtype=float)
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp

# 梯度下降法：使用梯度下降找到函數 f 的最小值
def gradientDescent(f, p):
    iterations = 0
    while True:
        fnow = f(p)
        gp = grad(f, p)
        temp = p - gp * step

        fneighbor = f(temp)

        if fneighbor < fnow:
            p = temp
            iterations += 1
            print('迭代次數:', iterations, 'p =', p, 'f(p) =', fneighbor)
        else:
            break

# 範例函數：f(p) = p[0]^2 + p[1]^2 + p[2]^2
def exampleFunction(p):
    return np.sum(p**2)

# 最小值的初始猜測點
initial_point = np.array([2.0, 1.0, 3.0])

# 在範例函數上運行梯度下降
gradientDescent(exampleFunction, initial_point)