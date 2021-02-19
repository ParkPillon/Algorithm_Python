# 백준 11403 경로 찾기
# https://www.acmicpc.net/problem/11403

import sys

INF = int(1e9)
N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline())))
