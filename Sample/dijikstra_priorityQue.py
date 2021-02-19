# 다익스트라 최단거리 우선순위 큐 구현
# Greedy Algorithm에 속함
# O(VlogN) 시간복잡도 V: 간선의 수 N: 노드 수
# 노드의 개수 10000개 이상
import heapq

INF = int(1e9)  # 무한대의 수를 의미
n, m = 6, 11  # 노드, 간선의 수
graph = [
    [],
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    [],
]
distance = [INF] * (n + 1)


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


dijikstra(1)
print(distance)
