# 백준 11054 가장 긴 바이토닉 부분수열
# https://www.acmicpc.net/problem/11054

import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

dp_increase = [1] * N  # i를 끝으로 하는 부분증가수열
dp_decrease = [1] * N  # i를 시작으로 하는 부분감소수열
for i in range(N):
    for j in range(0, i):
        if array[i] > array[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if array[i] > array[j]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)

answer = 0
for i in range(N):
    answer = max(answer, dp_increase[i] + dp_decrease[i] - 1)
print(answer)
