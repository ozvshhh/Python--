N = int(input())

dp = [0 for __ in range(301)]

dp[0] = [0,0]

for n in range(1,N+1):
    print(dp)
    stare = int(input())
    line=[]
    
    if dp[n-1][0]>=2:
        pass
    else:
        print(1,dp[n-1])
        pnt=dp[n-1][1]+stare
        cnt=dp[n-1][0]+1
        value = [cnt,pnt]
        print("stare:",stare,"value:",value) 
        line.append(value)
    
    if n!=1:
      print(2,dp[n-1])
      pnt=dp[n-2][1]+stare
      cnt=0
      value = [cnt,pnt]
      print("stare:",stare,"value:",value)
      line.append(value)

      dp[n]=line
    
print(*dp)