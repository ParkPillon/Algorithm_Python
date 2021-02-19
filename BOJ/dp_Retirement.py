# 백준 14501 퇴사
# https://www.acmicpc.net/problem/14501

import sys

N = int(sys.stdin.readline())
T, P = [], []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    T.append(a)
    P.append(b)

dp = [0] * N
if T[-1] == 1:  # 마지막날 일정
    dp[-1] = P[-1]

for i in range(N - 2, -1, -1):
    if i + T[i] > N:  # 선택할 수 없는 경우
        dp[i] = dp[i + 1]
    elif i + T[i] == N:  # 선택하면 뒤의 일정은 선택못함
        dp[i] = max(P[i], dp[i + 1])

    else:  # 선택하고 뒤에도 선택가능
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
print(dp[0])