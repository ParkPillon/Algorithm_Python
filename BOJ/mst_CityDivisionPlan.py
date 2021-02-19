# 백준 1647 도시 분할 계획
# https://www.acmicpc.net/problem/1647

import sys

N, M = map(int, sys.stdin.readline().split())
costs = []
for _ in range(M):
    costs.append(list(map(int, sys.stdin.readline().split())))

# MST 만든 뒤 가장 비싼 도로는 제외
def solution(n, costs):
    answer = 0
    parents = list(range(n + 1))  # 0~n노드. 0노드는 무시
    costs.sort(key=lambda cost: cost[2])
    link = 0
    for a, b, cost in costs:
        if link == n - 2:
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


print(solution(N, costs))
