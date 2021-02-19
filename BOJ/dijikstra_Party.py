# 백준 1238 파티
# https://www.acmicpc.net/problem/1238

import sys
import heapq

INF = int(1e9)
N, M, X = map(int, sys.stdin.readline().split())
costs = [[] for _ in range(N + 1)]
costs_reversed = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    costs[a].append((b, cost))
    costs_reversed[b].append((a, cost))

distance = [INF] * (N + 1)  # X에서 집으로 가는 최단경로
distance_reversed = [INF] * (N + 1)  # 집에서 X로 가는 최단경로


def dijikstra(start, costs, distance):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, now = heapq.heappop(hq)  # now 까지의 최소거리 dist
        if distance[now] < dist:
            continue
        for next, cost in costs[now]:
            new_cost = dist + cost
            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(hq, (new_cost, next))


dijikstra(X, costs, distance)
dijikstra(X, costs_reversed, distance_reversed)

answer = 0
for i in range(1, N + 1):
    answer = max(answer, distance[i] + distance_reversed[i])
print(answer)