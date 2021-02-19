# 백준 1005 ACM Craft
# https://www.acmicpc.net/problem/1005

import sys
from collections import deque


def solution(N, D, graph, indegree, W):
    start_time = [0] * (N + 1)  # N번째 건물이 건설 시작될수 있는 최소 시간
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append((i, D[i]))

    while queue:
        now, end_time = queue.popleft()
        if now == W:
            return end_time
        for next in graph[now]:
            indegree[next] -= 1
            start_time[next] = max(start_time[next], end_time)
            if indegree[next] == 0:
                queue.append((next, start_time[next] + D[next]))


T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = [0] + list(map(int, sys.stdin.readline().split()))
    indegree = [0] * (N + 1)
    graph = [[] for __ in range(N + 1)]
    for ___ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    W = int(sys.stdin.readline())
    print(solution(N, D, graph, indegree, W))
