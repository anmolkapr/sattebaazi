import numpy as np
# # CURRENT MATCH    
# # (general stuff)    
# 1 bowl number 
# 2 run rate
# 3 Required run rate(0 for 1st innings)
# 4 wicket array
# # bowler's performance 
# 5 current economy (runs /balls)
# 6 wicket performance (total wickets taken)
# batsmen
# 7 strike rate(runs / ball * 100)
# 8 total runs
# #batsmen vs bowler
# 9 balls/runs

# #PREVIOUS DATA

# # bowler vs batsmen
# 10 balls vs Runs (balls / runs (discounted))
# 11 wickets (sigma wickets) (discounted)

# #bowler perf
# 12 economy (runs / balls (disc))
# 13 wickets (sigma wickets (disc))

# #batsmen
# 14 strike rate(average)
# 15 runs(sigma runs discounted)


# // 1. Model (Linear Reg with Grad Desc)
# // 2. Extract
# // 3. Run
n = 240
m = 15
inp = np.zeros([n , m])
out = np.zeros([n, 1])

for i in range(n):
    for j in range(m):
        inp[i][j] = 

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
        params = params - 0.01 * diff_cost()
        # print(params)
        # print(np.sum(calc_cost() ** 2) / (2 * n))

grad_desc(1000)
print(params)