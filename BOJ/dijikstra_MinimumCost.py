# 백준 1916 최소비용 구하기
# https://www.acmicpc.net/problem/1916

import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
start, end = map(int, sys.stdin.readline().split())


INF = int(1e9)
distance = [INF] * (N + 1)


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
print(distance[end])