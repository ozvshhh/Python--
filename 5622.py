a = str(input())
add = 0

for i in range(len(a)):
    if 87 <= ord(a[i]) <= 90:
        add = add + 10
        
    elif 84 <= ord(a[i]) <=86:
        add = add + 9
        
    elif 80 <= ord(a[i]) <=83:
        add = add + 8
    else:
        add = add + ((ord(a[i])-65)//3 + 3)
print(add)
# we can use ascii code
'''ZD
a = 0
b = 1
c = 2

d = 3
e = 4
f = 5

if n//3 -> 
'''
