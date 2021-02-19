# 백준 2110 공유기 설치
# Parametric Search
# https://www.acmicpc.net/problem/2110

import sys

N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

# 가장 인접한 거리의 탐색 범위
start = 1
end = houses[-1] - houses[0]
result = 0

while start <= end:
    gap = (start + end) // 2  # 공유기가 최소 gap만큼 떨어져 있음
    temp = houses[0]
    count = 1
    isGap = False
    for i in range(1, N):
        if houses[i] - temp >= gap:
            if houses[i] - temp == gap:
                isGap = True
            count += 1
            temp = houses[i]

    if count >= C:  # 최소거리가 gap일 때 공유기 설치 가능
        start = gap + 1
        if isGap:
            result = gap
    else:
        end = gap - 1

print(result)