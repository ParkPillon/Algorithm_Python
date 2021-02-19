# 이코테 223p 바닥 공사
import sys

N = int(sys.stdin.readline())
dp = [0] * (N + 1)
dp[1], dp[2] = 1, 3
for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796

print(dp[N])