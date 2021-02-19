# 백준 2352 반도체 설계
# https://www.acmicpc.net/problem/2352
# LIS

import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

incList = [array[0]]
for i in range(1, n):
    list_end, new = incList[-1], array[i]
    if list_end < new:
        incList.append(new)
    else:
        idx = bisect_left(incList, new)
        incList[idx] = new
print(len(incList))