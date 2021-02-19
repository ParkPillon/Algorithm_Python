# 백준 1504 특정한 최단경로
# https://www.acmicpc.net/problem/1504

import sys
import heapq

INF = int(1e9)
N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
node1, node2 = map(int, sys.stdin.readline().split())
distance_node1 = [INF] * (N + 1)  # node1에서 출발한 최단거리
distance_node2 = [INF] * (N + 1)  # node2에서 출발한 최단거리


def dijikstra(start, distance):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for next, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(hq, (new_cost, next))


dijikstra(node1, distance_node1)
dijikstra(node2, distance_node2)

answer = (
    min(distance_node1[1] + distance_node2[N], distance_node2[1] + distance_node1[N])
    + distance_node1[node2]
)
if answer >= INF:
    print(-1)
else:
    print(answer)
