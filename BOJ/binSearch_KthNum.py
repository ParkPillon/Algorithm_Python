# 백준 1300 K번째 수
# 중요 문항
# https://www.acmicpc.net/problem/1300

import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start, end = 1, k
answer = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, N + 1):
        count += min(mid // i, N)
    if count >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
