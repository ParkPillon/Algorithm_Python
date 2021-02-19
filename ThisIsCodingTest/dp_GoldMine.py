# 이코테 375p 금광
# Flipkart 인터뷰

import sys


def getMaxGold(n, m, mine):
    dp = [[0] * (m) for _ in range(n)]
    for i in range(n):
        dp[i][0] = mine[i][0]
    for j in range(1, m):
        for i in range(n):
            dp[i][j] = dp[i][j - 1] + mine[i][j]
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + mine[i][j])
            if i < n - 1:
                dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + mine[i][j])
    return max([dp[i][-1] for i in range(n)])


T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    temp = list(map(int, sys.stdin.readline().split()))
    print(temp)
    mine = [temp[i : i + m] for i in range(0, len(temp), m)]
    print(mine)
    print(getMaxGold(n, m, mine))
