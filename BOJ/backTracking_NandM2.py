# 백준 15650 N과 M 2
# https://www.acmicpc.net/problem/15650

import sys

N, M = map(int, sys.stdin.readline().split())


def dfs(count, array):
    if count == M:
        print(*array)
        return
    for i in range(1, N + 1):
        if array and i <= array[-1]:
            continue
        dfs(count + 1, array + [i])


dfs(0, [])
