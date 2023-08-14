import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline
n = int(input())

synergy = []
player = [i for i in range(n)]
for i in range(n):
    synergy.append(list(map(int,input().split())))

#print(synergy)

    
def calStat(line_up):
    stat = 0
    for j in combinations(line_up,2):
        stat += (synergy[j[0]][j[1]]+synergy[j[1]][j[0]])
    return stat


Min = 9999999999
for i in combinations(player,n//2):
    link_player = deepcopy(player)
    for start_player in i:
        link_player.remove(start_player)
    start = calStat(i)
    link = calStat(link_player)
    diff = abs(start-link)
    if diff < Min:
        Min = diff

print(Min)
    