# 이코테 381p 못생긴 수
# Google 인터뷰
import sys


def isUgly(num):
    while num > 1:
        if num % 2 == 0:
            num = num // 2
            continue
        if num % 3 == 0:
            num = num // 3
            continue
        if num % 5 == 0:
            num = num // 5
            continue
        return False
    return True


n = int(sys.stdin.readline())

dp = [0] * (n + 1)  # 첫번째 못생긴수는 1
for i in range(1, n + 1):
    target = dp[i - 1] + 1
    while not isUgly(target):
        target += 1
    dp[i] = target
print(dp[n])
