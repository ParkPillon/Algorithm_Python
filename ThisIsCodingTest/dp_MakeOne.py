# 이코테 1로 만들기

dp = [0] * 27
dp[1] = 0
for i in range(2, 27):
    answer = 1 + dp[i - 1]
    if i % 5 == 0:
        answer = min(answer, 1 + dp[i // 5])
    if i % 3 == 0:
        answer = min(answer, 1 + dp[i // 3])
    if i % 2 == 0:
        answer = min(answer, 1 + dp[i // 2])
    dp[i] = answer
    print(dp)
print(dp[26])