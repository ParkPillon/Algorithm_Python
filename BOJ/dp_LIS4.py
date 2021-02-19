# 백준 14002 가장 긴 증가하는 부분수열4
# https://www.acmicpc.net/problem/14002
import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

dp = [(1, x) for x in range(N)]  # 수열의 길이, 이전 수의 위치
for i in range(1, N):
    for j in range(0, i):
        if array[j] < array[i]:
            if dp[j][0] + 1 > dp[i][0]:
                dp[i] = (dp[j][0] + 1, j)
print(dp)
max_idx = dp.index(max(dp, key=lambda a: a[0]))
print(dp[max_idx][0])
res = [array[max_idx]]
while dp[max_idx][1] != max_idx:
    max_idx = dp[max_idx][1]
    res.append(array[max_idx])
res.reverse()
print(*res)
