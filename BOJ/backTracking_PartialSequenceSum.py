# 백준 1182 부분수열의 합
# https://www.acmicpc.net/problem/1182

import sys

input = sys.stdin.readline
N, S = map(int, input().split())
array = list(map(int, input().split()))

answer = 0

for memo in range(1, 2 ** N):  # 각 원소 선택여부를 비트마스킹으로 기록
    total = 0
    idx = 0
    while memo > 0:
        if memo % 2 != 0:
            total += array[idx]
        memo = memo // 2
        idx += 1
    if total == S:
        answer += 1
print(answer)