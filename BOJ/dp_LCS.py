# 백준 9251 LCS Longest Common Subsequence
# https://www.acmicpc.net/problem/9251

import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
F, S = len(first), len(second)
dp = [[0] * (S + 1) for _ in range(F + 1)]
for i in range(1, F + 1):
    for j in range(1, S + 1):
        if first[i - 1] == second[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[F][S])
