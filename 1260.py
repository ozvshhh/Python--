N,M,V = map(int(input().split()))

graph = [[]for _ in range(N)]


def fill_graph(start,end):
    graph[start].append(end)


for m in M:
    start, end = map(int(input()))  
    fill_graph(start,end)

print(graph)