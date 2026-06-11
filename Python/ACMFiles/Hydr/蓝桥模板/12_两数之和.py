n,x=map(int,input().split())
_list=list(map(int,input().split()))
_set=set(_list)

ans=0
for i in _list:
    if i!=x-i and x-i in _set:
        ans+=1
print(ans//2)