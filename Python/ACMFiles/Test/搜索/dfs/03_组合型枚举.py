n,m=map(int,input().split())

vis=[False]*(n+1)

def dfs(k,_new):
    if k>m:
        for i in range(1,n+1):
            if vis[i]:
                print(i,end=' ')
        print()
        return
    
    for i in range(_new+1,n+1):
        vis[i]=True
        dfs(k+1,i)
        vis[i]=False

dfs(1,0)