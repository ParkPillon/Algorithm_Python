# 백준 1007 벡터 매칭
# https://www.acmicpc.net/problem/1007

import sys
from itertools import combinations

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    points = []
    x_sum, y_sum = 0, 0
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))
        x_sum += x
        y_sum += y
    ans = 1e9
    for end_points in combinations(points[1:], N // 2):  # 벡터의 출발지점 N/2개, 끝지점 N/2개
        x_vec, y_vec = x_sum, y_sum
        for x, y in end_points:
            x_vec -= 2 * x
            y_vec -= 2 * y

        vector_length = (x_vec ** 2 + y_vec ** 2) ** 0.5
        ans = min(ans, vector_length)
    print(ans)