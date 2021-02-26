# 백준 1208 부분수열의 합2
# https://www.acmicpc.net/problem/1208

import sys

input = sys.stdin.readline
N, S = map(int, input().split())
array = list(map(int, input().split()))

A = array[: N // 2]
B = array[N // 2 :]
aTable = {}
bTable = {}


def dfs(count, array, total, table):
    if count == len(array):
        table[total] = table.get(total, 0) + 1
        return
    dfs(count + 1, array, total + array[count], table)
    dfs(count + 1, array, total, table)


dfs(0, A, 0, aTable)
dfs(0, B, 0, bTable)
# 길이가 0인 부분수열은 제외
aTable[0] -= 1
bTable[0] -= 1

answer = aTable.get(S, 0) + bTable.get(S, 0)  # 각부분 자체적으로 합이 S인 부분수열
for asum in aTable:
    if S - asum in bTable:  # 두부분을 조합해서 합이 S
        answer += aTable[asum] * bTable[S - asum]
print(answer)