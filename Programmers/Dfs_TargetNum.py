# 프로그래머스 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165
import sys
from itertools import combinations


def solution(numbers, target):
    answer = 0
    idx_list = []
    for i in range(1, len(numbers)):
        idx_list += list(combinations(list(range(len(numbers))), i))
    for idx_comb in idx_list:
        temp = numbers.copy()
        for idx in idx_comb:
            temp[idx] = -temp[idx]
        if sum(temp) == target:
            answer += 1
    return answer


numbers = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())
print(f"결과는 {solution(numbers, target)}가지")

# 좋은풀이

answer = 0


def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if idx == N and target == value:
        answer += 1
        return
    if idx == N:
        return

    DFS(idx + 1, numbers, target, value + numbers[idx])
    DFS(idx + 1, numbers, target, value - numbers[idx])


def solution2(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer