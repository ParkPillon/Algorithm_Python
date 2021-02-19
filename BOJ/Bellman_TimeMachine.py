# 백준 11657 타임 머신
# https://www.acmicpc.net/problem/11657
# 벨만 포드 알고리즘
# 다익스트라 알고리즘 응용
# 간선이 양수가 아닌경우 and 음수 간선의 순환이 이루어질 경우

import sys

n, m = map(int, sys.stdin.readline().split())
INF = int(1e9)
edges = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))
distance = [INF] * (n + 1)


def bellman(start):
    distance[start] = 0
    for times in range(n):  # n-1번의 라운드, n번째는 음수간선 확인용
        for dep, dest, cost in edges:  # 각 라운드마다 모든 간선 확인
            if distance[dep] != INF and distance[dep] + cost < distance[dest]:
                distance[dest] = distance[dep] + cost
                if times == n - 1:  # 음수 간선이 발생할 경우
                    return False
    return True


if bellman(1):
    for i in range(2, n + 1):
        print(distance[i] if distance[i] < INF else -1)
else:
    print(-1)