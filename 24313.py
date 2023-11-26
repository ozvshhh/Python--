a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

#O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
#f(n) = 7n + 7, g(n) = n, c = 8, n0 = 1이다. f(1) = 14, c × g(1) = 8이므로 O(n) 정의를 만족하지 못한다.

state = 1

for i in range(n0,101):
    if a1*i + a0 > c*i:
        state = 0
        break
print(state)
        
        
