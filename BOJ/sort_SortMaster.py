# 백준 20551 sort 마스터 배지훈의 후계자
# https://www.acmicpc.net/problem/20551

import sys
from bisect import bisect_left, bisect_right

N, M = map(int, sys.stdin.readline().split())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline()))
array.sort()

for _ in range(M):
    d = int(sys.stdin.readline())
    r_idx = bisect_right(array, d)
    l_idx = bisect_left(array, d)
    if r_idx - l_idx == 0:
        print(-1)
    else:
        print(l_idx)