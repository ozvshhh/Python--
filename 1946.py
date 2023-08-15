#신입사원

import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    applicant = [tuple(map(int,input().split()))for _ in range(N)]
    passer = []
    
    #(doc,interview)
    applicant_document = deque(sorted(applicant,key=lambda x:x[0]))
    applicant_interview = deque(sorted(applicant,key=lambda x:x[1]))
    
    
    n2 = applicant_document[0][1]
    n1 = applicant_interview[0][0]
    
    
    passer.append(applicant_document[0])
    passer.append(applicant_interview[0])

    #배열 범위 줄이기
    applicant_document.popleft()
    applicant_interview = applicant_interview[1:n2-1]
    
    print(applicant_document)
    print(applicant_interview)
    
    #중복되는 값 찾아서 passer에 저장하기
    for i in range(len(applicant_document)):
        for j in range(len(applicant_interview)):
            if applicant_document[i] == applicant_interview[j]:
                passer.append(applicant_document[i])
        
    print(len(passer))
                
    
'''
[(2, 3), (3, 2)]
[(3, 2), (2, 3)]
[(2, 5), (3, 6), (4, 2), (5, 7)]
[(4, 2), (7, 3)]

지원자 배열과
합격자 배열을 만든다.

각 배열을 오름차순으로 정렬한다, key 값이 2개 임으로 이때 배열이 2개 생성된다.
서류등수 배열에서 가장 등수가 높은 참가자(0번 인덱스)의 면접등수를 저장한다.
popleft한 뒤 합격자 배열에 넣어준다.
면접등수 배열에서도 똑같이 해준다.  

저장된 등수를 이용해 배열을 선형탐색해주고,
적당한 값이 있다면 합격자 배열에 저장한다.

합격자 배열에서 저장된 등수를 업데이트한다.
'''