# 백준 1167 트리의 지름
# https://www.acmicpc.net/problem/1167

import sys

V = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
for _ in range(V):
    a, *links, _ = map(int, sys.stdin.readline().split())
    i = 0
    while i < len(links):
        graph[a].append((links[i], links[i + 1]))
        i += 2


def dfs(node, distance):  # 임의의 노드에서 가장 먼 노드를 찾는다
    global max_node, max_dist
    visited[node] = 1
    hasNext = False
    for new, cost in graph[node]:
        if visited[new]:
            continue
        hasNext = True
        dfs(new, distance + cost)

    visited[node] = 0
    if not hasNext:  # 더 이상 탐색할 수 없을때
        if distance > max_dist:
            max_node = node
            max_dist = distance
        return


visited = [0] * (V + 1)
max_node, max_dist = 0, 0
dfs(1, 0)
end_node = max_node  # 트리의 지름을 구성하는 한쪽 끝노드
max_node, max_dist = 0, 0
dfs(end_node, 0)
print(max_dist)