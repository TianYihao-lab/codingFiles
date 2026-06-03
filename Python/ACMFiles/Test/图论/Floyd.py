from math import *
n,m=map(int,input().split())

_list=[[inf]*(n+1)for _ in range(n+1)]
for i in range(1,n+1):_list[i][i]=0

for _ in range(m):
    u,v,w=map(int,input().split())
    _list[u][v]=min(_list[u][v],w)
    _list[v][u]=_list[u][v]
# for i in _list[1:]:print(*i[1:])

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            _list[i][j]=min(_list[i][j],_list[i][k]+_list[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        print(_list[i][j],end=' ')
    print()