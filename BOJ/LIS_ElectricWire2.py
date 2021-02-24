# 백준 2568 전깃줄2
# https://www.acmicpc.net/problem/2568

import sys
from bisect import bisect_left
import heapq

N = int(sys.stdin.readline())
wires = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(wires, (a, b))


INF = int(1e9)
tail_nums = [-INF]  # 길이가 i인 증가수열의 마지막 값들 중 최소값
memo = []
max_length = 0
while wires:
    a, linked = heapq.heappop(wires)
    if linked > tail_nums[max_length]:
        tail_nums.append(linked)
        max_length += 1
        memo.append((max_length, a, linked))  # 수열 내에서 max_length위치에 linked가 들어감
    else:
        idx = bisect_left(tail_nums, linked)
        tail_nums[idx] = linked
        memo.append((idx, a, linked))

idx = max_length
answer = []
for i, start, end in reversed(memo):
    if i == idx:
        idx -= 1
    else:  # 없애야 하는 전깃줄
        answer.append(start)  # A위치를 출력
print(N - max_length)
print(*sorted(answer), sep="\n")
