# 두개의 포인터를 활용, 특정 범위를 탐색
# 특정 합을 가지는 부분 연속 수열 찾기


def twoPointer(N, M, data):
    end = 0
    count = 0
    temp_sum = 0
    for start in range(N):
        # end를 가능한 만큼 이동시키기
        while temp_sum < M and end < N:
            temp_sum += data[end]
            end += 1
        if temp_sum == M:
            count += 1
        temp_sum -= data[start]
    return count


print(twoPointer(5, 5, [1, 2, 3, 2, 5]))
