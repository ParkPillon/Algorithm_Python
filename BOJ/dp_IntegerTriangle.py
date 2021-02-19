# 백준 1932 정수 삼각형
# https://www.acmicpc.net/problem/1932

import sys

n = int(sys.stdin.readline())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))
# dp_tri = [[0] * (i + 1) for i in range(n)]
for i in range(1, n):
    for j in range(len(triangle[i])):
        value = triangle[i][j]
        if j > 0:
            triangle[i][j] = max(triangle[i][j], triangle[i - 1][j - 1] + value)
        if j < len(triangle[i]) - 1:
            triangle[i][j] = max(triangle[i][j], triangle[i - 1][j] + value)
print(max(triangle[-1]))
