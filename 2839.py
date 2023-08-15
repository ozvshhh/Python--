#설탕배달
#그리디 -> 걍 다 ㅈ까고 조합 시전 -> DFS

from itertools import combinations

n = int(input())
nums = []



# #55
# if n%5 == 0:
#     grd.append(n//5)
# #33
# if n%3 == 0:
#     grd.append(n//3)

# #53
# if True:
#     nn = n
#     count = 0
#     while True:
#         if nn >= 5:
#             nn -=5
#             count +=1
#         elif nn >= 3:
#             nn -=3
#             count +=1
#         else:
#             break
#     #print(n)
#     if nn == 0:
#         grd.append(count)

# if True:
#     nn = n
#     count = 0
#     while True:
#         if nn >= 3:
#             nn -=3
#             count +=1
#         elif nn >= 5:
#             nn -=5
#             count +=1
#         else:
#             break
#     #print(n)
#     if nn == 0:
#         grd.append(count)

# if grd:
#     print(min(grd))
# else:
#     print(-1)