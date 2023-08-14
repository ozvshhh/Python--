N = int(input())
o =[]
high = 0
a = input()
k = map(int,a.split())
o = list(k).copy()
o.sort()
high = o[-1]
for q in range(N):
    o[q]=o[q]/high*100

print(sum(o)/N)
    
#map에 관해 notion에 노트쓰기
