#안테나
#솔팅 그리디
# N 최대 200,000
# 제한시간 1초 -1억번 연산 가능
# 예상 시간복잡도 : NlogN (N^2은 400억으로 불가능함)

#논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.



'''
현준이형 코드: 중간값이 정답임.
이유는 인덱스 위치에 따라 편차합이 + 인지
-인지를 따지게 된다면 -> 결국 중간값이 출려값이 되더라

성준이코드, 집위치 유효성 검사 추가해야 통과됨
완전탐색이라서, 인덱스 잡을 때 탐색알고리즘 써서
시간복잡도 줄여줘야됨
n = int(input())
li = list(map(int, input().split()))
li.sort() #입력값

b = sum(li) // n

calc = lambda x : sum(map(lambda y: abs(y - x), li))
#시그마 합 구하는거, 어차피 (상수+상수)라 안되네;;

r = 1 #오른쪽
l = 1 #왼쪽
m = calc(b) #편차합 m
c = b #합c

while True:
    if r == None and l ==  None:
        break

    if not r == None:
        v = calc(b + r) # 편차합 +오른쪽


        if v < m:
            if m > v:
                m = v
                c = b+ r
            r += 1
        else:
            r = None



    if not l == None:
        v = calc(b - l) #편차합


        if v < m:
            l += 1
            if m > v:
                m = v
                c= b - l +1
        else:
            l = None



print(c)
'''
