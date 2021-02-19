# 백준 2056 작업
# https://www.acmicpc.net/problem/2056


import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
costs = [0] * (N + 1)
indegree = [0] * (N + 1)

for a in range(N):
    cost, n, *prerequisites = map(int, sys.stdin.readline().split())
    indegree[a + 1] += n  # (a+1)의 진입차수 n
    costs[a + 1] = cost
    for b in prerequisites:  # (a+1)의 선행 작업 b
        graph[b].append(a + 1)

start_time = [0] * (N + 1)  # 작업을 시작할 수 있는 시간
answer = 0
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:  # 진입차수가 0인 작업; 바로 시작할 수 있는 작업
        queue.append((i, costs[i]))
while queue:
    now, end_time = queue.popleft()
    answer = max(answer, end_time)
    for new in graph[now]:
        indegree[new] -= 1
        start_time[new] = max(start_time[new], end_time)
        if indegree[new] == 0:
            queue.append((new, start_time[new] + costs[new]))

print(answer)