# 백준 1717 집합의 표현
# https://www.acmicpc.net/problem/1717
# Union-Find

import sys


def getParent(x):
    if parents[x] < 0:
        return x
    parents[x] = getParent(parents[x])
    return parents[x]


def union(x, y):
    xPar = getParent(x)
    yPar = getParent(y)
    if xPar == yPar:
        return
    if parents[xPar] < parents[yPar]:
        parents[xPar] += parents[yPar]
        parents[yPar] = xPar
    else:
        parents[yPar] += parents[xPar]
        parents[xPar] = yPar


def isUnion(x, y):
    return getParent(x) == getParent(y)


n, m = map(int, sys.stdin.readline().split())
parents = [-1] * (n + 1)
for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().split())
    if op:  # 확인
        print("YES" if isUnion(a, b) else "NO")
    else:
        union(a, b)
