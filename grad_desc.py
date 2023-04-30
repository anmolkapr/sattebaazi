import numpy as np
from hello import *

def shuffle_in_unison(a, b):
        assert len(a) == len(b)
        shuffled_a = np.empty(a.shape, dtype=a.dtype)
        shuffled_b = np.empty(b.shape, dtype=b.dtype)
        permutation = np.random.permutation(len(a))
        for old_index, new_index in enumerate(permutation):
            shuffled_a[new_index] = a[old_index]
            shuffled_b[new_index] = b[old_index]
        return shuffled_a, shuffled_b


n,m = np.shape(vec)



inp = vec
out = outcome



params = np.zeros([1 , m])

# print(inp , out , params)
inp , out = shuffle_in_unison(inp, out)
        

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
        print(np.sum(calc_cost() ** 2) / (2 * n))

grad_desc(20)


print(params)

ct = 0
ctdum = 0
totct = 0
for i in vec:
    outputprob = np.inner(i,params)
    if outputprob > 0.6:
        if outcome[totct] == 0 and vec[totct][0] > 60 :
            ct += 1
        ctdum += 1
    elif outputprob < 0.4 and vec[totct][0] > 60:
        if outcome[totct] == 1:
            ct += 1
        ctdum += 1
    totct += 1
    
    
print(100 - (ct / ctdum) * 100)

