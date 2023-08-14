#가장 많이 사용된 알파벳 탐색
#대문자 소문자 모두 같은 알파벳 취급한다
#출력은 대문자로만 한다.
#알파벳의 수가 똑같으면 ?를 출력한다.
#65:A ~ 90:Z -> 26개
#97:a ~ 122:z -> 26개
#대문자 10진코드 + 32 = 소문자 10진 코드
#귀찮으깐 리스트에 넣고 합을 구하면 되지 않을까?

import numpy

ini_list = [0 for i in range(26)]

word = input()

for i in range(len(word)):
    if ord(word[i]) >= 97: #소문자라면
        ini_list[ord(word[i])-32-65] += 1
    else:
        ini_list[ord(word[i])-65] += 1
ini_numpy = numpy.array(ini_list)
count_numpy=numpy.where(ini_numpy == max(ini_list))[0]

if len(count_numpy) != 1:
    print('?')
else:
    print(chr(count_numpy[0]+65))