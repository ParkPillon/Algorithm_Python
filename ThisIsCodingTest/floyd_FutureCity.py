# 이코테 259p 미래 도시

import sys

INF = int(1e9)
N, M = map(int, sys.stdin.readline().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b], graph[b][a] = 1, 1
X, K = map(int, sys.stdin.readline().split())

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
answer = graph[1][K] + graph[K][X]
print(answer if answer < INF else -1)
