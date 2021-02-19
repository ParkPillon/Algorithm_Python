# 카카오 2020 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059
import sys


def solution(key, lock):
    answer = False
    M, N = len(key), len(lock)
    for k in range(4):
        rotated_key = rotate90d(key, k)
        for x in range(1, M + N):
            for y in range(1, M + N):
                new_lock = expand_lock(lock, M, N)
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] += rotated_key[i][j]
                if check(new_lock, M, N):
                    answer = True
    return answer


def rotate90d(arr, k):
    m, n = len(arr), len(arr[0])
    if k == 0:
        return arr
    if k == 1:
        new_arr = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_arr[n - j - 1][i] = arr[i][j]
        return new_arr
    return rotate90d(rotate90d(arr, k - 1), 1)


def check(new_lock, M, N):
    for i in range(N):
        for j in range(N):
            if new_lock[M + i][M + j] != 1:
                return False
    return True


def expand_lock(lock, M, N):
    new_lock = [[0] * (N + 2 * M) for _ in range(N + 2 * M)]
    for i in range(N):
        for j in range(N):
            new_lock[M + i][M + j] = lock[i][j]
    return new_lock


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
M, N = len(key), len(lock)
# print(f"정답은 {solution(key,lock)}")
