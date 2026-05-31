n,m=map(int,input().split())

_list=[0]+list(map(int,input().split()))

# 差分数组初始化
_Ext=[0]*(n+2)
for i in range(1,n+1):
	_Ext[i]=_list[i]-_list[i-1]


def cal(a,b,i):
	_Ext[a]+=i
	_Ext[b]-=i
	
	
# 通过差分数组求原数组(前缀和)	
def back_sum():
	_Sum=[0]*(n+1)		
	for i in range(1,n+1):
		_Sum[i]=_Sum[i-1]+_Ext[i]
	return _Sum
	
for i in range(m):
	a,b,i=map(int,input().split())
	cal(a,b,i)
_Sum=back_sum()
print(*_Sum[1:])