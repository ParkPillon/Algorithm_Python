# 프로그래머스 이분탐색 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238


n = 6
times = [7, 10]


def solution(n, times):
    answer = 0
    start, end = 0, n * max(times)

    while start <= end:
        total = (start + end) // 2
        if how_many(total, times) >= n:
            answer = total
            end = total - 1
        else:
            start = total + 1
    return answer


def how_many(total, times):
    answer = 0
    for t in times:
        answer += total // t
    return answer


print(solution(n, times))
