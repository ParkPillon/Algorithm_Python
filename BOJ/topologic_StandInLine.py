# 백준 2252 줄 세우기
# https://www.acmicpc.net/problem/2252

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque([])
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
result = []
while queue:
    now = queue.popleft()
    result.append(now)
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)
print(*result)
