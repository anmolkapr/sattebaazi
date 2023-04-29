import numpy as np
from hello import *




n,m = np.shape(vec)


inp = vec
out = outcome



params = np.zeros([1 , m])

# print(inp , out , params)

def calc_cost():
    global params , inp , out
    # print(params , inp , out)
    tmp = (inp @ params.T - out)
    return tmp

def diff_cost():
    global inp
    out = np.zeros([1 , m])
    tmp = calc_cost()
    # print(np.shape(tmp))
    for i in range(m):
        for j in range(n):
            out[0][i] += (1 / n) * tmp[j] * inp[j][i]

    return out  

def grad_desc(iter):
    global params
    for i in range(iter):
        params = params - 0.00001 * diff_cost()
        # print(params)
        # print(np.sum(calc_cost() ** 2) / (2 * n))

grad_desc(100)
print(params)


