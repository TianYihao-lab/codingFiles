s,_num=input().split()
# print(s,_num)
_num=int(_num)

def converter(s,_num):
    tmp,cnt=0,0
    length=len(s)
    for i in range(length-1,-1,-1):
        if s[i].isdigit():
            tmp+=int(s[i])*_num**cnt
        else:
            tmp+=(ord(s[i])-ord('A')+10)*_num**cnt
        cnt+=1
    return tmp

print(converter(s,_num))
