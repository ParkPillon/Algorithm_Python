import sys

S = sys.stdin.readline().strip()
num_total = 0
onlyChr = "".join([s for s in S if s >= "A" and s <= "Z"])
onlyNum = sum(map(int, [s for s in S if s >= "0" and s <= "9"]))
answer = onlyChr + str(onlyNum)