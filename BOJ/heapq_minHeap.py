# 백준 1927 최소 힙
# https://www.acmicpc.net/problem/1927

import sys
import heapq

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
hq = []
for x in nums:
    if x:
        heapq.heappush(hq, x)
    else:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)