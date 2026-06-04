from math import *

ans=0
for i in range(1,10**6+1):
    j=2025-(i%2025)
    # if gcd(i,j)==1:
    #     ans+=((10**6-i)//2025)
    while j<=10**6:
        if j>i and gcd(i,j)==1:ans+=1
        j+=2025
print(ans)

from math import *
def slove():        # i+j<=2000000<2025*1000
    cut = 0
    for i in range(1, 1000):
        for j in range(1, 1000000):
            b = 2025 * i - j
            if j < b <= 1000000:
                if gcd(j, b) == 1:
                    cut += 1
    print(cut)

# # slove()
# print(93816892)     # 这道题目可以靠暴力