from collections import deque
m=int(input())
Q=deque()

for i in range(m):
    _list=list(input().split())
    if _list[0]=='push':
        Q.appendleft(int(_list[1]))
        pass
    elif _list[0]=='pop':
        if len(Q)>0:
            Q.popleft()
        pass
    elif _list[0]=='query':
        if len(Q)>0:
            tmp=Q.popleft()
            print(tmp)
            Q.appendleft(tmp)
        else:
            print('empty')
        pass
    else:
        if len(Q)==0:
            print('YES')
        else:
            print('NO')


