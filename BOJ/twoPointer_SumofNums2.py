# 백준 2003 수들의 합2
# https://www.acmicpc.net/problem/2003

import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))


def intervalSum(N, M, data):
    end = 0
    count = 0
    temp_sum = 0
    for start in range(N):
        # end를 가능한 만큼 이동시키기
        while temp_sum < M and end < N:
            temp_sum += data[end]
            end += 1
        if temp_sum == M:
            count += 1
        temp_sum -= data[start]
    return count


print(intervalSum(N, M, data))
