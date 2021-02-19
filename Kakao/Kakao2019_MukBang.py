# 카카오 2019 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891
def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1
    count_food = len(food_times)
    foods = sorted(
        [[index + 1, time] for index, time in enumerate(food_times)], key=lambda t: t[1]
    )
    prev_food = 0
    for i in range(len(foods)):
        if (foods[i][1] - prev_food) * count_food < k:
            k -= (foods[i][1] - prev_food) * count_food
            count_food -= 1
            prev_food = foods[i][1]
        else:
            temp = sorted(foods[i:], key=lambda f: f[0])
            answer = temp[k % len(temp)][0]
            break
    # 복구 후 먹어야하는 음식
    return answer


import sys

food_times = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

print(f"{solution(food_times,k)}부터 먹으면 됩니다")
