# 카카오 2020 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058
import sys


def solution(p):
    answer = convert(p)
    return answer


def isBracketBalanced(brackets):
    if not brackets:
        return False
    return brackets.count("(") == brackets.count(")")


def isBracketMatch(brackets):
    br_open, br_close = 0, 0
    if not brackets:
        return False
    for br in brackets:
        if br == "(":
            br_open += 1
        else:
            br_close += 1
        if br_close > br_open:
            return False
    return True


def reverseBracket(brackets):
    if not brackets:
        return ""
    return "".join(["(" if br == ")" else ")" for br in brackets])


def convert(p):
    if not p:
        return p
    if isBracketMatch(p):
        return p
    u = ""
    v = ""
    for i in range(len(p)):
        u += p[i]
        if isBracketBalanced(u):
            v += p[i + 1 :]
            break
    if isBracketMatch(u):
        return u + convert(v)
    else:
        return "(" + convert(v) + ")" + reverseBracket(u[1:-1])


p = sys.stdin.readline().strip()
print(solution(p))
# print(p.popleft())