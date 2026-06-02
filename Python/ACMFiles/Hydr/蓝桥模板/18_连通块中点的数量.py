import sys
input=lambda:sys.stdin.readline().strip()

def find(k):
    if parents[k]!=k:
        parents[k]=find(parents[k])
    return parents[k]

def union(a,b):
    _a=find(a)
    _b=find(b)
    if _a!=_b:
        parents[_a]=parents[_b]
        vis[_b]+=vis[_a]

n,m=map(int,input().split())
parents=[i for i in range(n+1)]
vis=[1]*(n+1)
for _ in range(m):
    op=list(map(str,input().split()))

    for i in range(1,len(op)):op[i]=int(op[i])
    # for i in op:print(i,type(i))
   
    if op[0]=='C':
        union(op[1],op[2])
    elif op[0]=='Q1':
        if find(op[1])==find(op[2]):
            print('Yes')
        else:
            print('No')
    else:
        _index=find(op[1])
        print(vis[_index])