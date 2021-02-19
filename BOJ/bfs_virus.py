# 백준 2606 바이러스
# https://www.acmicpc.net/problem/2606

import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
networks = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    networks[a].append(b)
    networks[b].append(a)

visited = [False] * (N + 1)
queue = deque([1])
visited[1] = True
answer = []
while queue:
    now = queue.popleft()
    for next in networks[now]:
        if not visited[next]:
            queue.append(next)
            visited[next] = True
            answer.append(next)

print(len(answer))