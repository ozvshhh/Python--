import sys

input = sys.stdin.readline

K,N = map(int,input().split())
lans = []
for i in range(K):
    lan = int(input())
    lans.append(lan)

def getNum(cut_len):
    cnt = 0
    for lan in lans:
        cnt += lan//cut_len
    return cnt

def binSearch():
    left = 0
    right = 1 << 31 
    while left+1 < right:
        mid = (left+right)//2 
        if  getNum(mid) >= N:
            left = mid
        else:
            right = mid
    #print(left,right)
    return left 

a = binSearch()  
print(a)  
    


'''
이 문제가 어렵게 느껴지는 이유
start와 end를 이용해 자연수 배열을 탐색한다.
탐색한 값을 getNum() 함수에 넣으면 값이 바뀌는데
mid 값이 작을 수록 getNum()의 return이 커지고
mid 값이 클 수록 getNum()의 return 값이 작아진다.

start와 end, mid 값은 자연수 배열을 기준으로 움직여야하고,
getNum()에 대한 비교는 역순이기에 생각을 요하는 문제이다.
2 6
100
200
50
이 경우로 생각해보자

mid :        53 52 51 50 49 48 ...... 42 41 40 39 38
getNum(mid):  4  4  4  6  6  6  66666  6  6  8  8  8

mid :        38 39 40 41 42 ...... 48 49 50  (경계) 51 52 53
getNum(mid):  8  8  8  6  6  66666  6  6  6  (경계)  4  4  4
bool       :  T  T  T  T  T  TTTTT  T  T  T          F  F  F

찾아야 하는값 : 50 <- 경계 왼쪽
값을 T F로 나눠야한다.
T의 기준: 6이상인가?
F의 기준: 6 미만인가?

T중 최댓값을 찾아야 한다.

1번코드
def binSearch():
    left = 0
    right = 1 << 31 
    while left < right:
        mid = (left+right)//2 
        if  getNum(mid) >= N:
            left = mid + 1
        else:
            right = mid - 1
    #print(left,right)
    return left 

a = binSearch()  
print(a)  

2번코드
def binSearch():
    left = 0
    right = 1 << 31 
    while left+1 < right:
        mid = (left+right)//2 
        if  getNum(mid) >= N:
            left = mid
        else:
            right = mid
    #print(left,right)
    return left 

a = binSearch()  
print(a)  
    
두 코드의 차이점은 무엇인가..

'''