# 위상 정렬
# 선수과목 문제
# 사이클 없는 방향 그래프에서 노드를 순서대로 나열
# DAG(순환하지 않는 방향 그래프)에 대해서만 수행 가능
# 시간 복잡도 O(V+E)
from collections import deque
import sys

v, e = map(int, sys.stdin.readline().split())
indegree = [0] * (v + 1)  # 진입 차수
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for j in graph[now]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
    return result


print(*topology_sort())
