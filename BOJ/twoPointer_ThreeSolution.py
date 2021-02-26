# 백준 2473 세 용액
# https://www.acmicpc.net/problem/2473

import sys

N = int(sys.stdin.readline())
sols = list(map(int, sys.stdin.readline().split()))
sols.sort()

answer = int(1e10)
one, two, three = 0, 0, 0
for left in range(N - 2):
    mid = left + 1
    right = N - 1
    while mid < right:
        temp = sols[left] + sols[mid] + sols[right]
        if abs(temp) < answer:  # 현재의 용액 특성값이 더 0에 가까울 경우
            answer = abs(temp)
            one, two, three = sols[left], sols[mid], sols[right]
        if temp < 0:
            mid += 1
        elif temp > 0:
            right -= 1
        else:
            print(one, two, three)
            exit()
print(one, two, three)
