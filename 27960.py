#사격내기
#2^n으로 나타낼 수 있는가


bins = [2**i for i in range(9,-1,-1)]
a_count = [False for _ in range(10)]
b_count = [False for _ in range(10)]

A,B = map(int,input().split())

for i,subtract in enumerate(bins):
    if A >= subtract:
        A -= subtract
        a_count[i] = True  
    if B >= subtract:
        B -= subtract
        b_count[i] = True  

# print(a_count)
# print(b_count)

c_count = [False for _ in range(10)]

for i in range(10):
    if a_count[i] != b_count[i]:
        c_count[i] = True

# print("a",a_count)
# print("b",b_count)
# print("c",c_count)

c = 0 
for i,bool in enumerate(c_count):
    if bool:
        c += 2**(9-i)
print(c)