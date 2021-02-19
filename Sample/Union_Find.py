import sys

input = sys.stdin.readline


def find(x):
    if parent[x] < 0:
        return x

    y = find(parent[x])
    parent[x] = y
    return y


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
    return


n, m = map(int, input().split())
parent = [-1] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    if a:
        print("YES" if find(b) == find(c) else "NO")
    else:
        union(b, c)