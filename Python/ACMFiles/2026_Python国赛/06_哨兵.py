import sys
sys.setrecursionlimit(200000)
n=int(input())
g=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
# for i in g:print(*i)

res,p=-1,-1
def dfs(u,f,d):
    global res,p
    if d>res:
        res=d
        p=u
    for v in g[u]:
        if v!=f:
            dfs(v,u,d+1)
dfs(1,-1,0)
st=p
res=-1
dfs(st,-1,0)
if res%2==0:
    print(res)
else:
    print(res-1)