# 백준 1966 프린터 큐
# https://www.acmicpc.net/problem/1966

import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    weight = list(map(int, sys.stdin.readline().split()))
    queue = deque()
    for idx, w in enumerate(weight):
        queue.append((idx, w))
    weight.sort(reverse=True)
    count = 1  # 몇번째 출력
    w_idx = 0  # 현재 시점에 남아있는 문서 중 최고 중요도 문서의 위치
    while queue:
        idx, w = queue.popleft()
        if w < weight[w_idx]:  # 현재 큐의 문서보다 중요한 문서가 존재할 경우
            queue.append((idx, w))
        else:  # 현재 큐의 문서 출력
            if idx == M:
                print(count)
            w_idx += 1
            count += 1
