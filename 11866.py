#요세푸스문제 0

'''
(7,3) 일 때
1,2,3,4,5,6,7 - 3
4,5,6,7,1,2 - 6


'''

N, K = map(int,input().split())

josephus = [i for i in range(1,N+1,1)]
output = []
while josephus:
    for i in range(K-1):
        josephus.append(josephus.pop(0))
    output.append(josephus[0])
    josephus.pop(0)

print("<",sep='',end='')
for i in range(len(output)):
    if i == len(output) - 1:
        print(output[i],sep='',end='')
    else:
        print(output[i],sep='',end=', ')
    
print(">",sep='',end='')