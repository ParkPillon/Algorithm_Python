# 카카오 2020 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062


import sys
from itertools import permutations

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]


def solution(n, weak, dist):
    answer = 1e9
    total_weak = len(weak)
    friends_perm = list(permutations(dist))
    for i in range(total_weak):  # 원형의 리스트를 길이두배 일자형으로
        weak.append(weak[i] + n)
    for start in range(total_weak):  # 각 취약점을 출발지점으로
        start_pos = weak[start]
        for friends in friends_perm:  # 모든 친구들의 순서에 대해
            # print(f"취약점위치: {weak}")
            # print(f"친구순서: {friends}")
            count = 1
            end_pos = start_pos + friends[count - 1]
            # print(f"첫번째 친구가 {start_pos}부터 {end_pos}까지 점검")
            for weak_point in weak[
                start + 1 : start + total_weak
            ]:  # 출발점 이후의 취약점들에 대해 점검이 되는지 확인
                if end_pos < weak_point:
                    count += 1
                    if count > len(dist):
                        break
                    end_pos = weak_point + friends[count - 1]
                    # print(f"{count}번째 친구가 {end_pos}까지 점검")
            answer = min(answer, count)
    if answer > len(dist):  # 모든 친구를 투입해도 점검 불가
        return -1
    return answer


print(f"결과는 {solution(n,weak,dist)}")
