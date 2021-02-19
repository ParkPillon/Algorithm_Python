# 다익스트라 최단거리 간단한 구현방법
# Greedy Algorithm에 속함
# O(N2) 시간복잡도
# 노드의 개수 5000개 이하라면 적용 가능
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
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# 방문하지 않은 노드 중, 가장 최단거리가 짧은 노드의 번호
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijikstra(start):
    distance[start] = 0
    visited[start] = True
    for dest, cost in graph[start]:
        distance[dest] = cost

    while False in visited:
        cur = get_smallest_node()
        visited[cur] = True
        for dest, cost in graph[cur]:
            if visited[dest]:
                continue  # 이미 처리한 노드
            new_cost = distance[cur] + cost
            if new_cost < distance[dest]:
                distance[dest] = new_cost


dijikstra(1)

print(distance)
