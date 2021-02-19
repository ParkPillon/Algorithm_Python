# 백준 11286 절댓값 힙
# https://www.acmicpc.net/problem/11286

import sys
import heapq

N = int(sys.stdin.readline())
hq = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x < 0:
        heapq.heappush(hq, (-x - 0.1, x))  # 같은 절댓값인 수에 대해 우선순위를 두기 위해 -0.1
    elif x > 0:
        heapq.heappush(hq, (x, x))
    else:
        if hq:
            weight, realVal = heapq.heappop(hq)
            print(realVal)
        else:
            print(0)