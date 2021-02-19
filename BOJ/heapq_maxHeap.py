# 백준 11279 최대 힙
# https://www.acmicpc.net/problem/11279

import sys
import heapq

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
hq = []
for x in nums:
    if x:
        heapq.heappush(hq, -x)
    else:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)