import yaml 
import math
import numpy as np
user_list = {}
with open(r'data.yaml') as file:
    user_list = yaml.load(file,Loader = yaml.FullLoader)
    
    # winner = user_list['outcome']['winner']
    


winner = user_list['info']['outcome']['winner']

def inningsextract(innings):

    dum_list = user_list['innings']
    var = 0
    if innings == '2nd innings':
        var = 1
    
    dum_list_beta = dum_list[var]
    
    win = 0

    dum_list_pota = dum_list_beta[innings]
    # print(dum_list_pota['team'])
    if dum_list_pota['team'] == winner:
        win = 1

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

    return dum_list_pota,win





# for i in bowldata:
#     # print(i,' ',bowldata[i])
        
# # CURRENT MATCH    
# # (general stuff)   ✅ 
# 1 bowl number ✅✅
# 2 run rate ✅✅
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

# bowler vs batsmen
# 10 balls vs Runs (balls / runs (discounted))
# 11 wickets (sigma wickets) (discounted)

# bowler perf
# 12 economy (runs / balls (disc))
# 13 wickets (sigma wickets (disc))

# batsmen  
# 14 strike rate(average)
# 15 runs(sigma runs discounted)

def vectorcreate(dum_list_pota):

    totruns = 0 
    bowlnum = 0
    target = 0
    innings = 0

    

    

    wickets = np.zeros(10)
    wicketct = 0
    wickets[0] = 1
    bowlerperf = {}
    dumdictb = {}
    batsmanperf = {}

    for i in range(len(dum_list_pota['deliveries'])):
        for key , value in dum_list_pota['deliveries'][i].items():
            bowlnum += 1
    
    # for i in range(len(dum_list_pota['deliveries'])):
    #     for key , value in dum_list_pota['deliveries'][i].items():
    #         print(key , ' ' ,value)
    
    # print()

    vec = np.zeros([bowlnum,24])
    bowlnum = 0
    

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
                if wicketct == 10:
                    break

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
    
    return vec
    


dum_list_pota1, winfg1 = inningsextract('1st innings')
dum_list_pota2, winfg2 = inningsextract('2nd innings')   

vec1 = vectorcreate(dum_list_pota1)
vec2 = vectorcreate(dum_list_pota2)
sz1 = np.shape(vec1)[0]
sz2 = np.shape(vec2)[0]

vec = np.concatenate((vec1, vec2), axis= 0)

outcome = np.zeros([(np.shape(vec)[0]),1])

for i in range(sz1 + sz2):
    if i < sz1 : 
        outcome[i] = winfg1
    else :
        outcome[i] = winfg2

    
    









        
        
        





# for i in range(len(dum_list_pota['deliveries'])):
#     for key , value in dum_list_pota['deliveries'][i].items():
#         print(key,' ',value)
#         




# for i in range(20):
#     print(vec[i])
    


