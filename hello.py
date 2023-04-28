import yaml 
import math
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
#     print(i,' ',bowldata[i])
        





# for i in range(len(dum_list_pota['deliveries'])):
#     for key , value in dum_list_pota['deliveries'][i].items():
#         print(key,' ',value)


        
# CURRENT MATCH    
# (general stuff)    
bowl number 
run rate
Required run rate(0 for 1st innings)
wicket array
# bowler's performance 
current economy (runs /balls)
wicket performance (total wickets taken)
#batsmen
strike rate(runs / ball * 100)
total runs
#batsmen vs bowler
balls/runs

#PREVIOUS DATA

# bowler vs batsmen
balls vs Runs (balls / runs (discounted))
wickets (sigma wickets) (discounted)

#bowler perf
economy (runs / balls (disc))
wickets (sigma wickets (disc))

#batsmen
strike rate(average)
runs(sigma runs discounted)







   