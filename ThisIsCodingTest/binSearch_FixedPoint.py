# 이코테 이진탐색 고정점찾기
# 아마존 인터뷰

import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

start, end = 0, N - 1
answer = -1
while start <= end:
    mid = (start + end) // 2
    if array[mid] == mid:
        answer = mid
        break
    elif array[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1
print(answer)