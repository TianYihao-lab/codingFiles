n,m=map(int,input().split())
from collections import *
Q=deque(i for i in range(1,n+1))
# print(*Q)

for i in range(m):
    _list=list(map(int,input().split()))
    if _list[0]==1:
        Q.remove(_list[1])
        Q.appendleft(_list[1])
        pass
    elif _list[0]==2:
        Q.remove(_list[1])
        Q.append(_list[1])
        pass
    else:
        if _list[1]==_list[2]:
            _index=Q.index(_list[2])
            Q.insert(_list[1],_index+1)
        pass
print(*Q)