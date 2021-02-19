# 프로그래머스 정수 삼각형
# https://programmers.co.kr/learn/courses/30/lessons/43105


def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            value = triangle[i][j]
            if j > 0:
                triangle[i][j] = max(triangle[i][j], triangle[i - 1][j - 1] + value)
            if j < len(triangle[i]) - 1:
                triangle[i][j] = max(triangle[i][j], triangle[i - 1][j] + value)
    answer = max(triangle[-1])
    return answer