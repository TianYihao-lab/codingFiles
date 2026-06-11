_list=[0]*(101)
def solve(n):
  if n==1 or n==2:return 1
  if _list[n]!=0:return _list[n]
  _list[n]=solve(n-1)+solve(n-2)
  return _list[n]

solve(100)
for i,j in enumerate(_list):print(i,j)

ans=0
for i in range(1,61):
  if _list[i]%10==7:ans+=1
print(ans)
print(202202011200//60*8)
print(202202011200%60)