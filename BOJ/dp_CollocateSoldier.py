# 백준 18353 병사 배치하기
# https://www.acmicpc.net/problem/18353
# LIS (가장 긴 증가하는순열) 알고리즘 사용

import sys

N = int(sys.stdin.readline())
soldiers = list(map(int, sys.stdin.readline().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))
