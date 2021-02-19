# 백준 6603 로또
# https://www.acmicpc.net/problem/6603

import sys


def dfs(count, array):
    if count == 6:
        print(*array)
        return
    for i in range(k):
        if array and nums[i] <= array[-1]:
            continue
        dfs(count + 1, array + [nums[i]])


while True:
    k, *nums = map(int, sys.stdin.readline().split())
    if k == 0:
        break
    dfs(0, [])
    print()
