import os
import sys
input=lambda:sys.stdin.readline().strip()

# 请在此输入您的代码
_dict=dict()

n,_min,_max=map(int,input().split())
# print(n,_min,_max)

# 记录索引
for i in range(n):
  _s=input()
  length=len(_s)

  if length<_min:
    _dict[_s]=_dict.get(_s,0)+1
  else:
    for i in range(_min,_max+1):
        for j in range(length-i+1):
            tmp_s=_s[j:j+i]
            _dict[tmp_s]=_dict.get(tmp_s,0)+1

#   for i in _dict:print(i,_dict[i])
#   print()

_s=input()
length=len(_s)

if length<_min:
    print(_dict[_s])
else:
    ans=0
    for i in range(_min,_max+1):
        for j in range(length-i+1):
            tmp_s=_s[j:j+i]
            if tmp_s in _dict:
               ans+=_dict[tmp_s]
    print(ans)