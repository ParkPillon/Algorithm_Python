# 백준 12581 숨바꼭질2
# https://www.acmicpc.net/problem/12851

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())


def findRoute(N, K):
    time = 0
    answer = 0
    if N >= K:
        return (N - K, 1)
    distance = [0] * 100001
    queue = deque([(N, 0)])
    min_time = 1e9
    answer = 0
    while queue:
        now, time = queue.popleft()
        if time > min_time:  # 최소시간을 넘어선 노드에 대해 탐색 중지
            break
        if now == K:
            min_time = time
            answer += 1
            continue
        if now - 1 >= 0 and (distance[now - 1] == 0 or distance[now - 1] == time + 1):
            queue.append((now - 1, time + 1))
            distance[now - 1] = time + 1
        if now + 1 <= 100000 and (
            distance[now + 1] == 0 or distance[now + 1] == time + 1
        ):
            queue.append((now + 1, time + 1))
            distance[now + 1] = time + 1
        if now * 2 <= 100000 and (
            distance[now * 2] == 0 or distance[now * 2] == time + 1
        ):
            queue.append((now * 2, time + 1))
            distance[now * 2] = time + 1
    return (min_time, answer)


time, answer = findRoute(N, K)
print(time)
print(answer)
