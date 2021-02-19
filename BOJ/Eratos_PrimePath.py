# 백준 1963 소수경로
# https://www.acmicpc.net/problem/1963

import sys
from collections import deque

primeList = []
isPrime = [True] * 10000
for i in range(2, 101):
    if isPrime[i]:
        j = 2
        while i * j < 10000:
            isPrime[i * j] = False
            j += 1
for i in range(1000, 10000):
    if isPrime[i]:
        primeList.append(i)


def possibleNext(num, array):  # array 중 num이 바꿀수있는 수
    result = []
    idx = 1000  # 바꿀 자릿수
    while idx >= 1:
        now = (num % (idx * 10)) // idx
        for new in range(10):
            if now != new:
                newNum = num - now * idx + new * idx
                if newNum in array:
                    result.append(newNum)
        idx //= 10
    return result


def solution(start, end):
    if start == end:
        return 0
    queue = deque([(start, 0)])
    visited = [start]
    while queue:
        now, count = queue.popleft()
        if now == end:
            return count
        for next in possibleNext(now, primeList):
            if next in visited:  # 이미 방문했으면 패스
                continue
            queue.append((next, count + 1))
            visited.append(next)


T = int(sys.stdin.readline())
for _ in range(T):
    start, end = map(int, sys.stdin.readline().split())
    print(solution(start, end))
