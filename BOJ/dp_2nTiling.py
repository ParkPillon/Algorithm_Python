# 백준 11726 2xN 타일링
# https://www.acmicpc.net/problem/11726

import sys

n = int(sys.stdin.readline())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    print(dp[n])