# 백준 2805
# https://www.acmicpc.net/problem/2805

import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())
trees = Counter(map(int, sys.stdin.readline().split()))

start, end = 0, max(trees)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for length, cnt in trees.items():
        if length > mid:
            total += (length - mid) * cnt
    if total >= M:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)