while True:
    tri = list(map(int,input().split()))
    tri.sort()
    if sum(tri) == 0:
        break
    else:
        if tri[2]**2 == tri[0]**2 + tri[1]**2:
            print('right')
        else:
            print('wrong')
