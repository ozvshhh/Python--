LMI=lambda:list(map(int,input().split()))
II=lambda:int(input())

def binarySearch(L,value):
    start = 0
    end = len(L)-1
    while start <= end:
        mid = (start+end)//2
        if value > L[mid]:
            start = mid+1
        elif value < L[mid]:
            end = mid-1
        else:
            return 1
    return 0
            
                        
    

for i in range(II()):
    N = II()
    lst1 = sorted(LMI())
    M = II()
    lst2 = LMI()
    
    for j in range(len(lst2)):
        print(binarySearch(lst1,lst2[j]))
        
        
