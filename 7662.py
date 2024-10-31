#7662
#이중 우선순위 큐
'''
문제
1. 최솟값과 최댓값을 항상 알고 있어야한다.
2. 큐에서 처럼 입력순서를 기록해야한다.

해결책

아니 그냥 문제 제목에서 답을 알려주는구나
우선순위 큐를 두개 돌려서
하나는 max우선순위큐 하나는 min우선순위큐 돌리면 된다.
최대힙 최소힙 문제임

--------------------------------------------------

여기서 문제!
숫자가 중복으로 들어오는 경우가 문제가 되는디;;
최대힙 최소힙을 쓸때는 각 최솟값 최댓값만 수정되다 보니
다른 값들이 남아돈다..
이때 삭제되지 않고 남아있던 다른 값을이 결과에 영향을 미치는 것 같다.

이걸 해결하는 방법은 중복 값을 따로 관리하면 된다!
해당 값이 중복되는 값이면 push를 제한적으로 하는 것이다.
그리고 값을 삭제시킬 때에는 중복값을 관리하는 녀석의 값도 같이 삭제!

'''

import sys
input = sys.stdin.readline

import heapq

T = int(input())

for t in range(T):
    Q=int(input())
    minHeap = []
    maxHeap = []
    emptyCheck = []
    nums = dict()
    for q in range(Q):
        com,num = input().split()
        num = int(num)
        # print(nums)
        if com == 'I':
            if num in nums:
                nums[num]+=1
                heapq.heappush(maxHeap,num)
                heapq.heappush(minHeap,(-num,num))
                emptyCheck.append(1)
            else:
                heapq.heappush(maxHeap,num)
                heapq.heappush(minHeap,(-num,num))
                emptyCheck.append(1)
                nums[num] = 1
        elif com == 'D':
            if num == -1:
                if len(minHeap)==1:
                    heapq.heappop(minHeap)
                while maxHeap:
                    if nums[maxHeap[0]] != 0:
                        nums[maxHeap[0]]-=1
                        
                        if nums[maxHeap[0]]>=1:
                            pass
                        else:
                            heapq.heappop(maxHeap)
                        break
                    else:
                        heapq.heappop(maxHeap)

                    
            if num == 1:
                if len(maxHeap)==1:
                    heapq.heappop(maxHeap)
                while minHeap:
                    if nums[minHeap[0][1]] != 0:
                        nums[minHeap[0][1]]-=1
                        
                        if nums[minHeap[0][1]]>=1:
                            pass
                        else:
                            heapq.heappop(minHeap)
                        break
                    else:
                        heapq.heappop(minHeap)

            if len(emptyCheck)>0:
                emptyCheck.pop()
        
        # print(q,":",com,num)
        # print("min:",minHeap)
        # print("max:",maxHeap)
        # print("nums:",nums)
        # print("-"*20) 

    # for min in minHeap:
    #     if nums[min[1]]==0:
    #         heapq.heappop(minHeap)
    #     else:
    #         break

    # for max in maxHeap:
    #     if nums[max]==0:
    #         heapq.heappop(maxHeap)
    #     else:
    #         break
    
    # print("end")
    # print("min:",minHeap)
    # print("max:",maxHeap)
    # print("nums:",nums)
    # print("-"*20) 

    if len(emptyCheck) == 0:
        print("EMPTY")
    else:
        for min in minHeap:
            if nums[min[1]]>0:
                print(min[1],end=" ")
                break
        for max in maxHeap:
            if nums[max]>0:
                print(max)
                break




