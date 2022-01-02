import sys
import collections

N,M=map(int,sys.stdin.readline().split())
array=[]
for i in range(N):
    a=int(input())
    array.append(a)
array=sorted(array)

ans=2000000000

st=0
en=0
while st<len(array) and en<len(array):
    if array[en]-array[st]>=M:
        ans=min(ans,array[en]-array[st])
        st+=1
    else:
        en+=1
print(ans)