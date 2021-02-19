# 백준 1로 만들기 1
# https://www.acmicpc.net/problem/1463

import sys

N = int(sys.stdin.readline())

dp = [0] * (N + 1)
dp[1] = 0
for i in range(2, N + 1):
    answer = 1 + dp[i - 1]
    if i % 3 == 0:
        answer = min(answer, 1 + dp[i // 3])
    if i % 2 == 0:
        answer = min(answer, 1 + dp[i // 2])
    dp[i] = answer
print(dp[N])