# 프로그래머스 단속카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884

routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]


def solution(routes):
    answer = 0
    routes.sort(key=lambda route: route[1])  # 진출 위치 기준 정렬
    while routes:
        start, end = routes[0]
        answer += 1  # end 위치에 설치
        # 단속카메라로 단속하지 못하는 차량만 남김
        routes = [[f, t] for f, t in routes if not (f <= end and end <= t)]

    return answer


print(solution(routes))