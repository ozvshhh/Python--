#나무 자르기
'''
1초
나무의 수 N 1,000,000
캐야할 나무의  수 2,000,000,000
절단기 높이는 
높이 1,000,000,000

절단기의 높이를 높이면, 나무의 수가 줄어들고
절단기의 높이를 낮추면, 나무의 수가 늘어난다

절단기 높이를 세팅하는데 이진탐색을 이용 log 1,000,000,000
설정된 높이를 이용하여 나무 길이 계산 1,000,000
시간복잡도 이정도면 ㄱㅊ할듯

'''

N,M = map(int,input().split())
trees = list(map(int,input().split()))
def cutTree(cut):
    answer = 0
    for tree in trees:
        if tree-cut > 0:
            answer += tree-cut
    return answer

def BinSearch():
    start = 0
    end = max(trees)
    while start <= end:
        #print(0,start, end)
        mid = (start + end)//2
        get = cutTree(mid)
        #print(get)
        if get >= M:
            start = mid + 1
            #print(1,start,end)
        else:
            end = mid - 1
            #print(2,start,end)
    return end  
print(BinSearch())