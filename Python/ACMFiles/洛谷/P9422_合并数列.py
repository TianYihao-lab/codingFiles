n,m=map(int,input().split())
_listA=list(map(int,input().split()))
_listB=list(map(int,input().split()))

# def test01():
    # i,j=0,0
    # ans=0
    # while j<n and i<m:
    #     if _listA[j]==_listB[i]:
    #         pass
    #     elif _listA[j]<_listB[i]:
    #         tmp01,tmp02=_listA[j],_listB[i]
    #         while tmp01<tmp02 and j+1<n:
    #             tmp01+=_listA[j+1]
    #             j+=1
    #             ans+=1
    #         pass
    #     else:
    #         tmp01,tmp02=_listA[j],_listB[i]
    #         while i+1<m and tmp01!=tmp02:
    #             tmp02+=_listB[i+1]
    #             i+=1
    #             ans+=1
    #     i+=1
    #     j+=1
    # print(ans)

def test02():
    # i 指向 A，j 指向 B
    i, j = 0, 0
    ans = 0

    # 维护两个全局累加和，彻底避免内部循环带来的状态丢失或超载问题
    sum_a, sum_b = _listA[0], _listB[0]

    while i < n and j < m:
        if sum_a == sum_b:
            # 累加和相等，说明这一段完美匹配，指针双双推进到下一组的开头
            i += 1
            j += 1
            if i < n:
                sum_a = _listA[i]
            if j < m:
                sum_b = _listB[j]
        elif sum_a < sum_b:
            # A 的累加和较小，只推进 A 的指针并累加
            i += 1
            sum_a += _listA[i]
            ans += 1
        else:
            # B 的累加和较小，只推进 B 的指针并累加
            j += 1
            sum_b += _listB[j]
            ans += 1
            
    print(ans)

test02()