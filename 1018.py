M, N = map(int,input().split())
chess_board = []
w = 0
b = 0
for i in range(8):
    chess_board.append(input())
    w += chess_board[i].count('W')
    b += chess_board[i].count('B')
    

print((M*N//2)-b)
print((M*N//2)-w)


'''
32 = 현재 수 + 고칠 수

검은색 
'''