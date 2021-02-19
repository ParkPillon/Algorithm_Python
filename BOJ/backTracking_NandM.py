# 백준 15649 N과 M
# https://www.acmicpc.net/problem/15649

import sys

N, M = map(int, sys.stdin.readline().split())
selected = [False] * (N + 1)


def dfs(count, curArray):
    if count == M:
        print(*curArray)
        return
    for i in range(1, N + 1):
        if not selected[i]:
            selected[i] = True
            dfs(count + 1, curArray + [i])
            selected[i] = False


dfs(0, [])
