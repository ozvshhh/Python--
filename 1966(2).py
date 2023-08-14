T = int(input())

for test_case in range(T):
    N,M = map(int,input().split())
    importances = list(map(int,input().split()))
    indexes = [i for i in range(N)]
    outputs = []
    
    while len(importances) != 0:
        max_value = max(importances)
        if importances[0] >= max_value:
            outputs.append(indexes[0])
        else:
            importances.append(importances[0])
            indexes.append(indexes[0])
        del(indexes[0])
        del(importances[0])
    
    print(outputs.index(M)+1)