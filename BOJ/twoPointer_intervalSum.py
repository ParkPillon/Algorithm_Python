# 백준 1806 부분합
# https://www.acmicpc.net/problem/1806

import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

end = 0
min_length = 1e9
temp_sum = 0
for start in range(N):
    while temp_sum < M and end < N:
        temp_sum += data[end]
        end += 1
    if temp_sum >= M:
        min_length = min(min_length, end - start)
    temp_sum -= data[start]

print(min_length if min_length < 1e9 else 0)
