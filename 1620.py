#1620
#나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline


N,M = map(int,input().split())

dict={}

for n in range(1,N+1):
    poke = input().rstrip()
    dict[n]=poke
    dict[poke]=n

#print(dict)

for m in range(M):
    q = input().rstrip()
    if ord(q[0])<=58:
        print(dict[int(q)])
    else:
        print(dict[q])