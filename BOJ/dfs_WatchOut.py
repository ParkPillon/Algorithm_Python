# 백준 18428 감시 피하기
# https://www.acmicpc.net/problem/18428

import sys

# N = 5
# hall = [
#     ["X", "S", "X", "X", "T"],
#     ["T", "X", "S", "X", "X"],
#     ["X", "X", "X", "X", "X"],
#     ["X", "T", "X", "X", "X"],
#     ["X", "X", "T", "X", "X"],
# ]
N = int(sys.stdin.readline())
hall = [list(sys.stdin.readline().split()) for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def isHallSafe(hall):
    for i in range(len(hall)):
        for j in range(len(hall[0])):
            if hall[i][j] == "S":  # 학생 안전검사
                if not isStudentSafe(hall, i, j):
                    return False
    return True


def isStudentSafe(hall, x, y):
    for i in range(4):  # 동,북,서,남 방향으로 체크
        nx = x + dx[i]
        ny = y + dy[i]
        isObstacle = False
        isTeacher = False
        while not (nx < 0 or ny < 0 or nx >= N or ny >= N):
            if hall[nx][ny] == "O":  # 장애물 있으면 True
                isObstacle = True
            elif hall[nx][ny] == "T":  # 선생님 있으면 True
                isTeacher = True
            if not isObstacle and isTeacher:  # 장애물은 없고 선생님이 있을때
                return False
            nx = nx + dx[i]
            ny = ny + dy[i]
    return True


def solution(count):
    global safe
    if count == 3:
        if isHallSafe(hall):
            safe = True
            return
        return
    else:
        for i in range(N):
            for j in range(N):
                if hall[i][j] == "X":
                    hall[i][j] = "O"
                    count += 1
                    solution(count)
                    hall[i][j] = "X"
                    count -= 1


safe = False
solution(0)
print("YES" if safe else "NO")
