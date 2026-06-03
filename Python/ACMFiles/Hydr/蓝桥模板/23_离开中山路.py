n=int(input())
_list=[[0]*(n+1)for i in range(n+1)]
for i in range(n):
    line=list(map(int,input()))
    for j in range(n):
        _list[i+1][j+1]=line[j]
for i in _list:print(*i)

# x1,y1,x2,y2=map(int,input().split())

# dx=[0,1,0,-1]
# dy=[1,0,-1,0]
# _set=set()

# from collections import deque

# Q=deque()
# Q.append((x1,y1,0))
# _set.add((x1,x2))
# flag=False
# while Q:
#     x,y,cnt=Q.popleft()
#     for i in range(4):
#         _x=x+dx[i]
#         _y=y+dy[i]
#         if (_x,_y)==(x2,y2):
#             print(cnt+1)
#             flag=True
#             break
#         if 1<=_x<=n and 1<=_y<=n and _list[_x][_y]==0 and (_x,_y) not in _set:
#             Q.append((_x,_y,cnt+1))
#             _set.add((_x,_y))
#     if flag:break