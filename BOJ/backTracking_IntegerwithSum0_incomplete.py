# 백준 7453 합이 0인 네 정수
# https://www.acmicpc.net/problem/7453

import sys

n = int(sys.stdin.readline())
ABCD = [[0] * n for _ in range(4)]
for i in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    for idx in range(4):
        ABCD[idx][i] = nums[idx]


answer = 0


def dfs(count, total):
    global answer
    if count == 4:
        if total == 0:
            answer += 1
        return
    for i in range(n):
        dfs(count + 1, total + ABCD[count][i])


dfs(0, 0)
print(answer)
