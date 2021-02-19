# 플로이드 워셜 최단경로
# DP
# O(N3) 시간복잡도

import sys

INF = int(1e9)
V = int(sys.stdin.readline())
graph = [[-INF] * (V + 1) for _ in range(V + 1)]
for i in range(V + 1):
    graph[i][i] = 0
for _ in range(V):
    a, *links, _ = map(int, sys.stdin.readline().split())
    i = 0
    while i < len(links):
        graph[a][links[i]] = links[i + 1]
        i += 2

for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = max(graph[a][b], graph[a][k] + graph[k][b])

print(graph)