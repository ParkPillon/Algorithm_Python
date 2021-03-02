# 백준 1948 임계 경로
# https://www.acmicpc.net/problem/1948
# 임계경로 = A->B로 가장 오래걸리는 경로

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
back_graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
start_time = [0] * (n + 1)  # 마지막사람기준 각 도시에 도착하는 시각
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    back_graph[b].append((a, c))
    indegree[b] += 1
start, end = map(int, input().split())


# 탐색
queue = deque()
queue.append((start, 0))
while queue:
    now, time = queue.popleft()  # 현재 위치, 현재위치에 도달한 시각, 지나온 도로의 수
    for new, cost in graph[now]:
        indegree[new] -= 1
        start_time[new] = max(start_time[new], time + cost)
        if indegree[new] == 0:
            queue.append((new, start_time[new]))


# 역추적
checked = [0] * (n + 1)
queue.append(end)
answer = 0
while queue:
    now = queue.popleft()
    for new, cost in back_graph[now]:
        if start_time[now] - start_time[new] == cost:  # 쉬지않고 온 사람이 해당 경로 지남
            answer += 1
            if checked[new] == 0:
                checked[new] = 1
                queue.append(new)
print(start_time[end])
print(answer)