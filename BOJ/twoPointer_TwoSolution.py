# 백준 2467 두 용액
# https://www.acmicpc.net/problem/2467

import sys

N = int(sys.stdin.readline())
sols = list(map(int, sys.stdin.readline().split()))
sols.sort()
answer = int(1e10)
first, second = 0, 0
left, right = 0, N - 1
while left < right:
    temp = sols[left] + sols[right]
    if abs(temp) < answer:
        answer = abs(temp)
        first = sols[left]
        second = sols[right]
        if temp == 0:
            break
    if temp < 0:
        left += 1
    else:
        right -= 1
print(first, second)
