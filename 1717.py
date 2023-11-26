#유니온 파인드 두 집합을 합칠 때에는
#큰 집합의 요소를 작은 집합에 연결하자
import sys
sys.setrecursionlimit(2500)
N,M = map(int,input().split())

input = sys.stdin.readline


#parent = [i for i in range(N+1)]
parent = list(range(N+1))

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for m in range(M):
    c,a,b = map(int,input().split())
    
    if c == 0:
        union_parent(parent,a,b)
    elif c == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print("YES")
        else:
            print("NO")