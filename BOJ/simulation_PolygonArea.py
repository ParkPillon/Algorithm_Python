# 백준 2166 다각형의 면적
# https://www.acmicpc.net/problem/2166

import sys

N = int(sys.stdin.readline())
x_coords = [0] * N
y_coords = [0] * N

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_coords[i] = x
    y_coords[i] = y


def getArea(N, x_coords, y_coords):
    total = 0
    for i in range(N):
        if i < N - 1:
            total += x_coords[i] * y_coords[i + 1] - x_coords[i + 1] * y_coords[i]
        else:
            total += x_coords[i] * y_coords[0] - x_coords[0] * y_coords[i]
    total = abs(total) / 2
    return total


print(getArea(N, x_coords, y_coords))
