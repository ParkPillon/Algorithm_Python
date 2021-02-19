# 카카오 2020 기둥과 보
# https://programmers.co.kr/learn/courses/30/lessons/60061


import sys

n = int(sys.stdin.readline())
build_frame = eval(sys.stdin.readline().strip())

# n = 5
# build_frame = [
#     [0, 0, 0, 1],
#     [2, 0, 0, 1],
#     [4, 0, 0, 1],
#     [0, 1, 1, 1],
#     [1, 1, 1, 1],
#     [2, 1, 1, 1],
#     [3, 1, 1, 1],
#     [2, 0, 0, 0],
#     [1, 1, 1, 0],
#     [2, 2, 0, 1],
# ]


def possible(answer):
    for frame in answer:
        x, y, stuff = frame
        if stuff == 0:  # 기둥일 경우
            if not (
                y == 0
                or [x - 1, y, 1] in answer
                or [x, y, 1] in answer
                or [x, y - 1, 0] in answer
            ):
                return False
        else:  # 보일 경우
            if not (
                [x, y - 1, 0] in answer
                or [x + 1, y - 1, 0] in answer
                or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)
            ):
                return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operation = frame
        if operation == 0:  # 삭제의 경우
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        else:  # 설치의 경우
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    answer.sort()
    return answer


print(f"결과는 {solution(n,build_frame)}")