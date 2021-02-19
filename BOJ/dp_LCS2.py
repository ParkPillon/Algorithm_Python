# 백준 9251 LCS2 Longest Common Subsequence
# https://www.acmicpc.net/problem/9252

import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
F, S = len(first), len(second)
dp = [[""] * (S + 1) for _ in range(F + 1)]
for i in range(1, F + 1):
    for j in range(1, S + 1):
        if first[i - 1] == second[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + first[i - 1]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
if len(dp[F][S]):
    print(len(dp[F][S]))
    print(dp[F][S])
else:
    print(0)
