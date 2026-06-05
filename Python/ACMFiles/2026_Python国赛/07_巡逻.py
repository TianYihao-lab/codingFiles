n,k=map(int,input().split())
edge=[[] for _ in range(n+1)]#edge[i]=[j,val],第i个节点与j相连，权值为val
for _ in range(n-1):
  a,b,c=map(int,input().split())
  edge[a].append([b,c])
  edge[b].append([a,c])
ans=0
for i in edge:print(*i)


# def dfs(par,cur,num,val):
#   global ans
#   if num==k:
#     ans+=val#经过k路径，递归终止条件
#     return
#   for i in edge[cur]:#遍历当前节点的子节点
#     if i[0]!=par:#由于该节点cur上一个节点为父节点par,那么不能回到par节点，否则会重复
#       dfs(cur,i[0],num+1,val+i[1])
# for i in range(1,n+1):#将每个节点作为初始节点即可
#   dfs(-1,i,0,0)
# print(ans)