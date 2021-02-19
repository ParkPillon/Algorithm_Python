# 백준 14888번 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
import sys

N = int(sys.stdin.readline())
arguments = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))
ans_max, ans_min = -1e9, 1e9


def solution(current, size, idx, plus, minus, multi, divide):
    global ans_max, ans_min
    if size == N:
        ans_max = max(ans_max, current)
        ans_min = min(ans_min, current)
    else:
        if plus:
            solution(
                current + arguments[idx],
                size + 1,
                idx + 1,
                plus - 1,
                minus,
                multi,
                divide,
            )
        if minus:
            solution(
                current - arguments[idx],
                size + 1,
                idx + 1,
                plus,
                minus - 1,
                multi,
                divide,
            )
        if multi:
            solution(
                current * arguments[idx],
                size + 1,
                idx + 1,
                plus,
                minus,
                multi - 1,
                divide,
            )
        if divide:
            if current < 0:
                solution(
                    -((-current) // arguments[idx]),
                    size + 1,
                    idx + 1,
                    plus,
                    minus,
                    multi,
                    divide - 1,
                )
            else:
                solution(
                    current // arguments[idx],
                    size + 1,
                    idx + 1,
                    plus,
                    minus,
                    multi,
                    divide - 1,
                )


solution(arguments[0], 1, 1, *operators)
print(ans_max, ans_min, sep="\n")
