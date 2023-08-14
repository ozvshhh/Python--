money = []
for i in range(int(input())):
    dice = list(map(int,input().split()))
    
    for i in range(1,7,1):
        if dice.count(i) == 3:
            money.append(10000+1000*i)
            break
        elif dice.count(i) == 2:
            money.append(1000+100*i)
        else:
            money.append(max(dice)*100)
print(max(money))