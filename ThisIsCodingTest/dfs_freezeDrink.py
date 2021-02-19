def solution(N, M, frame):
    answer = 0
    for n in range(N):
        for m in range(M):
            if dfs(n, m, frame):
                answer += 1
    return answer


def dfs(x, y, frame):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    if frame[x][y] == 0:
        frame[x][y] = 1
        dfs(x - 1, y, frame)
        dfs(x, y - 1, frame)
        dfs(x, y + 1, frame)
        dfs(x + 1, y, frame)
        return True
    return False


import sys


N, M = map(int, sys.stdin.readline().split())
frame = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

print(f"총 {solution(N,M,frame)}개의 음료수를 만들 수 있습니다")
