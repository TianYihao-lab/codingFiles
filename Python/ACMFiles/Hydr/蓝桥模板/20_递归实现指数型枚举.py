n=int(input())

_list=[0]*(n+1)
vis=[False]*(n+1)

def dfs(m):
    if m>n:
        for i in range(1,n+1):
            if vis[i]:print(i)
        return
    
    