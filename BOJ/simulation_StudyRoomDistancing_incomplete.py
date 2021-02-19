# 백준 20665 독서실 거리두기
# https://www.acmicpc.net/problem/20665

import sys

N, T, P = map(int, sys.stdin.readline().split())
hours = []
for _ in range(T):
    start, end = map(int, sys.stdin.readline())
    start = (start // 100) * 60 + start % 100
    end = (end // 100) * 60 + end % 100
used = [0] * N  # 좌석 사용중 여부


def chooseSeat(used):
    pass