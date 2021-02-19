# 프로그래머스 네트워크

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

from collections import deque


def solution(n, computers):
    visited = [0] * n
    network = 0
    for i in range(n):
        if visited[i]:
            continue
        queue = deque([i])
        visited[i] = 1
        network += 1
        while queue:
            com = queue.popleft()
            for k in range(n):
                if computers[com][k] == 1 and not visited[k]:
                    queue.append(k)
                    visited[k] = 1

    return network


print(solution(n, computers))
