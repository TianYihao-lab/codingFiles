n,m,k=map(int,input().split())

_list=[[0]*(m+1)for _ in range(n+1)]
for i in range(n):
    line=list(input().strip())
    for j in range(m):
        _list[i+1][j+1]=line[j]
# for i in _list:print(*i)

x1,y1,x2,y2=1,1,n,m
dx=[0,1,0,-1]
dy=[1,0,-1,0]

from collections import deque
Q=deque()
_set=set()
Q.append((x1,y1,_list[x1][y1],1,0))
_set.add((x1,y1))
flag=False

while Q:
    x,y,target,cnt,ans=Q.popleft()
    # print(x,y,target,cnt,ans)
    if cnt<k:
        for i in range(4):
            _x,_y=x+dx[i],y+dy[i]
            if 1<=_x<=n and 1<=_y<=m and _list[_x][_y]==target and (_x,_y) not in _set:
                if (_x,_y)==(x2,y2):
                    flag=True
                    break
                Q.append((_x,_y,_list[_x][_y],cnt+1,ans+1))
                _set.add((_x,_y))
        cnt+=1
    else:
        cnt=0
        for i in range(4):
            _x,_y=x+dx[i],y+dy[i]
            if 1<=_x<=n and 1<=_y<=m and _list[_x][_y]!=target and (_x,_y) not in _set:
                if (_x,_y)==(x2,y2):
                    flag=True
                    break
                Q.append((_x,_y,_list[_x][_y],cnt+1,ans+1))
                _set.add((_x,_y))
        if flag:break
        cnt+=1

print(ans+1)