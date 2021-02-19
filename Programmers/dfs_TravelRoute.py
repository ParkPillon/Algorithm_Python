# 프로그래머스 여행경로
# https://programmers.co.kr/learn/courses/30/lessons/43164
tickets = [
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
]
answer = []


def solution(tickets):
    global answer
    used = [0] * len(tickets)
    dfs(["ICN"], used, tickets)
    answer.sort()
    return answer[0]


def dfs(route, used, tickets):
    global answer
    if len(route) == len(tickets) + 1:
        temp = route[:]
        answer.append(temp)
        return
    dep = route[-1]
    for ticketId in possibleRoute(dep, tickets):
        a, b = tickets[ticketId]  # 출발, 도착지
        if not used[ticketId]:  # 사용하지 않은 티켓일 경우
            used[ticketId] = 1
            route.append(b)
            dfs(route, used, tickets)
            route.pop(-1)
            used[ticketId] = 0


def possibleRoute(dep, tickets):
    res = []  # 몇 번째 티켓이 사용 가능한지
    for i, ticket in enumerate(tickets):
        if ticket[0] == dep:
            res.append(i)

    return res


print(solution(tickets))
# print(possibleRoute("ICN", tickets))