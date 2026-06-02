n=int(input())

vis=[False]*(n+1)

def dfs(m):
    if m>n:
        for i in range(1,n+1):
            if vis[i]:print(i,end=' ')
        print()
        return
    
    dfs(m+1)
    vis[m]=True
    dfs(m+1)
    vis[m]=False

dfs(1)
