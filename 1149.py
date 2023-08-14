'''
6
30 19 5
64 77 64
15 19 97
4 71 57
90 86 84
93 32 91


0 10 4
7 5  0
0 8  9

패턴 총 6가지
6 가지 패턴 중 제일 싼거를 구하자
R G B
R B G
G R B
G B R
B R G
B G R
'''
'''
pattern = [[0,1,2],
           [0,2,1],
           [1,0,2],
           [1,2,0],
           [2,0,1],
           [2,1,0]]
case = [[],[],[],[],[],[]]
N = int(input())
house = [[] for i in range(N)]
for i in range(N):
    house[i] = list(map(int,input().split()))

for i in range(6):
        sum = 0
        for k in range(N):
            if k%3 == 1:
                sum += house[k][pattern[i][0]]
            elif k%3 == 2:
                sum += house[k][pattern[i][1]]
            elif k%3 == 0:
                sum += house[k][pattern[i][2]]
        case[i] = sum
print(case)
'''
N = int(input())
house = [[] for i in range(N)]
for i in range(N):
    house[i] = list(map(int,input().split()))
sum = 0
for i in range(N):
    print(min(house[i]))
    sum += min(house[i])
    prev = house[i].index(min(house[i]))
    if i != N-1:
        del(house[i+1][prev])
    else:
        pass

print(sum)

39+32+37+89+11+13+29+60