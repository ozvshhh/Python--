'''
air_block = 0
redstone_block = 1
redstion_dust = 2
redstion_lamp = 3

조건) 레드스톤 램프의 갯수는 1개 이상이다.
레드스톤 램프에서 부터 역으로 트랙킹 해보자.
'''
x,y = map(int,input().split())
map = [[0 for i in range(x)] for i in range(y)]
#print(map)

T = int(input())
redstone_block = 0
lamp_pos = []

for i in range(T):
    block, x, y = input().split()
    x = int(x)
    y = int(y)
    if block == "redstone_block":
        map[y][x] = 1
        redstone_block += 1
    elif block == "redstone_dust":
        map[y][x] = 2
    elif block == "redstone_lamp":
            map[y][x] = 3
            lamp_pos.append([y,x])
            
    else:
        map[y][x] = 0

print(map)

if redstone_block == 0:
    print("failed")
else:
    ramp_on = 0
    for i in range(len(lamp_pos)):#레드스톤 램프의 수 만큼 탐색 반복
        stack = []
        stack.append(lamp_pos[i])
        power = 15
        prev_pos = []
        
        for i in range(9):
            if len(stack) != 0:
                y1,x1 = stack[i]
            else:
                break
                       
            for j,k in [[1,0],[-1,0],[0,1],[0,-1]]:
                #print("y,x:",y1,x1)
                try:
                    #print("map:",map[y1+j][y1+k])
                    if map[y1+j][x1+k] == 1:
                        #레드스톤 블럭
                        #print("break")
                        ramp_on += 1
                        break
                    elif map[y1+j][x1+k] == 2:
                        stack.append([y1+j,x1+k])
                    else:
                        pass
                except IndexError:
                    pass
                
    if ramp_on == len(lamp_pos):
        print("succes")
    else:
        print("failed")