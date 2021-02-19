# 이코테 397 어두운 길

import sys


def find_parent(parents, i):  # 어떤 집합에 속하는가. 최상단노드가 누구인가
    if parents[i] != i:  # 찾기함수를 호출하면서 부모테이블 갱신
        parents[i] = find_parent(parents, parents[i])
    return parents[i]


def union(parents, a, b):  # 각 노드가 포함된 두 집합을 합침
    a_par = find_parent(parents, a)
    b_par = find_parent(parents, b)
    if a_par < b_par:
        parents[b_par] = a_par
    else:
        parents[a_par] = b_par


def isCycle(parents, a, b):
    a_par = find_parent(parents, a)
    b_par = find_parent(parents, b)
    return a_par == b_par


N, M = map(int, sys.stdin.readline().split())
roads = []
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    roads.append((z, x, y))
roads.sort()
print(roads)
parents = list(range(N))
answer = 0
for z, x, y in roads:
    if isCycle(parents, x, y):
        answer += z
        continue
    else:
        union(parents, x, y)
print(answer)