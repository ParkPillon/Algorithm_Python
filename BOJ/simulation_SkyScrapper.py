# 백준 1027 고층 건물
# https://www.acmicpc.net/problem/1027
# 기울기 이용

import sys

N = int(sys.stdin.readline())
buildings = list(map(int, sys.stdin.readline().split()))

views = [0] * N
for now in range(N):
    left, right = now - 1, now + 1  # 왼쪽, 오른쪽으로 탐색할 빌딩 인덱스
    left_lastGrad = 1e9  # 현재 빌딩 기준 왼쪽 빌딩들과의 기울기 중 가장 완만한 기울기
    right_lastGrad = -1e9
    while left >= 0:
        newGrad = (buildings[now] - buildings[left]) / (now - left)
        if newGrad >= left_lastGrad:  # 이전에 탐색한 기울기값보다 작아야만 관찰가능
            left -= 1
            continue
        left_lastGrad = newGrad
        views[now] += 1
        left -= 1

    while right < N:
        newGrad = (buildings[now] - buildings[right]) / (now - right)
        if newGrad <= right_lastGrad:
            right += 1
            continue
        right_lastGrad = newGrad
        views[now] += 1
        right += 1

print(max(views))