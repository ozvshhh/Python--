S = str(input())
C_list = []

for i in range (26):
    C_list.append(-1)

for i in range (len(S)):
    if C_list[ord(S[i]) - 97] == -1: 
        C_list[ord(S[i]) - 97] = i
    else:
        continue

for i in range(26):
    print(C_list[i], end=' ')
    