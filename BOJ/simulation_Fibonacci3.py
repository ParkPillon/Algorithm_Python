# 백준 2749 피보나치 수 3
# https://www.acmicpc.net/problem/2749
# 피사노 주기 활용

import sys

n = int(sys.stdin.readline())
n = n % 1500000
dp = [0] * 1500000
dp[1] = 1
dp[2] = 1
if n <= 2:
    print(dp[n])
else:
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000
    print(dp[n])
