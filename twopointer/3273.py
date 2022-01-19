import sys
import collections

n=int(input())
nums=list(map(int,sys.stdin.readline().split()))
k=int(input())
nums.sort()

end=n-1
count=0
for i in range(n):
    start=i
    temp=nums[start]+nums[end]
    while temp>k and start+1<end:
        end-=1
        temp=nums[start]+nums[end]
    if temp==k:
        count+=1
print(count)