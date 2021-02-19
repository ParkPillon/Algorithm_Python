# 백준 17534 최단경로
# https://www.acmicpc.net/problem/1753

import heapq
import sys

INF = int(1e9)  # 무한대의 수를 의미
V, E = map(int, sys.stdin.readline().split())  # 노드, 간선의 수
K = int(sys.stdin.readline())
graph = [dict() for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if v in graph[u]:  # u에서 v로의 간선이 이미 있을 경우
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w
distance = [INF] * (V + 1)


def dijikstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, node = heapq.heappop(hq)
        if distance[node] < dist:  # 이미 처리된 경우
            continue
        for dest, cost in graph[node].items():
            new_cost = dist + cost
            if new_cost < distance[dest]:
                distance[dest] = new_cost
                heapq.heappush(hq, (new_cost, dest))


dijikstra(K)
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])