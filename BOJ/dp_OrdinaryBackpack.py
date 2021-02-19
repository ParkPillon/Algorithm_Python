# 백준 12865 평범한 배낭
# https://www.acmicpc.net/problem/12865

import sys

N, K = map(int, sys.stdin.readline().split())
weight = [0] * N
value = [0] * N
for i in range(N):
    w, c = map(int, sys.stdin.readline().split())
    weight[i] = w
    value[i] = c

dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for w in range(1, K + 1):
        if weight[i - 1] <= w:  # 가방을 넣을 수 있는 경우
            dp[i][w] = max(value[i - 1] + dp[i - 1][w - weight[i - 1]], dp[i - 1][w])
        else:  # 가방을 넣을 수 없는 경우
            dp[i][w] = dp[i - 1][w]

print(dp[N][K])
