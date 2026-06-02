n,m=map(int,input().split())
from collections import *
Q=deque(i for i in range(1,n+1))
# print(*Q)

for i in range(m):
    _list=list(map(int,input().split()))
    if _list[0]==1:
        # print(*Q)
        Q.remove(_list[1])
        Q.appendleft(_list[1])
        # print(*Q)
        # print()
        pass
    elif _list[0]==2:
        # print(*Q)
        Q.remove(_list[1])
        Q.append(_list[1])
        # print(*Q)
        # print()
        pass
    else:
        # print(*Q)
        if _list[1]!=_list[2]:
            Q.remove(_list[1])
            _index=Q.index(_list[2])
            Q.insert(_index+1,_list[1])
        # print(*Q)
        # print()
        pass
# print()
print(*Q)