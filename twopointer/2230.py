import sys
import collections

N,M=map(int,sys.stdin.readline().split())
array=[]
for i in range(N):
    temp=int(input())
    array.append(temp)

array.sort()


end=0
ans=2000000000
for i in range(N):
    start=i
    temp=array[end]-array[start]
    while temp<M and end<N-1:
        end+=1
        temp=array[end]-array[start]
    if temp>=M:
        ans=min(ans,temp)
print(ans)