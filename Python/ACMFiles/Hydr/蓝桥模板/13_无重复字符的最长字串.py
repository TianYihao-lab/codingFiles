n=int(input())
s=input()

def test01():
    ans=0
    for i in range(n):
        _set=set()
        for j in range(i,n):
            if s[j] not in _set:
                _set.add(s[j])
                ans=max(ans,j-i+1)
            else:
                break
    print(ans)

def test02():
    _l,_r=0,0
    ans=0
    _dict={}
    for i in range(n):
        if s[i] in _dict:
            _l=max(_l,_dict[s[i]]+1)
        _dict[s[i]]=i
        ans=max(ans,i-_l+1)
        # _r+=1
    print(ans)
test02()