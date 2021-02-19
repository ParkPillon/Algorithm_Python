# 백준 14003 가장 긴 증가하는 부분수열5
# https://www.acmicpc.net/problem/14003
# 이진 탐색


import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
INF = int(1e10)
tail_nums = [INF] * (N + 1)  # 길이가 i인 배열의 마지막 값 중 최소값
tail_nums[0] = -INF
max_length = 0
sample = []  # 탐색 과정을 기록
for num in array:
    if num > tail_nums[max_length]:
        tail_nums[max_length + 1] = num
        max_length += 1
        sample.append((max_length, num))
    else:
        idx = bisect_left(tail_nums, num)
        tail_nums[idx] = num
        sample.append((idx, num))

print(max_length)
idx = max_length
answer = []
for n, num in reversed(sample):
    if n == idx:
        answer.append(num)
        idx -= 1
print(*reversed(answer))