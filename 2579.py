N = int(input())

#dp = [[0,0] for __ in range(301)]
dp = []
dp.append([[0,0]])
first_value = int(input())
dp.append([[1,first_value],[0,0]])
#print(dp[1])
for n in range(2,N+1):
    line=[]
    # print("dp",dp)
    stare = int(input())

    save1=[]
    for data in dp[n-1]:
        if data[0]>=2:
            pass
        else:
            pnt=data[1]+stare
            cnt=data[0]+1
            value = [cnt,pnt]
            # print("stare:",stare,"value:",value) 
            save1.append(value)
    line.append(max(save1,key=lambda x:x[1]))
            
    if n!=1:
    #   print(2,dp[n-2])
      save2=[]
      for data in dp[n-2]:
        pnt=data[1]+stare
        cnt=1
        value = [cnt,pnt]
        # print("stare:",stare,"value:",value)
        save2.append(value)
    line.append(max(save2,key=lambda x:x[1]))

    #print(n,"line:",line)
    #print("/line",max(line, key = lambda x:x[1]))
    dp.append(line)
    


dp[-1].sort(key = lambda x:x[1])
print(dp[-1][-1][1])