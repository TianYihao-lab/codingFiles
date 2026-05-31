n,k=map(int,input().split())

s=''
while n!=0:
    tmp=n%k
    if tmp<10:  
        s=f'{tmp}'+s
    else:
        s=chr(ord('A')+tmp-10)+s
    n//=k
print(s)
