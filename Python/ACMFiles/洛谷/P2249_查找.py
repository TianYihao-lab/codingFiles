n,m=map(int,input().split())
_list=[0]+list(map(int,input().split()))
_index=list(map(int,input().split()))

def _find(q):       # 求最小值
    _l,_r=1,n
    while _l<_r:
        _m=(_l+_r)>>1
        if _list[_m]<q:
            _l=_m+1
        else:
            _r=_m
    # print(_l,_r,_list[_l])
    return  _l if _l<=n and _list[_l]==q else -1

for i in _index:
    print(_find(i))