# 백준 11053 가장 긴 증가하는 부분수열
# https://www.acmicpc.net/submit/11053
import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))