# 프로그래머스 도둑질
# https://programmers.co.kr/learn/courses/30/lessons/42897

money = [1, 2, 3, 1]


def solution(money):
    answer = 0
    case1 = money[:-1]  # 첫번째 집을 선택하는 경우
    case2 = money[1:]  # 첫번째 집 선택X
    cashe1, cashe2 = [0] * (len(money) - 1), [0] * (len(money) - 1)
    cashe1[0], cashe2[0] = case1[0], case2[0]
    cashe1[1], cashe2[1] = max(case1[0], case1[1]), max(case2[0], case2[1])
    for i in range(2, len(money) - 1):
        cashe1[i] = max(case1[i] + cashe1[i - 2], cashe1[i - 1])
        cashe2[i] = max(case2[i] + cashe2[i - 2], cashe2[i - 1])
    answer = max(cashe1[-1], cashe2[-1])
    return answer


print(solution(money))