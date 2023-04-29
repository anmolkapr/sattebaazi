import yaml 
import math
import numpy as np
user_list = {}
with open(r'data.yaml') as file:
    user_list = yaml.load(file,Loader = yaml.FullLoader)
    # print(user_list)

dum_list = user_list['innings']
dum_list_beta = dum_list[0]
dum_list_pota = dum_list_beta['1st innings']

batsmen = set([])
bowlers = set([])


for i in range(len(dum_list_pota['deliveries'])):
    for key , value in dum_list_pota['deliveries'][i].items():
        # print(key , value)
        batsmen.add(value['batsman'])
        batsmen.add(value['non_striker'])
        bowlers.add(value['bowler'])

batsdata = {}
bowldata = {}

for i in batsmen:
    bowlertemp = {}
    for j in bowlers: 
        bowlertemp[j] = 0
    batsdata[i] = {'runs': 0 , 'balls' :0, 'bowlname' : bowlertemp}

for i in bowlers:
    batsmenname = {}
    for j in batsmen: 
        batsmenname[j] = 0
    bowldata[i] = {'balls' : 0, 'runs': 0 , 'wickets' : [],'batsname' : batsmenname}




for i in range(len(dum_list_pota['deliveries'])):
    for key , value in dum_list_pota['deliveries'][i].items():
        #adding batting data
        batsdata[value['batsman']]['runs'] += value['runs']['total']
        batsdata[value['batsman']]['balls'] += 1
        batsdata[value['batsman']]['bowlname'][value['bowler']] += value['runs']['total']

        #adding bowling data
        bowldata[value['bowler']]['balls'] += 1
        bowldata[value['bowler']]['runs'] += value['runs']['total']
        bowldata[value['bowler']]['batsname'][value['batsman']] += value['runs']['total']

        if 'wicket' in value:
            bowldata[value['bowler']]['wickets'].append(value['wicket']['player_out'])

# for i in bowldata:
#     # print(i,' ',bowldata[i])
        
# # CURRENT MATCH    
# # (general stuff)   ✅ 
# 1 bowl number ✅
# 2 run rate ✅
# 3 Required run rate(0 for 1st innings) ✅
# 4 wicket array ✅
# # bowler's performance ✅
# 5 current economy (runs /balls)✅
# 6 wicket performance (total wickets taken)✅
# batsmen✅
# 7 strike rate(runs / ball * 100)✅
# 8 total runs✅
# #batsmen vs bowler✅
# 9 runs/balls✅

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


totruns = 0 
bowlnum = 0
target = 0
innings = 0

vec = np.zeros([124,24])

wickets = np.zeros(10)
wicketct = 0
wickets[0] = 1
bowlerperf = {}
dumdictb = {}
batsmanperf = {}
for i in range(len(dum_list_pota['deliveries'])):
    for key , value in dum_list_pota['deliveries'][i].items():
        bowlername = value['bowler']
        batsmanname = value['batsman']
        dumdictb[batsmanname + ' to ' + bowlername] = [0,0]
        bowlerperf[bowlername] = [0,0,0]
        batsmanperf[batsmanname] = [0,0]


# print(bowlerperf)

for i in range(len(dum_list_pota['deliveries'])):
    for key , value in dum_list_pota['deliveries'][i].items():
        # print(key,' ',value)
        bowlnum += 1
        totruns += value['runs']['total']
        vec[bowlnum - 1][0] = bowlnum

        vec[bowlnum - 1][1] = totruns/bowlnum

        vec[bowlnum - 1][2] = (target - totruns)/(125 - bowlnum)*(innings)

        
        flg = 0

        if 'wicket' in value:
            wickets[wicketct] = 0
            wicketct += 1
            flg = 1
            wickets[wicketct] = 1

        for j in range(10):
            vec[bowlnum-1][3+j] = wickets[j]

        bowlername = value['bowler']
        batsmanname = value['batsman']

        bowlerperf[bowlername][0] += value['runs']['total']
        bowlerperf[bowlername][1] += flg
        bowlerperf[bowlername][2] += 1
        
        dumdictb[batsmanname + ' to ' + bowlername][0] += value['runs']['total']
        dumdictb[batsmanname + ' to ' + bowlername][1] += 1
        
        # current economy (runs /balls)
        vec[bowlnum - 1][13] = bowlerperf[bowlername][0]/bowlerperf[bowlername][2]

        # wicket performance (total wickets taken)
        vec[bowlnum - 1][14] = bowlerperf[bowlername][1]
        

        batsmanperf[batsmanname][0] += value['runs']['total']
        batsmanperf[batsmanname][1] += 1

        # strike rate(runs / ball * 100)
        vec[bowlnum - 1][15] = (batsmanperf[batsmanname][0]/batsmanperf[batsmanname][1])*100.00
        
        # total runs
        vec[bowlnum - 1][16] = batsmanperf[batsmanname][0]

        # runs/balls
        if dumdictb[batsmanname + ' to ' + bowlername][0] != 0:
            vec[bowlnum - 1][17] = dumdictb[batsmanname + ' to ' + bowlername][0]/dumdictb[batsmanname + ' to ' + bowlername][0]




        

        
        
        
        
        
        





# for i in range(len(dum_list_pota['deliveries'])):
#     for key , value in dum_list_pota['deliveries'][i].items():
#         print(key,' ',value)
#         




for i in vec:
    print(i)

    
