# 백준 6118 숨바꼭질
# https://www.acmicpc.net/problem/6118

import sys
import heapq

INF = int(1e9)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
distance = [INF] * (N + 1)

hq = []
heapq.heappush(hq, (0, 1))
distance[1] = 0
while hq:
    dist, now = heapq.heappop(hq)
    if distance[now] < dist:
        continue
    for next in graph[now]:
        new_cost = dist + 1
        if new_cost < distance[next]:
            heapq.heappush(hq, (new_cost, next))
            distance[next] = new_cost

max_dist = max(distance[1:])
max_idx = distance.index(max_dist)
count = distance.count(max_dist)
print(max_idx, max_dist, count)
