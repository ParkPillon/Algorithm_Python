# 백준 10775 공항
# https://www.acmicpc.net/problem/10775

import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

G = int(input())
P = int(input())
dock = list(range(G + 1))
planes = [int(input()) for _ in range(P)]


def try_dock(g):  # i번 게이트에 도킹 시도했을 때 실제로 도킹되는 게이트. 만약 값이 0이면 비행기 도킹 불가
    if dock[g] == g:
        return g
    dock[g] = try_dock(dock[g])
    return try_dock(dock[g])


count = 0
for g in planes:
    gate = try_dock(g)
    if gate == 0:  # 도킹 실패
        break
    else:
        dock[gate] = gate - 1
        count += 1
print(count)
