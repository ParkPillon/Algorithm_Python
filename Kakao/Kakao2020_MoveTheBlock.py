# 카카오2020 블록 이동하기 완전탐색
# https://programmers.co.kr/learn/courses/30/lessons/60063


board = [
    [0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 0],
]

from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def solution(board):
    answer = 0
    n = len(board)
    # 테두리를 1로 채움
    newBoard = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            newBoard[i + 1][j + 1] = board[i][j]
    queue = deque([({(1, 1), (1, 2)}, 0)])
    visited = []
    while queue:
        pos, count = queue.popleft()
        if (n, n) in pos:
            answer = count
            break
        for next_pos in getNextPos(pos, newBoard):
            if next_pos in visited:
                continue
            visited.append(next_pos)
            queue.append((next_pos, count + 1))

    return answer


def getNextPos(pos, board):
    nextPos = []
    pos1, pos2 = list(pos)
    # 이동
    for i in range(4):
        npos1x, npos1y = pos1[0] + dx[i], pos1[1] + dy[i]
        npos2x, npos2y = pos2[0] + dx[i], pos2[1] + dy[i]
        if board[npos1x][npos1y] == 0 and board[npos2x][npos2y] == 0:
            nextPos.append({(npos1x, npos1y), (npos2x, npos2y)})

    # 회전
    if pos1[0] == pos2[0]:  # 가로
        for i in [1, -1]:  # 위 아래로 회전
            if board[pos1[0] + i][pos1[1]] == 0 and board[pos2[0] + i][pos2[1]] == 0:
                # 위 또는 아래 두칸 모두 비어있을 경우
                nextPos.append({pos1, (pos1[0] + i, pos1[1])})
                nextPos.append({pos2, (pos2[0] + i, pos2[1])})

    elif pos1[1] == pos2[1]:
        for i in [1, -1]:  # 우,좌로 회전
            if board[pos1[0]][pos1[1] + i] == 0 and board[pos2[0]][pos2[1] + i] == 0:
                # 오른쪽 왼쪽 두칸 모두 비어있을 경우
                nextPos.append({pos1, (pos1[0], pos1[1] + i)})
                nextPos.append({pos2, (pos2[0], pos2[1] + i)})
    return nextPos


# print(getNextPos({(1, 1), (1, 2)}))
print(solution(board))
