board = []
output = []
for i in range(5):
    board.append(input())
    
for i in range(15):
    for j in range(5):
        if len(board[j]) >= i+1:
            output.append(board[j][i])
        else:
            continue

for i in range(len(output)):
    print(output[i],sep='',end='')
        
        
    
        
    
#1.길이가 되는가?
#2.무슨 값인가?