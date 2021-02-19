# 백준 1920
# https://www.acmicpc.net/problem/1920

import sys
from bisect import bisect_left, bisect_right


def count_by_range(array, left, right):
    right_idx = bisect_right(array, right)  # 우측 경계
    left_idx = bisect_left(array, left)  # 좌측 경계
    return right_idx - left_idx


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
sample = list(map(int, sys.stdin.readline().split()))

A.sort()
for s in sample:
    count = count_by_range(A, s, s)
    print(1 if count else 0)