import sys
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])   # 路径压缩
    return parent[x]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pa] = pb

for _ in range(m):
    op, a, b = input().split()
    a, b = int(a), int(b)

    if op == 'M':
        union(a, b)
    else:
        if find(a) == find(b):
            print('Yes')
        else:
            print('No')