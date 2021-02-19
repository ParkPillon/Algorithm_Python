# 이코테 298 팀 결성

import sys

N, M = map(int, sys.stdin.readline().split())


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


parents = list(range(N + 1))
for _ in range(M):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 0:
        union(parents, a, b)
    else:
        if isCycle(parents, a, b):
            print("YES")
        else:
            print("NO")
