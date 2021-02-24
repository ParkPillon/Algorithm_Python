# 백준 12015 가장 긴 증가하는 부분 수열 2
# https://www.acmicpc.net/problem/12015
# 수열의 길이만 구할때 사용
# 실제 수열과는 다를 수 있음

import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

incList = [array[0]]
for i in range(1, N):
    if array[i] > incList[-1]:
        incList.append(array[i])
    else:
        idx = bisect_left(incList, array[i])
        incList[idx] = array[i]
print(len(incList))