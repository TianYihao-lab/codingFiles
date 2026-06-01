n,m,q=map(int,input().split())
_list=[[0]*(m+1)for i in range(n+1)]
for i in range(1,n+1):
    line=list(map(int,input().split()))
    for j in range(1,m+1):
        _list[i][j]=line[j-1]
for i in _list:print(*i)
print()


_Sum=[[0]*(m+1)for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        _Sum[i][j]=_Sum[i-1][j]+_Sum[i][j-1]-_Sum[i-1][j-1]+_list[i][j]
for i in _Sum:print(*i)
print()


def find(x1,y1,x2,y2):  # 查询
    return _Sum[x2][y2]-_Sum[x1-1][y2]-_Sum[x2][y1-1]+_Sum[x1-1][y1-1]


for _ in range(q):
    x1,y1,x2,y2=map(int,input().split())
    print(find(x1,y1,x2,y2))