# Top-down 하향식 (Memoization 방식)
# 재귀함수의 깊이 제한이 있어 주로 bottom-up방식을 사용
d = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(99))

# Bottom-up 상향식 (DP 테이블 사용)
dp = [0] * 100
dp[1] = 1
dp[2] = 1
n = 99
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])