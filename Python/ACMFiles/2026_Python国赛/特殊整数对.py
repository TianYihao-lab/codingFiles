from math import *

ans=0
for i in range(1,10**6+1):
    j=2025-(i%2025)
    # if gcd(i,j)==1:
    #     ans+=((10**6-i)//2025)
    while j<=10**6:
        if gcd(i,j)==1:ans+=1
        j+=2025
print(ans)