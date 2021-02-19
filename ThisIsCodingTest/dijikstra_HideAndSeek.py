# 이코테 390 숨바꼭질
# USACO 기출

import sys
import heapq

INF = int(1e9)
N, M = map(int, sys.stdin.readline().split())
costs = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    costs[a].append((b, 1))
    costs[b].append((a, 1))
distance = [INF] * (N + 1)


def dijikstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, node = heapq.heappop(hq)
        if distance[node] < dist:
            continue
        for dest, cost in costs[node]:
            new_cost = dist + cost
            if new_cost < distance[dest]:
                distance[dest] = new_cost
                heapq.heappush(hq, (new_cost, dest))


dijikstra(1)
answer = max(distance[1:])
print(distance.index(answer), answer, distance.count(answer))