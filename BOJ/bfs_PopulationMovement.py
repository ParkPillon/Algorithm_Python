# 백준 16234 인구이동
# https://www.acmicpc.net/problem/16234

import sys
from collections import deque


N, L, R = map(int, sys.stdin.readline().split())
worldMap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def move(union):
    new_pop = sum([worldMap[x][y] for x, y in union]) // len(union)
    for x, y in union:
        worldMap[x][y] = new_pop


def buildUnion(worldMap, N, L, R):
    unionList = []
    visited = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 1:
                continue
            queue = deque([(x, y)])
            union = []  # 연합된 국가를 담을 리스트
            while queue:
                temp_x, temp_y = queue.popleft()
                visited[temp_x][temp_y] = 1
                union.append((temp_x, temp_y))
                for i in range(4):
                    nx = temp_x + dx[i]
                    ny = temp_y + dy[i]
                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    if visited[nx][ny] == 1:
                        continue
                    if (nx, ny) in queue:
                        continue
                    diff = abs(worldMap[temp_x][temp_y] - worldMap[nx][ny])
                    if diff >= L and diff <= R:  # 범위 내에 존재
                        queue.append((nx, ny))
            if len(union) > 1:  # 연합이 존재할 경우
                unionList.append(union)

    return unionList


def solution():
    count = 0
    while True:
        unionList = buildUnion(worldMap, N, L, R)
        if not unionList:  # 연합이 없을 경우
            break
        count += 1
        for union in unionList:
            move(union)
    print(count)


solution()