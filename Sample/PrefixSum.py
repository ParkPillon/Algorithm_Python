# 접두사 합
# 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해놓은 것

n = 5
data = [1, 2, 3, 4, 5]

temp_sum = 0
prefix_sum = [0]
for i in data:
    temp_sum += i
    prefix_sum.append(temp_sum)

print(f"2번부터 4번까지의 합은 {prefix_sum[4] - prefix_sum[1]}")
