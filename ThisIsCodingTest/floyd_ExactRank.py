# 이코테 386p 정확한 순위
# K 대회
import sys

INF = int(1e9)
N, M = map(int, sys.stdin.readline().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
answer = 0
for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if j == i:
            continue
        if graph[i][j] < INF or graph[j][i] < INF:
            count += 1
    if count == N - 1:
        answer += 1
print(answer)