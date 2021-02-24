# 백준 15644 구슬 탈출 3
# https://www.acmicpc.net/problem/15644
# '.' 빈칸 '#' 장애물/벽 'O' 구멍 'R' 빨간 구슬 'B' 파란 구슬

import sys
from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
N, M = map(int, sys.stdin.readline().split())
board = [["#"] * (M) for _ in range(N)]
visited = [
    [[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)
]
rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
    row = list(sys.stdin.readline().strip())
    for j in range(M):
        board[i][j] = row[j]
        if row[j] == "R":
            rx, ry = i, j
        elif row[j] == "B":
            bx, by = i, j
visited[rx][ry][bx][by] = True


def move(direction, x, y):
    count = 0
    while board[x + dx[direction]][y + dy[direction]] != "#" and board[x][y] != "O":
        x += dx[direction]
        y += dy[direction]
        count += 1
    return x, y, count


dirChr = ["R", "U", "L", "D"]
findAns = False
queue = deque()
queue.append((rx, ry, bx, by, 1, ""))
while queue and not findAns:
    rx, ry, bx, by, depth, memo = queue.popleft()
    if depth > 10:
        break
    for direction in range(4):
        next_rx, next_ry, rcount = move(direction, rx, ry)  # 빨간공 이동
        next_bx, next_by, bcount = move(direction, bx, by)  # 파란공 이동

        if board[next_bx][next_by] == "O":  # 파란공이 구멍에 떨어지면 실패
            continue
        if board[next_rx][next_ry] == "O":  # 빨간공이 구멍
            print(depth)
            print(memo + dirChr[direction])
            findAns = True
            break

        if next_rx == next_bx and next_ry == next_by:  # 두공이 같은위치
            if rcount > bcount:  # 더많이 움직인 공을 뒤로 이동
                next_rx -= dx[direction]
                next_ry -= dy[direction]
            else:
                next_bx -= dx[direction]
                next_by -= dy[direction]
        if not visited[next_rx][next_ry][next_bx][next_by]:
            visited[next_rx][next_ry][next_bx][next_by] = True
            queue.append(
                (
                    next_rx,
                    next_ry,
                    next_bx,
                    next_by,
                    depth + 1,
                    memo + dirChr[direction],
                )
            )
if not findAns:
    print(-1)