# 백준 14500 테트로미노
# https://www.acmicpc.net/problem/14500

import sys


def getTet(r, c):
    result = []
    # 일자모양
    result.append([(r, c), (r + 1, c), (r + 2, c), (r + 3, c)])
    result.append([(r, c), (r, c + 1), (r, c + 2), (r, c + 3)])
    # 정사각형
    result.append([(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)])
    # 기역자
    result.append([(r, c), (r + 1, c), (r + 2, c), (r + 2, c + 1)])
    result.append([(r, c), (r + 1, c), (r + 2, c), (r + 2, c - 1)])
    result.append([(r, c), (r - 1, c), (r - 2, c), (r - 2, c + 1)])
    result.append([(r, c), (r - 1, c), (r - 2, c), (r - 2, c - 1)])

    result.append([(r, c), (r, c + 1), (r, c + 2), (r + 1, c + 2)])
    result.append([(r, c), (r, c + 1), (r, c + 2), (r - 1, c + 2)])
    result.append([(r, c), (r, c - 1), (r, c - 2), (r + 1, c - 2)])
    result.append([(r, c), (r, c - 1), (r, c - 2), (r - 1, c - 2)])
    # 와리가리
    result.append([(r, c), (r + 1, c), (r + 1, c + 1), (r + 2, c + 1)])
    result.append([(r, c), (r + 1, c), (r + 1, c - 1), (r + 2, c - 1)])
    result.append([(r, c), (r, c + 1), (r - 1, c + 1), (r - 1, c + 2)])
    result.append([(r, c), (r, c + 1), (r + 1, c + 1), (r + 1, c + 2)])
    # 오목할 철
    result.append([(r, c), (r, c + 1), (r, c + 2), (r - 1, c + 1)])
    result.append([(r, c), (r, c + 1), (r, c + 2), (r + 1, c + 1)])
    result.append([(r, c), (r + 1, c), (r + 2, c), (r + 1, c + 1)])
    result.append([(r, c), (r + 1, c), (r + 2, c), (r + 1, c - 1)])

    return result


N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for r in range(N):
    for c in range(M):
        for tet in getTet(r, c):  # 테트리스 모형
            temp = 0
            for pos_x, pos_y in tet:  # 각각의 위치
                if pos_x < 0 or pos_x >= N or pos_y < 0 or pos_y >= M:
                    break
                temp += board[pos_x][pos_y]
            answer = max(answer, temp)
print(answer)