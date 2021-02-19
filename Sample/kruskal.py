# Kruskal Algorithm
# 시간 복잡도 O(ElogE) 간선 E개
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
        if isCycle(parents, a, b):
            continue
        union(parents, a, b)
        link += 1
        answer += cost
    return answer


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
