n,q=map(int,input().split())
_list=[0]+list(map(int,input().split()))        # 这道题目的顺序从0开始

def test01():
    def quiry01(a,b,cnt):       # 求符合要求的最小值
        # print(_list[a:b+1])
        _l,_r=a,b+1
        while _l<_r:
            _mid=(_l+_r)>>1
            if _list[_mid]>=cnt:
                _r=_mid
            else:
                _l=_mid+1
        # print(_l,_r,_list[_l])
        return _l if _list[_l]==cnt else -1

    def quiry02(a,b,cnt):       # 求符合要求的最大值
        # print(_list[a:b+1])
        _l,_r=a,b+1
        while _l<_r:
            _mid=(_l+_r)>>1
            if _list[_mid]<=cnt:
                _l=_mid+1
            else:
                _r=_mid
        # print(_l,_r,_list[_l])
        return _l-1 if _list[_l-1]==cnt else -1

    def quiry03(a,b,cnt):       # 求符合要求的最小值
        # print(_list[a:b+1])
        _l,_r=a,b+1  
        while _l<_r:
            _mid=(_l+_r)>>1
            if _list[_mid]>=cnt:
                _r=_mid
            else:
                _l=_mid+1
        # print(_l,_r,_list[_l])
        # return _l if _list[_l]>=cnt else -1
        return _l if _l <= b and _list[_l] >= cnt else -1

    def quiry04(a,b,cnt):       # 求符合要求的最小值
        # print(_list[a:b+1])
        _l,_r=a,b+1
        while _l<_r:
            _mid=(_l+_r)>>1
            if _list[_mid]>cnt:
                _r=_mid
            else:
                _l=_mid+1
        # print(_l,_r,_list[_l])
        # return _l if _list[_l]>cnt else -1
        return _l if _l <= b and _list[_l] > cnt else -1



    for i in range(q):
        m,l,r,x=map(int,input().split())
        if m==1:
            print(quiry01(l,r,x))
        elif m==2:
            print(quiry02(l,r,x))
        elif m==3:
            print(quiry03(l,r,x))
        else:
            print(quiry04(l,r,x))

from bisect import *
def test02():
    for i in range(q):
        m,l,r,x=map(int,input().split())
        if m==1:
            _index=bisect_left(_list[l:r+1],x)+l
            if _list[_index]==x and l<=_index<=r:
                print(_index)
            else:
                print(-1)
        elif m==2:
            _index=bisect_right(_list[l:r+1],x+1)+l
            if _list[_index-1]==x and l<=_index-1<=r:
                print(_index-1)
            else:
                print(-1)
        elif m==3:
            _index=bisect_left(_list[l:r+1],x)+l
            if l<=_index<=r:
                print(_index)
            else:
                print(-1)
                # print(bisect_left(_list[l:r+1],x)+l)
        else:
            _index=bisect_right(_list[l:r+1],x)+l
            if l<=_index<=r:
                print(_index)
            else:
                print(-1)
            # print(bisect_right(_list[l:r+1],x)+l)

test02()