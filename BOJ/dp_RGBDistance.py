# 백준 1149 RGB거리
# https://www.acmicpc.net/problem/1149

import sys

N = int(sys.stdin.readline())
distance = []
for _ in range(N):
    distance.append(list(map(int, sys.stdin.readline().split())))

for house in range(1, N):
    for color in range(3):
        result = 1e9
        for color_prev in range(3):  # 이전 집까지의 최소비용 + 이번 집의 비용
            if color_prev == color:
                continue
            result = min(result, distance[house - 1][color_prev])
        distance[house][color] += result
print(min(distance[-1]))
