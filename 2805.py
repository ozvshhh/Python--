#목재절단기
'''
높이 H
그 높이에 이상은 다 절단
낮은나무 잘리지 않음
20 15 10 17 일때
높이 15이면
15 15 10 15
7미터 집에 가져감
상근이가 M미터의 나무를 가져가려면
높이를 최대 몇 H미터로 설정해야 하는가

2NlogN

나무의 최댓 값
sum(trees)

나무의 최솟값

0 ~ sum(trees) <- 이 안에는 있겠지

'''

'''
20230427

n 높이의 나무의 갯수를 n번index의 값으로 갖는 배열을 만들어보자

나무의 높이를 입력받아 trees 배열에 저장한다.
0 ~ max(trees)만큼 이진탐색을 진행하여
높이를 index값으로 갖는 나무가 몇개인지 저장한다.
가장 큰 값부터 차례대로 훑어가면서
목표한 값이 나올 때 까지 합연산을 진행한다.
-> 시간복잡도가 너무 커서 망한다.. ㅅㅂ
'''

N, M = map(int,input().split())
trees = list(map(int,input().split()))

def getBS(list):
    global M
    start = min(list)
    end = max(list)
    save = 0
    while start <= end:
        mid = (start+end)//2
        namu=get_woods(list,mid)
        if M <= namu:
            save = mid
            start = mid + 1
        else:
            print(save)
            break

def get_woods (list2,h):
    j = 0
    for i in range(len(list2)):
        if list2[i]-h > 0:
             j+= list2[i]-h
        else:
            pass
    return j
getBS(trees)