n,m=map(int,input().split())

_list=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().strip().split())
    if a==b:_list[a]+=2
    else:
        _list[a],_list[b]=_list[a]+1,_list[b]+1
print(*_list[1:])