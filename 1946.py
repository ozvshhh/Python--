#신입사원

import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    newbies = [tuple(map(int,input().split()))for _ in range(N)] 
    newbies.sort(key=lambda x:x[0])
    #newbies.sort(key=lambda x:x[1])
    print(newbies)
    
    '''
    [(4, 1), (3, 2), (2, 3), (1, 4), (5, 5)]
    [(6, 1), (4, 2), (7, 3), (1, 4), (2, 5), (3, 6), (5, 7)]
    '''