n=int(input())

# def cal(s):
#     _str=str(s)
#     _num=0
#     for i in _str:
#         _num+=int(i)
#     return _num


if n!=1:
    # length=len(str(n))        # 使用n会导致 100->1000
    length=len(str(n-1))        # 使用n-1可以避免这个情况
    ans=10**(length)
else:
    ans=1
print(ans)