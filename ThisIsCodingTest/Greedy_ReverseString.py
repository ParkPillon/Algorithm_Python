import sys

S = sys.stdin.readline().strip()
prev_chr = "-1"
change = 0
for char in S:
    if char != prev_chr:
        change += 1
        prev_chr = char

print(change // 2)
