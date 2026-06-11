n,m=map(int,input().split())

_list=[[0]*(n+1)for _ in range(n+1)]

flag=True
for _ in range(m):
    a,b=map(int,input().strip().split())
    if a==b or _list[b][a]==1 or _list[a][b]==1:
        flag=False
        break
    _list[a][b]=1
    _list[b][a]=1
# print(flag)
print('Yes' if flag else 'No')