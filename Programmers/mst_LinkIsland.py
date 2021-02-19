# 프로그래머스 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861
# MST(최소 신장 트리), Kruskal 알고리즘 사용

n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]


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


def isUnion(parents, a, b):
    a_par = getParent(parents, a)
    b_par = getParent(parents, b)
    return a_par == b_par


print(solution(n, costs))
