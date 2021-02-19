# 백준 1260 DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

N, M, start = map(int, sys.stdin.readline().split())
link = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    link[a].append(b)
    link[b].append(a)
for l in link:
    l.sort()

# dfs 수행
visited = [False] * (N + 1)
dfsRoute = []


def dfs(start):
    visited[start] = True
    dfsRoute.append(start)
    for next in link[start]:
        if not visited[next]:
            dfs(next)


dfs(start)
print(*dfsRoute)

# bfs 수행
visited = [False] * (N + 1)
bfsRoute = []


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        bfsRoute.append(now)
        for next in link[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)


bfs(start)
print(*bfsRoute)
