import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    predator = sorted(map(int,input().split()))
    prey = sorted(map(int,input().split()))
    #print(predator)
    #print(prey)
    
    count = 0
    
    search_idx = len(predator)-1
    target_idx = len(prey)-1
    
    while target_idx >= 0:
        #print("search:",search_idx)
        #print("target:",target_idx)
        if predator[search_idx] == prey[target_idx]:
            count += len(predator)-(search_idx+1)
            search_idx -= 1
            target_idx -= 1
        elif predator[search_idx] < prey[target_idx]:
            count += len(predator)-(search_idx+1)
            target_idx -= 1
        elif search_idx < 0:
            count += len(predator)
            target_idx -= 1
        else:
            search_idx -= 1
        
    print(count)