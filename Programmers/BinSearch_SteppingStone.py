# 프로그래머스 이분탐색
# https://programmers.co.kr/learn/courses/30/lessons/43236

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2


def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance  # 거리의 최솟값이 취할 수 있는 범위
    targetRock = len(rocks) - n  # 남겨야 하는 바위 수
    rocks.sort()
    while start <= end:
        gap = (start + end) // 2  # 거리의 최솟값이 gap 이라 가정
        count = 0
        temp = 0
        exactGap = False
        for i in range(len(rocks)):
            if rocks[i] - temp >= gap:  # gap 이상의 거리차를 둔 바위만 선택
                if rocks[i] - temp == gap:
                    exactGap = True  # 거리차가 정확히 gap
                count += 1
                temp = rocks[i]

        if count >= targetRock:  # 선택된 바위 수가 목표보다 많을 때
            start = gap + 1
            if exactGap:  # 가정한 gap이 실제 최소값일 때
                answer = gap
        else:  # 거리의 최소값을 더 작게 해서 탐색
            end = gap - 1

    return answer


print(solution(distance, rocks, n))