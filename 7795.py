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
    
    while target_idx >= 0 and search_idx >= 0:
        #print("search:",search_idx)
        #print("target:",target_idx)
        if predator[search_idx] == prey[target_idx]:
            count += len(predator)-(search_idx+1)
            search_idx -= 1
            target_idx -= 1
        elif predator[search_idx] < prey[target_idx]:
            count += len(predator)-(search_idx+1)
            target_idx -= 1
        elif search_idx == 0: #두 인덱스 중 하나가 끝에 있을 때 +1 씩 해준다
            count += len(predator)
            target_idx -= 1
        else:
            search_idx -= 1
        
    print(count)
    
    
    '''
    1 1=(1) 3=(3) (6)7 8
    1 3 6
    '''