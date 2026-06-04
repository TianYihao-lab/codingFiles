import os
import sys
input=lambda:sys.stdin.readline().strip()

n,_min,_max=map(int,input().split())
# print(n,_min,_max)

def solve(s):
    length=len(s)
    _set=set()
    if length<_min:
        _set.add(s)
        return _set
    else:
        for i in range(_min,_max+1):
            for j in range(length-i+1):
                tmp_s=s[j:j+i]
                _set.add(tmp_s)
        return _set
    
ans=0
_list=[]
for _ in range(n):
    _list.append(input())

s=input()
_set=solve(s)

for i in _list:
    _set02=solve(i)
    for j in _set:
        if j in _set02:
            ans+=1
            break
print(ans)