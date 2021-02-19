# 이코테 220p 개미전사
import sys

N = int(sys.stdin.readline())
foodHouses = list(map(int, sys.stdin.readline().split()))
dp = [0] * (N)
dp[0], dp[1] = foodHouses[0], max(foodHouses[0], foodHouses[1])
for i in range(2, N):
    dp[i] = max(foodHouses[i] + dp[i - 2], dp[i - 1])

print(dp[N - 1])
