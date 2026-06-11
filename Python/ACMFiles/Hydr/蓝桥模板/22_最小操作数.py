a,b=map(int,input().split())

from collections import deque

Q=deque()

Q.append((a,0))
while Q:
    now,cnt=Q.popleft()
    tmp01=now+1
    tmp02=now*2
    tmp03=now-1
    if tmp01==b or tmp02==b or tmp03==b:
        print(cnt+1)
        break
    Q.append((tmp01,cnt+1))
    Q.append((tmp02,cnt+1))
    Q.append((tmp03,cnt+1))