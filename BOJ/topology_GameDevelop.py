# 백준 1516 게임 개발
# https://www.acmicpc.net/problem/1516

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]  # 건물들의 선행 관계
indegree = [0] * (N + 1)  # 건물을 짓기 전에 지어야 하는 건물 수
costs = [0] * (N + 1)  # 건물 짓는데 소요되는 시간
start_time = [0] * (N + 1)  # 건물 지을 수 있는 최소 시각
for i in range(1, N + 1):
    cost, *precede, _ = map(int, input().split())
    costs[i] = cost
    for p in precede:
        graph[p].append(i)
        indegree[i] += 1

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append((i, costs[i]))

answer = [0] * (N + 1)  # 건물이 지어지는 최소 시각
# 탐색 시작
while queue:
    now, end_time = queue.popleft()  # 현재 짓는 건물과 건설 완료시각
    answer[now] = end_time
    for nex in graph[now]:
        start_time[nex] = max(start_time[nex], end_time)
        indegree[nex] -= 1
        if indegree[nex] == 0:
            queue.append((nex, start_time[nex] + costs[nex]))

for i in range(1, N + 1):
    print(answer[i])