# 백준 2565 전깃줄
# https://www.acmicpc.net/problem/2565

import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
linkedNum = [0] * 501
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    linkedNum[a] = b

incList = [int(1e9)]
for i in range(1, 501):
    if linkedNum[i] == 0:  # 전깃줄이 연결안된 번호 (왼쪽기준)
        continue
    maxNum, new = incList[-1], linkedNum[i]  # 증가리스트의 마지막수와 새로운 수를 비교
    if new > maxNum:
        incList.append(new)
    else:
        idx = bisect_left(incList, new)
        incList[idx] = new
print(N - len(incList))
