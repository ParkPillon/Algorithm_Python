# 백준 14499 주사위 굴리기
# https://www.acmicpc.net/problem/14499

import sys


def roll(state, direction):  # state: 위,북,동,서,남,아래 순서
    if direction == 1:
        return [state[3], state[1], state[0], state[5], state[4], state[2]]
    elif direction == 2:
        return [state[2], state[1], state[5], state[0], state[4], state[3]]
    elif direction == 3:
        return [state[4], state[0], state[2], state[3], state[5], state[1]]
    elif direction == 4:
        return [state[1], state[5], state[2], state[3], state[0], state[4]]


N, M, x, y, K = map(int, sys.stdin.readline().split())
mmap = []
for _ in range(N):
    mmap.append(list(map(int, sys.stdin.readline().split())))
commands = list(map(int, sys.stdin.readline().split()))
dx = [0, 0, 0, -1, 1]  # None, 동, 서, 북, 남
dy = [0, 1, -1, 0, 0]
diceVal = [0] * 7  # 0번칸부터 6번칸까지 주사위에 써있는 수 0번 무시
state = [1, 2, 3, 4, 5, 6]  # 최초 주사위 상태
for com in commands:
    nx, ny = x + dx[com], y + dy[com]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    state = roll(state, com)
    upper, bottom = state[0], state[5]
    if mmap[nx][ny] == 0:
        mmap[nx][ny] = diceVal[bottom]
    else:
        diceVal[bottom] = mmap[nx][ny]
        mmap[nx][ny] = 0
    print(diceVal[upper])
    x, y = nx, ny
