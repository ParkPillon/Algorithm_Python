# 백준 2887 행성 터널
# https://www.acmicpc.net/problem/2887

import sys


def solution(n, costs):
    answer = 0
    parents = list(range(n))
    costs.sort(key=lambda cost: cost[2])
    link = 0
    for a, b, cost in costs:
        if link == n - 1:
            break
        if isUnion(parents, a, b):
            continue
        union(parents, a, b)
        link += 1
        answer += cost
    return answer


def getParent(parents, i):
    if parents[i] == i:
        return i
    else:
        return getParent(parents, parents[i])


def union(parents, a, b):  # 각 노드가 포함된 두 집합을 합침
    a_par = getParent(parents, a)
    b_par = getParent(parents, b)
    if a_par < b_par:
        parents[b_par] = a_par
    else:
        parents[a_par] = b_par


def isUnion(parents, a, b):  # 같은 트리 내에 속하는가
    a_par = getParent(parents, a)
    b_par = getParent(parents, b)
    return a_par == b_par


N = int(sys.stdin.readline())

planets = []
costs = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    planets.append((i, x, y, z))
for idx in [1, 2, 3]:
    planets.sort(key=lambda pl: pl[idx])  # x,y,z축으로 정렬
    for k in range(N - 1):  # 정렬된 행성에 대해 인접한 간선을 추가
        i, x, y, z = planets[k]
        j, x2, y2, z2 = planets[k + 1]
        dist = min(abs(x - x2), abs(y - y2), abs(z - z2))
        costs.append((i, j, dist))
print(solution(N, costs))