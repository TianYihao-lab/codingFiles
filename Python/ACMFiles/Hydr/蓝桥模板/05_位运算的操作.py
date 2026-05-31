n,m=map(int,input().split())

def to_2(n):
  n = str(bin(n)[2:])
  return n

tmp_n=to_2(n)
for i in range(m):
    actions=list(map(int,input().split()))
    if actions[0]==1:
        # print(tmp_n)
        print(tmp_n[-actions[1]])
        pass
    elif actions[0]==2:
        tmp_n=list(tmp_n)
        for i in range(-actions[1]-1,-actions[2]-2,-1):
            tmp_n[i]=str((int(tmp_n[i])+1)%2)
        print(int(''.join(tmp_n),2))
        pass
    elif actions[0]==3:
        tmp_n=list(tmp_n)
        for i in range(-actions[1]-1,-actions[2]-2,-1):
            tmp_n[i]='1'
        print(int(''.join(tmp_n),2))
        pass
    elif actions[0]==4:
        tmp_n=list(tmp_n)
        for i in range(-actions[1]-1,-actions[2]-2,-1):
            tmp_n[i]='0'
        print(int(''.join(tmp_n),2))
        pass
    else:
        length=len(tmp_n)
        for i in range(length-1,-1,-1):
            if tmp_n[i]=='1':
                print(length-i)
                break
        