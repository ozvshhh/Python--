T = int(input())

for i in range(T):
    stars = " "*(T-1-i)
    blanks = "*"*(i+1)
    print(stars,blanks,sep="")