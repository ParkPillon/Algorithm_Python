# 이코테 262p 전보

import heapq
import sys

INF = int(1e9)
n, m, start = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))


def dijikstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, node = heapq.heappop(hq)
        if distance[node] < dist:  # 이미 처리된 경우
            continue
        for dest, cost in graph[node]:
            new_cost = dist + cost
            if new_cost < distance[dest]:
                distance[dest] = new_cost
                heapq.heappush(hq, (new_cost, dest))


dijikstra(start)
count = 0
max_distance = 0
for i in range(1, n + 1):
    if distance[i] != INF:
        count += 1
        max_distance = max(max_distance, distance[i])
print(count - 1, max_distance)
