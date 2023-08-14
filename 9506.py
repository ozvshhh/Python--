while True:
    n = int(input())
    heathy_water_botle = []
    if n == -1:
        break
    else:
        for i in range(1,n+1,1):
            if (n//i) == (n/i):
                heathy_water_botle.append(i)
        if sum(heathy_water_botle) == 2*n:
            print(n,'= ',end='')
            for i in range(len(heathy_water_botle)-1):
                if i == len(heathy_water_botle)-2:
                    print(heathy_water_botle[i])
                else:
                    print(heathy_water_botle[i], end=' + ')
        else:
            print(f'{n} is NOT perfect.')