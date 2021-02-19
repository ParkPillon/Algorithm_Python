# 이코테 226p 효율적인 화폐구성
import sys

N, M = map(int, sys.stdin.readline().split())
money = [int(sys.stdin.readline()) for _ in range(N)]

dp = [0] * (M + 1)
for i in range(1, M + 1):

    if i in money:
        dp[i] = 1
        continue
    answer = M + 1
    for m in money:
        if i - m > 0:
            if dp[i - m] == -1:
                continue
            answer = min(1 + dp[i - m], answer)
    dp[i] = answer if answer != (M + 1) else -1
print(dp)
