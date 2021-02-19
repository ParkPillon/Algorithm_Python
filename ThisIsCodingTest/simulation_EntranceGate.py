# 이코테 395 탑승구

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


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
roots = list(range(G + 1))
planes = []
for _ in range(P):
    planes.append(int(sys.stdin.readline()))
answer = 0

for p in planes:
    selected_gate = find_parent(roots, p)
    if selected_gate == 0:  # 도킹 불가
        break
    else:
        answer += 1
        union(roots, selected_gate, selected_gate - 1)
print(answer)