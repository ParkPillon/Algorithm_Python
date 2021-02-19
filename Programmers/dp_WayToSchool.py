# 프로그래머스 등굣길
# https://programmers.co.kr/learn/courses/30/lessons/42898
m, n = 4, 3
puddles = [[2, 2]]


def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000007

    return dp[n][m]


print(solution(m, n, puddles))
