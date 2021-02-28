# 백준 11376 열혈강호2
# https://www.acmicpc.net/problem/11376
# dfs

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(2 * N + 1)]  # i번 직원이 할 수 있는 일. 2*i-1, 2*i번은 같은 사람
for i in range(1, N + 1):
    n, *works = map(int, input().split())
    for w in works:
        graph[2 * i - 1].append(w)
        graph[2 * i].append(w)
assigned_man = [0] * (M + 1)  # i번 일에 배정된 사람


def dfs(man):
    if visited[man]:
        return False
    visited[man] = 1
    for possible_job in graph[man]:
        if assigned_man[possible_job] == 0 or dfs(assigned_man[possible_job]):
            assigned_man[possible_job] = man
            return True
    return False


for i in range(1, 2 * N + 1):
    visited = [0] * (2 * N + 1)
    dfs(i)

answer = 0
for assigned in assigned_man:
    if assigned:  # 배정된 일
        answer += 1

print(answer)