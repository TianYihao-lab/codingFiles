n=int(input())
_list=list(input().split())
print(*_list)
print()

ans=0
for i in range(n-1):
    tmp01,tmp02=int(_list[i]),int(_list[i+1])
    print(tmp01,tmp02,tmp01<=tmp02)
    _list02=list(_list[i+1])
    print(*_list02)
    
    if tmp01>tmp02:
        length=len(_list[i+1])
        for j in range(1,length+1):
            _list02.insert(i,'0')
            ans+=1
            tmp02=int(''.join(_list02))
            print(*_list02,tmp02,tmp01<tmp02,ans)

            if tmp02<=tmp01:
                _list02.pop(i)
                # ans-=1
                tmp02=int(''.join(_list02))
            else:
                _list[i+1]=''.join(_list02)
                break
    print()

print(ans)