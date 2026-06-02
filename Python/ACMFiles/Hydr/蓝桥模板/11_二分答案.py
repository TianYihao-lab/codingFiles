n,k=map(int,input().split())
_list=sorted(list(map(int,input().split())))

def check(m):
    tmp=k
    for i in _list:
        if i<m:
            tmp-=(m-i)
        if tmp<0:break
    return tmp>=0

# 这是一道求最大值的问题
_l,_r=_list[0],_list[0]+k
while _l<_r:
    _m=(_l+_r)>>1
    if check(_m):
        _l=_m+1
    else:
        _r=_m
print(_l-1)