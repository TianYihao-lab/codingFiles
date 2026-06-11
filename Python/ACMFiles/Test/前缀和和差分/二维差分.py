n,m,q=map(int,input().split())

_list = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, m+1):
        _list[i][j] = row[j-1]
for i in _list:print(*i)
print()


# 准备差分数组
_Exp=[[0 for j in range(m+2)] for i in range(n+2)]
for i in range(1,n+1):
    for j in range(1,m+1):
        _Exp[i][j]=_list[i][j]-_list[i-1][j]-_list[i][j-1]+_list[i-1][j-1]
for i in _Exp:print(*i)
print()

# 差分数组的计算
def cal(x1,y1,x2,y2,_num):
    _Exp[x1][y1]+=_num
    _Exp[x1][y2+1]-=_num
    _Exp[x2+1][y1]-=_num
    _Exp[x2+1][y2+1]+=_num

# 求原数组
def back_sum():
    _Sum=[[0 for j in range(m+2)] for i in range(n+2)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            _Sum[i][j]=_Sum[i-1][j]+_Sum[i][j-1]-_Sum[i-1][j-1]+_Exp[i][j]
    return _Sum

for _ in range(q):
    x1,y1,x2,y2,_num=map(int,input().split())
    cal(x1,y1,x2,y2,_num)

_Sum=back_sum()
for i in _Sum[1:-1]:print(*i[1:-1])