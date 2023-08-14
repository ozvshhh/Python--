N,M = map(int,input().split())
relation = [[],[],[],[],[]]
kevin = []

def insertNum (one, two):
    if two in relation[one-1]:
        pass
    else:
        relation[one-1].append(two)

# def subtractList(main,*subs): #main list에 subs값들 더하는 함수
#     global 
#     for i in subs:
#         for j in i:
#             if j in main:
#                 del(main.index(j))
#             else:
#                pass 
#     return main
    

for i in range(M): #input
    m1, m2 = map(int,input().split())
    insertNum(m1,m2)
    insertNum(m2,m1)

for i in range(len(relation)): #sort
    relation[i] = sorted(relation[i])
print(relation)


'''
[1,2,3,4,5]
[[0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 0, 0, 1, 0]]
'''

'''
접근여부를 따져봐야하겠다.
큐를 사용하여 탐색 순서를 정한다.
내가 서칭하는 값과 다른 값의 접근 여부를 판단한다.
접근 여부를 판단하기 위해서 중복되는 값은 제거해준다.

거리를 어찌 탐색할까?
거리 판단을 위한 list
[1,[1이랑 근접한 수],[1이랑 근접한 수랑 근접한 수 1은 제외], ... 이런식으로 하면 될 듯 ]

1의 값을 순회 : 3 ,4  이 값들로 한 계산은 +1임
3 값을 순회
4  값을 순회
[[1],[3,4],[2,5]] 이런식의 배열을 만들어볼까?
거리를 판단하는 방법
if value in relation[distance[0]]
'''

bacon =[0 for i in range(N)] #결과
queue = [1] #탐색과정 너비우선탐색
check = [1] #탐색과정 중복제거
distance = [[1]] #distance값을 index로 지님

'''
queue의 0 번째 값에 근접한 값을 배열에 넣는다
단 check에 등록된 값은 넣지 않는다
[[1],[3,4],[2,5]]

거리를 어케 둘 것인가
탐색과정에서 거리는 늘어나기만 한다.
거리가 늘어날 조건은 전의 탐색 값을 부모로 두는가? 여부이다.
1을 최초값으로 둔다면 parent in realtion[queue[0]-1]


'''



    


# queue []


'''
친구 관계는 중복되어 들어올 수도 있으며 - 해결
1,3
1,4
4,5
4,3
3,2

1 - 3,4
2 - 3
3 - 1,2,4
4 - 1,3,5
5 - 4
`
[[3,4],[3],[1,2,4],[1,3,5],[4]]

이제 관계도를 계산해보자
관계도의 초기값은 0이다.
관계도 배열의 모든 값이 0보다 크면 코드를 멈춘다
1번의 1단계 친구의 수를 확인한다 2명 -> 2 * 1 = 2

서칭이 중요한것 아니겠습니까?
서칭 알고리즘을 짜봅시다.
[[0,1,0],
[1,0,0],
[0,1,1]]
<- 이런 이중 배열이 있다

두가지 방법을 제시한다.
1의 위치를 따로 기록해놓고,
1의 위치에 따른 인덱스를 조사한다



다시 새로운 방법을 고안해보자

이러한 방식은 너비 우선 탐색과 비슷해 보인다.
너비우선 탐색에서 중요한 것은, 탐색의 우선순위이다.
두번째는 방문여부를 표현할 것인가? 이다.
큐:선입선출 을 사용하자
예시로 굴리고 있는 테스트케이스의 큐를 따라가보면
[3]
[3,4] #relation[0] 값 추가
[2,5] #3,4 값 제거하고 relation[2],relation[3] 값에서 bacon 리스트 안에있는 값 제거하고 추가
[]# 더 추가할 값이 없을 때 까지 진행
이렇게 진행될 듯?
방문여부는 bacon 리스트를 통해서 기록하면 될듯

relation의 이중 리스트를 이용해 볼 것이다.
stack 이라는 변수도 함께 쓰자

stack 을 1로 선언한다
relation[0]에 있는 리스트를 저장한다.
relation[0]-1 의 값을 인덱스로 가지는 bacon 배열의 값을 stack으로 바꾼다
relation[0]

씨발 이거 왤케 어렵냐 진짜 현타온다
빨리 알고리즘 공부를 해야지 개빡쎄네 허허
'''


'''
김연경 선생님의 도움을 받았습니다
[[node value, node height],[],[]] 이런 이중 배열을 만들어서 값을 탐색하면 된다고 생각합니다.
'''