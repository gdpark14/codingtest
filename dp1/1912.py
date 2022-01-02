import sys
import collections

num=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

ans=[]
ans.append(nums[0])

for i in range(1,len(nums)):
    if(ans[i-1]<0):
        ans.append(nums[i])
    else:
        ans.append(ans[i-1]+nums[i])

print(max(ans))



