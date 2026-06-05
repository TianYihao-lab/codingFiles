n=int(input())
_list=[]
_dict=dict()
for _ in range(n):
    value,route=input().split()
    routes=list(route.split('/'))
    _list.append(routes)
    _dict[tuple(routes)]=value

m=int(input())
for _ in range(m):  
    routes=list(input().split())
    for i in _list:
        j,k=0,0
        flag=True
        while j<len(i):
            if i[j]==routes[k] or i[j]=='*':
                j+=1
                k+=1
            elif i[j]=='**':
                while i[j+1]!=routes[k]:    
                    k+=1
            else:
                flag=False
                print('SAFE')
                break
            if not flag and k==len(routes):
                flag=False
                print('SAFE')
                break
        if flag:
            print(f'ALERT:{_dict[tuple(i)]}')
        break