n,m=map(int,input().split())
_list=[[0]*(n+1)for _ in range(n+1)]

for i in range(m):
    x,y,value=map(int,input().split())
    _list[x][y]=value

# for i in _list:print(*i)