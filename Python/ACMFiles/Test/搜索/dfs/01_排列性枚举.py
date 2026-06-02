n=int(input())

_list=[0]*(n+1)
vis=[False]*(n+1)

def dfs(m):
    if m>n:
        print(*_list[1:])
        return	# 不能忘记
    
    for i in range(1,n+1):
        if not vis[i]:
            _list[m]=i			# 确定要用的数
            vis[i]=True			# 标记被用过的数
            dfs(m+1)
            vis[i]=False		# 回溯，把这个数放回去

dfs(1)
