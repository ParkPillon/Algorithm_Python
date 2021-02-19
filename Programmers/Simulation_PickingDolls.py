# 프로그래머스 스킬 체크 테스트 level 1

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
bucket = [4, 3, 1]
count = 0


def put(item):
    if item == bucket[-1]:
        bucket.pop(-1)
    else:
        bucket.append(item)


def solution(board, moves):
    answer = 0
    N = len(board)
    topIndex = [0] * N  # 맨 위 인형의 위치
    bucket = []  # 바구니
    for x in range(N):
        for y in range(N):
            if board[y][x] != 0:
                topIndex[x] = y
                break
    for move in moves:
        targetRow = topIndex[move - 1]
        if targetRow >= N:
            continue
        item = board[targetRow][move - 1]
        board[targetRow][move - 1] = 0
        topIndex[move - 1] += 1
        if bucket:  # 바구니가 비어있지 않을 경우
            if item == bucket[-1]:
                bucket.pop(-1)
                answer += 2
            else:
                bucket.append(item)
        else:
            bucket.append(item)

    return answer


print(solution(board, moves))