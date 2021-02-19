# 백준 20542 받아쓰기
# https://www.acmicpc.net/problem/20542

import sys

n, m = map(int, sys.stdin.readline().split())
submit = list(sys.stdin.readline().strip())
answer = list(sys.stdin.readline().strip())
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = i
for j in range(m + 1):
    dp[0][j] = j
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if submit[i - 1] == answer[j - 1]:  # 수정 필요없음
            dp[i][j] = dp[i - 1][j - 1]
        else:  # 수정 필요
            if submit[i - 1] == "i" and answer[j - 1] in ["j", "l"]:  # 예외
                dp[i][j] = dp[i - 1][j - 1]
            elif submit[i - 1] == "v" and answer[j - 1] == "w":  # 예외
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

print(dp[n][m])