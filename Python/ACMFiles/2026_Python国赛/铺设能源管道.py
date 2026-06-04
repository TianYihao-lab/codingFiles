n=int(input())

# def cal(s):
#     _str=str(s)
#     _num=0
#     for i in _str:
#         _num+=int(i)
#     return _num


if n>=10:
    _s=list(str(n))
    for i in range(1,10):
        if str(i) in _s[1:]:
            _index=_s.index(f'{i}')
            break
        else:
            pass
    _s[_index-1]=chr(ord(_s[_index-1])+1)
    for j in range(_index,len(_s)):
        _s[j]='0'
    ans=int(''.join(_s))
else:
    ans=10
print(ans)