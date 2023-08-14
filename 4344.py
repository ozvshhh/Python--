C = int(input())
test_case = []

for i in range(C):
    test_case = list(map(int,input().split()))
    del test_case[0]
    average = sum(test_case)/len(test_case)
    over_avr = 0
    
    for i in range(len(test_case)):
        if test_case[i] > average:
            over_avr += 1
        else:
            continue
    
    rate = (over_avr/len(test_case))*100
    print(format(rate,'.3f'),'%',sep='')