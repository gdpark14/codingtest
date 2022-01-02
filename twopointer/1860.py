import sys
import collections

N,S=map(int,sys.stdin.readline().split())
array=list(map(int,sys.stdin.readline().split()))

ans=N+1
st=0
en=0

sum_temp=0

while st<len(array) and en<len(array) and st<=en:
    sum_temp+=array[en]

    if sum_temp>=S:
        ans=min(ans,en-st+1)
        sum_temp=sum_temp-array[en]-array[st]
        st+=1
    else:
        en+=1

if ans==N+1:
    ans=0
print(ans)