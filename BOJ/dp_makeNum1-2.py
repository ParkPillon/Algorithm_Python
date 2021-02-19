# 백준 1로 만들기2
# https://www.acmicpc.net/problem/12852
#

import sys

N = int(sys.stdin.readline())


dp = [0] * (N + 1)
dp[1] = (0, [1])  # 연산횟수, 1로 만드는 과정
for i in range(2, N + 1):
    count = 1 + dp[i - 1][0]
    selected = i - 1
    if i % 3 == 0 and (1 + dp[i // 3][0]) <= count:
        count = 1 + dp[i // 3][0]
        selected = i // 3
    if i % 2 == 0 and (1 + dp[i // 2][0]) <= count:
        count = 1 + dp[i // 2][0]
        selected = i // 2
    dp[i] = (count, dp[selected][1] + [i])
print(dp[N][0])
for i in dp[N][1][::-1]:
    print(i, end=" ")
