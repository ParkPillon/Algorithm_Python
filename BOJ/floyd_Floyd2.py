# 백준 11780 플로이드2
# https://www.acmicpc.net/problem/11780
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
via = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        via[i][j] = i

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                via[a][b] = k

for i in range(1, n + 1):
    print(*[(x if x != INF else 0) for x in graph[i][1:]])


def findRoute(start, end):  # 최단 경로
    if via[start][end] == start:
        return [start, end]
    else:
        mid = via[start][end]  # 경유 지점
        return findRoute(start, mid) + (findRoute(mid, end))[1:]  # 경유지점이 중복되므로 한번 빼준다


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 0 or graph[i][j] == INF:
            print(0)
        else:
            route = findRoute(i, j)
            print(len(route), *route)
