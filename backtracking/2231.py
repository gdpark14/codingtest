import sys
import collections

N=int(input())

ans=0
for i in range(1,N+1):
    num=sum(list(map(int,str(i))))
    check=num+i
    if check==N:
        ans=i
        break

print(ans)
x=map(int,'12345')