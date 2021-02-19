# 백준 1655 가운데를 말해요
# https://www.acmicpc.net/problem/1655

import sys
import heapq

N = int(sys.stdin.readline())
small, large = [], []
s, l = 0, 0
median = int(sys.stdin.readline())
print(median)
for _ in range(N - 1):
    new = int(sys.stdin.readline())
    if new > median:
        heapq.heappush(large, new)
        l += 1
        if s + 2 == l:
            heapq.heappush(small, -median)
            median = heapq.heappop(large)
            s += 1
            l -= 1
    else:
        heapq.heappush(small, -new)
        s += 1
        if s > l:
            heapq.heappush(large, median)
            median = -heapq.heappop(small)
            s -= 1
            l += 1
    print(median)
