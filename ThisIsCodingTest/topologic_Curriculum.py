# 이코테 303 커리큘럼
# 위상 정렬

import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
min_time = [0] * (N + 1)
indegree = [0] * (N + 1)
for i in range(1, N + 1):
    time, *temp, end = map(int, sys.stdin.readline().split())
    min_time[i] = time
    for course in temp:
        graph[course].append(i)
        indegree[i] += 1


def topology_sort():
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append((i, min_time[i]))
    while queue:
        now, time = queue.popleft()
        min_time[now] = time
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append((next, time + min_time[next]))


topology_sort()
print(min_time)