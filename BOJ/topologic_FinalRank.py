# 백준 3665 최종 순위
# https://www.acmicpc.net/problem/3665
# 일부의 순위로 전체 순위 유추

import sys
from collections import deque


def solution(n, last, m, changed):
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(1, n):  # 작년 순위를 위상그래프로 표현
        ith_team = last[i]  # 작년 (i+1)등 팀
        for j in range(i):
            jth_team = last[j]
            graph[jth_team].append(ith_team)  # 높은순위 팀이 낮은 순위 팀을 향하는 방향
            indegree[ith_team] += 1

    # 등수 바뀐 팀에 대해 그래프 갱신
    for first, second in changed:
        if first in graph[second]:  # second팀이 first팀보다 순위가 높은 상황
            graph[second].remove(first)
            graph[first].append(second)
            indegree[second] += 1
            indegree[first] -= 1
        else:
            graph[first].remove(second)
            graph[second].append(first)
            indegree[first] += 1
            indegree[second] -= 1

    # 갱신된 그래프에 대해 위상 정렬 수행
    queue = deque()
    result = []
    certain = True
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        if len(queue) >= 2:  # 정렬 수행결과가 여러개
            certain = False
        now = queue.popleft()
        result.append(now)
        for upper in graph[now]:  # 상위 노드에 대해
            indegree[upper] -= 1
            if indegree[upper] == 0:
                queue.append(upper)
    if len(result) < n:  # 순위를 알 수 없는 경우
        return None, certain
    else:
        return result, certain


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    last = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    changed = []
    for __ in range(m):
        changed.append(tuple(map(int, sys.stdin.readline().split())))
    result, certain = solution(n, last, m, changed)
    if result and certain:
        print(*result)
    elif result:
        print("?")
    else:
        print("IMPOSSIBLE")
