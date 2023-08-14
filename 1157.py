word = input()

ini_list = [0 for i in range(26)]

for i in range(len(word)):
    if ord(word[i]) >= 97:
        ini_list[ord(word[i])-32-65] += 1
    else:
        ini_list[ord(word[i])-65] += 1

max_save = max(ini_list)
ini_list[ini_list.index(max(ini_list))] = -1

if max_save == max(ini_list):
    print('?')
else:
    print(chr(ini_list.index(-1)+65))