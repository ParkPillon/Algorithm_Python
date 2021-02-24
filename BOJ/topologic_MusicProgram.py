# 백준 2623 음악프로그램
# https://www.acmicpc.net/problem/2623

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
for _ in range(M):
    n, *temp = map(int, sys.stdin.readline().split())
    for i in range(n - 1):
        first, second = temp[i], temp[i + 1]
        graph[first].append(second)
        indegree[second] += 1

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
count = 0
answer = []
while queue:
    now = queue.popleft()
    answer.append(now)
    count += 1
    for new in graph[now]:
        indegree[new] -= 1
        if indegree[new] == 0:
            queue.append(new)

if count < N:
    print(0)
else:
    print(*answer, sep="\n")
